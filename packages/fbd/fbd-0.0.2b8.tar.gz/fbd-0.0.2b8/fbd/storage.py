#!/usr/local/bin/python3
# STL imports
import datetime
import json
import logging
import pprint

# Package imports
import dateutil.parser
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (relationship, scoped_session, sessionmaker,
                            validates)

import fbd.tools


def default_json_serializer(obj):
    '''
    JSON serializer for storage objects not supported by the default package
    '''
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    if (isinstance(obj, Topic) or isinstance(obj, Place) or
            isinstance(obj, Event)):
        return obj.to_dict()
    raise TypeError('{} type could not be serialized.'.format(type(obj)))


Base = declarative_base()

place_topic = sqlalchemy.Table(
    'Place_Topic',
    Base.metadata,
    sqlalchemy.Column('place_id', sqlalchemy.String,
                      sqlalchemy.ForeignKey('Place.id')),
    sqlalchemy.Column('topic_id', sqlalchemy.String,
                      sqlalchemy.ForeignKey('Topic.id')),
)


class Topic(Base):
    __tablename__ = 'Topic'

    @classmethod
    def from_dict(cls, topic_dict):
        return cls(id=topic_dict.get('id'), name=topic_dict.get('name'))

    def to_json(self):
        return json.dumps(
            self.to_dict(),
            default=default_json_serializer,
            separators=(',', ':'),
        )

    def to_dict(self):
        return {'id': self.id, 'name': self.name}

    id = sqlalchemy.Column(sqlalchemy.String(200), primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(100))
    places = relationship('Place', secondary=place_topic)

    @validates('name')
    def validate_trunc(self, key, value):
        max_len = getattr(self.__class__, key).prop.columns[0].type.length
        if value and len(value) > max_len:
            return value[:max_len]
        return value

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Place(Base):
    __tablename__ = 'Place'

    @classmethod
    def from_dict(cls, place_dict):
        place_loc = place_dict.get('location', {})
        topic_list = []
        if place_dict.get('place_dict_topics'):
            topic_list = [Topic.from_dict(topic_dict)
                          for topic_dict
                          in place_dict['place_dict_topics'].get('data')]
        return cls(id=place_dict['id'],
                   topics=topic_list,
                   ptype=place_dict.get('place_dict_type', 'UNKNOWN'),
                   name=place_dict.get('name', 'Unnamed'),
                   city=place_loc.get('city', 'Wroclaw'),
                   country=place_loc.get('country', 'Poland'),
                   lat=place_loc.get('latitude', 0.0),
                   lon=place_loc.get('longitude', 0.0),
                   street=place_loc.get('street', 'Unknown'),
                   zip=place_loc.get('zip', '00-000'))

    def to_json(self):
        return json.dumps(
            self.to_dict(),
            default=default_json_serializer,
            separators=(',', ':'),
        )

    def to_dict(self):
        # IDEA: Add events=T/F flag?
        # IDEA: Auto-generate fields?
        return {
            'id': self.id,
            'name': self.name,
            'ptype': self.ptype,
            'topics': [topic.to_dict() for topic in self.topics],
            'city': self.city,
            'country': self.country,
            'lat': self.lat,
            'lon': self.lon,
            'street': self.street,
            'zip': self.zip,
        }

    id = sqlalchemy.Column(sqlalchemy.String(200), primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(100))
    ptype = sqlalchemy.Column(sqlalchemy.String(10))
    city = sqlalchemy.Column(sqlalchemy.String(25))
    country = sqlalchemy.Column(sqlalchemy.String(25))
    lat = sqlalchemy.Column(sqlalchemy.Float())
    lon = sqlalchemy.Column(sqlalchemy.Float())
    street = sqlalchemy.Column(sqlalchemy.String(100))
    topics = relationship('Topic', secondary=place_topic, cascade='save-update')
    zip = sqlalchemy.Column(sqlalchemy.String(6))

    @validates('name', 'ptype', 'street', 'country', 'zip')
    def validate_trunc(self, key, value):
        max_len = getattr(self.__class__, key).prop.columns[0].type.length
        if value and len(value) > max_len:
            return value[:max_len]
        return value

    def __init__(self, id, name, topics, ptype, city, country, lat, lon, street,
                 zip):
        self.id = id
        self.name = name
        self.ptype = ptype
        self.topics = topics
        self.city = city
        self.country = country
        self.lat = lat
        self.lon = lon
        self.street = street
        self.zip = zip

    def __repr__(self):
        return '<Place {} - {}>'.format(self.id, self.name)

    def __str__(self):
        return '<Place {} - {}>'.format(self.id, self.name)


class Event(Base):
    __tablename__ = 'Event'

    @classmethod
    def from_dict(cls, event_dict):
        return cls(
            id=event_dict['id'],
            desc=event_dict.get('description', 'None'),
            name=event_dict['name'],
            picture_url=event_dict.get('picture', {})
            .get('data', {}).get('url', 'None'),
            ticket_url=event_dict.get('ticket_uri', 'None'),
            place_id=event_dict.get['place_id'],
            start_time=dateutil.parser.parse(
                event_dict.get(
                    'start_time',
                    '2017-04-07T16:00:00+0200',
                )),
        )

    def to_json(self):
        return json.dumps(
            self.to_dict(),
            default=default_json_serializer,
            separators=(',', ':'),
        )

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'start_time': self.start_time,
            'place_id': self.place_id,
            'picture_url': self.picture_url,
            'ticket_url': self.ticket_url,
        }

    id = sqlalchemy.Column(sqlalchemy.String(200), primary_key=True)
    description = sqlalchemy.Column(sqlalchemy.String(10000))
    name = sqlalchemy.Column(sqlalchemy.String(100))
    picture_url = sqlalchemy.Column(sqlalchemy.String(150))
    ticket_url = sqlalchemy.Column(sqlalchemy.String(150))
    start_time = sqlalchemy.Column(sqlalchemy.DateTime)

    place_id = sqlalchemy.Column(
        sqlalchemy.String(50), sqlalchemy.ForeignKey('Place.id'))
    place = relationship('Place', backref='events', foreign_keys=[place_id])

    @validates('description', 'name')
    def validate_trunc(self, key, value):
        max_len = getattr(self.__class__, key).prop.columns[0].type.length
        if value and len(value) > max_len:
            return value[:max_len]
        return value

    @validates('picture_url', 'ticket_url')
    def validate_strict(self, key, value):
        max_len = getattr(self.__class__, key).prop.columns[0].type.length
        if value and len(value) > max_len:
            return 'None'
        return value

    def __init__(self, id, desc, name, picture_url, ticket_url, start_time,
                 place_id):
        self.id = id
        self.name = name
        self.description = desc
        self.start_time = start_time
        self.place_id = place_id
        self.picture_url = picture_url
        self.ticket_url = ticket_url

    def __repr__(self):
        return '<Event {} - {}>\n{}'.format(self.id, self.name,
                                            pprint.pformat(self.to_dict()))

    def __str__(self):
        return pprint.pformat(self.to_dict())


# TODO: Implement 'Page' class
# class Page(Base):
#     __tablename__ = 'Page'
#     id = sqlalchemy.Column(sqlalchemy.String(50), primary_key=True)
#     message = sqlalchemy.Column(sqlalchemy.String(10000))
#     link = sqlalchemy.Column(sqlalchemy.String(150))
#     created_time = sqlalchemy.Column(sqlalchemy.DateTime)
#
#     like = sqlalchemy.Column(sqlalchemy.Integer())
#     love = sqlalchemy.Column(sqlalchemy.Integer())
#     haha = sqlalchemy.Column(sqlalchemy.Integer())
#     wow = sqlalchemy.Column(sqlalchemy.Integer())
#     sad = sqlalchemy.Column(sqlalchemy.Integer())
#     angry = sqlalchemy.Column(sqlalchemy.Integer())
#     thankful = sqlalchemy.Column(sqlalchemy.Integer())
#
#     page_id = sqlalchemy.Column(sqlalchemy.String(50), sqlalchemy.ForeignKey('Page.id'))
#     page = relationship('Page', backref='posts', foreign_keys=[page_id])
#
#     @validates('message')
#     def validate_trunc(self, key, value):
#         max_len = getattr(self.__class__, key).prop.columns[0].type.length
#         if value and len(value) > max_len:
#             return value[:max_len]
#         return value
#
#     @validates('link')
#     def validate_strict(self, key, value):
#         max_len = getattr(self.__class__, key).prop.columns[0].type.length
#         if value and len(value) > max_len:
#             return 'None'
#         return value
#
#     def __init__(self, id, page_id, message, link, created_time, like, love, haha, wow, sad, angry, thankful):
#         self.id = id
#         self.message = message
#         self.page_id = page_id
#         self.message = message
#         self.link = link
#         self.created_time = created_time
#         self.like = like
#         self.love = love
#         self.haha = haha
#         self.wow = wow
#         self.sad = sad
#         self.angry = angry
#         self.thankful = thankful
#
#     def __repr__(self):
#         return '<Post {} - {}>'.format(self.id, self.message[:25])
#
#     def __str__(self):
#         return '<Post {} - {}>'.format(self.id, self.message[:25])

# TODO: Implement 'Post' class
# class Post(Base):
#     __tablename__ = 'Post'
#     id = sqlalchemy.Column(sqlalchemy.String(50), primary_key=True)
#     message = sqlalchemy.Column(sqlalchemy.String(10000))
#     link = sqlalchemy.Column(sqlalchemy.String(150))
#     created_time = sqlalchemy.Column(sqlalchemy.DateTime)
#
#     like = sqlalchemy.Column(sqlalchemy.Integer())
#     love = sqlalchemy.Column(sqlalchemy.Integer())
#     haha = sqlalchemy.Column(sqlalchemy.Integer())
#     wow = sqlalchemy.Column(sqlalchemy.Integer())
#     sad = sqlalchemy.Column(sqlalchemy.Integer())
#     angry = sqlalchemy.Column(sqlalchemy.Integer())
#     thankful = sqlalchemy.Column(sqlalchemy.Integer())
#
#     page_id = sqlalchemy.Column(sqlalchemy.String(
#         50), sqlalchemy.ForeignKey('Page.id'))
#     page = relationship('Page', backref='posts', foreign_keys=[page_id])
#
#     @validates('message')
#     def validate_trunc(self, key, value):
#         max_len = getattr(self.__class__, key).prop.columns[0].type.length
#         if value and len(value) > max_len:
#             return value[:max_len]
#         return value
#
#     @validates('link')
#     def validate_strict(self, key, value):
#         max_len = getattr(self.__class__, key).prop.columns[0].type.length
#         if value and len(value) > max_len:
#             return 'None'
#         return value
#
#     def __init__(self, id, page_id, message, link, created_time, like, love, haha, wow, sad, angry, thankful):
#         self.id = id
#         self.message = message
#         self.page_id = page_id
#         self.link = link
#         self.created_time = created_time
#         self.like = like
#         self.love = love
#         self.haha = haha
#         self.wow = wow
#         self.sad = sad
#         self.angry = angry
#         self.thankful = thankful
#
#     def __repr__(self):
#         return '<Post {} - {}>'.format(self.id, self.message[:25])
#
#     def __str__(self):
#         return '<Post {} - {}>'.format(self.id, self.message[:25])
#
#


class Storage:

    def __init__(self, db_url='sqlite:///db/fb.sqlite'):
        self.db = sqlalchemy.create_engine(db_url)
        try:
            Base.metadata.create_all(self.db)
        except Exception as e:
            logging.debug(e)
            pass
        session = scoped_session(sessionmaker(bind=self.db))
        self.session_factory = session
        self.session = self.session_factory()

    def __del__(self):
        self.session_factory.remove()

    def save_eventlist(self, eventlist, commit=True):
        try:
            eventlist = [Event.from_dict(event_dict)
                         for event_dict in eventlist]
            self.session.bulk_save_objects(eventlist)
            if commit:
                self.session.commit()
        except sqlalchemy.exc.IntegrityError as e:
            logging.debug(f'Storage.save_eventlist: {e}')
            self.session.rollback()
        except Exception as e:
            self.session.rollback()
            logging.exception(f'Storage.save_eventlist: {e}')

    def save_placelist(self, placelist, commit=True):
        try:
            placelist = [Place.from_dict(pdict)
                         for pdict in placelist]
            self.session.bulk_save_objects(placelist)
            if commit:
                self.session.commit()
        except sqlalchemy.exc.IntegrityError as e:
            logging.debug(f'Storage.save_placelist: {e}')
            self.session.rollback()
        except Exception as e:
            self.session.rollback()
            logging.exception(f'Storage.save_placelist: {e}')

    def save_topiclist(self, topiclist, commit=True):
        try:
            topiclist = [Topic.from_dict(topic_dict)
                         for topic_dict in topiclist]
            self.session.bulk_save_objects(topiclist)
            if commit:
                self.session.commit()
        except sqlalchemy.exc.IntegrityError as e:
            logging.debug(f'Storage.save_topiclist: {e}')
            self.session.rollback()
        except Exception as e:
            self.session.rollback()
            logging.exception(f'Storage.save_topiclist: {e}')

    def save_event(self, event_dict, commit=True):
        try:
            event = Event.from_dict(event_dict)
            self.session.add(event)
            if commit:
                self.session.commit()
        except sqlalchemy.exc.IntegrityError as e:
            logging.debug(f'Storage.save_event: {e}')
            self.session.rollback()
        except Exception as e:
            self.session.rollback()
            logging.exception(f'Storage.save_event: {e}')

    def save_topic(self, topic_dict, commit=True):
        try:
            if self.topic_exists(topic_dict.get('id')):
                return self.get_topic(topic_dict.get('id'))
            topic = Topic.from_dict(topic_dict)
            self.session.add(topic)
            if commit:
                self.session.commit()
            return topic
        except sqlalchemy.exc.IntegrityError as e:
            logging.debug(f'Storage.save_topic: {e}')
            self.session.rollback()
        except Exception as e:
            self.session.rollback()
            logging.exception(f'Storage.save_topic: {e}')

    def save_place(self, place_dict, commit=True):
        try:
            place = Place.from_dict(place_dict)
            self.session.add(place)
            if commit:
                self.session.commit()
        except sqlalchemy.exc.IntegrityError as e:
            logging.debug(f'Storage.save_place: {e}')
            self.session.rollback()
        except Exception as e:
            self.session.rollback()
            logging.exception(f'Storage.save_place: {e}')

    def update_place(self, place, commit=True):
        # TODO: update and use session.merge
        logging.debug(f'Storage: update_place request, place = {place}')
        try:
            # IDEA: Move this to the place class and pass in a string list
            if self.place_exists(place.get('id')):
                place_loc = place.get('location', {})
                topic_list = []
                if place.get('place_topics', None):
                    for topic in place['place_topics'].get('data'):
                        topic_list.append(
                            Topic.from_dict({
                                'name': topic['name'],
                                'id': topic['id']
                            }))
                old_place = self.get_place(place['id'])
                old_place.topics = topic_list
                old_place.ptype = place.get('place_type', 'UNKNOWN')
                old_place.name = place['name']
                old_place.city = place_loc.get('city')
                old_place.country = place_loc.get('country')
                old_place.lat = place_loc['latitude']
                old_place.lon = place_loc['longitude']
                old_place.street = place_loc.get('street')
                old_place.zip = place_loc.get('zip')
                if commit:
                    self.session.commit()
                return old_place
            else:
                return self.save_place(place, commit)
        except sqlalchemy.exc.IntegrityError as e:
            logging.debug(f'Storage.update_place: {e}')
            self.session.rollback()
        except Exception as e:
            self.session.rollback()
            logging.exception(f'Storage.update_place: {e}')

    def save_post(self):
        pass

    def save_page(self):
        pass

    def get_all_place_ids(self):
        return [id[0] for id in self.session.query(Place.id).all()]

    def get_all_event_ids(self):
        return [id[0] for id in self.session.query(Event.id).all()]

    def get_all_topic_ids(self):
        return [id[0] for id in self.session.query(Topic.id).all()]

    def get_place(self, place_id):
        return self.session.query(Place).filter_by(id=place_id).scalar()

    def get_topic(self, topic_id):
        return self.session.query(Topic).filter_by(id=topic_id).scalar()

    def topic_exists(self, topic_id):
        return (True if self.session.query(Topic.id).filter_by(
            id=topic_id).scalar() is not None else False)

    def place_exists(self, place_id):
        return (True if self.session.query(Place.id).filter_by(
            id=place_id).scalar() is not None else False)

    def get_event(self, event_id):
        return self.session.query(Event).filter_by(id=event_id).scalar()

    def event_exists(self, event_id):
        return (True if self.session.query(Event.id).filter_by(
            id=event_id).scalar() is not None else False)

    def get_events_coords(self, lat, lon, distance=2000,
                          date=datetime.datetime.today()):

        dlat = fbd.tools.lat_from_met(distance)
        dlon = fbd.tools.lon_from_met(distance)

        # Get the circle
        left, right = lon - dlon, lon + dlon
        bottom, top = lat - dlat, lat + dlat

        places = (self.session.query(Place).filter(Place.lat >= bottom)
                  .filter(Place.lat <= top).filter(Place.lon >= left)
                  .filter(Place.lon <= right).all())

        events = [
            event.to_dict() for place in places for event in place.events
            if event.start_time > date
        ]

        return events

    def get_places_coords(self, lat, lon, distance=2000):

        dlat = fbd.tools.lat_from_met(distance)
        dlon = fbd.tools.lon_from_met(distance)

        # Get the circle
        left, right = lon - dlon, lon + dlon
        bottom, top = lat - dlat, lat + dlat

        places = (self.session.query(Place).filter(Place.lat >= bottom)
                  .filter(Place.lat <=
                          top).filter(Place.lon >=
                                      left).filter(Place.lon <= right).all())

        return places


if __name__ == '__main__':
    s = Storage()
    pprint.pprint(s.get_events_coords(51.1, 17.01))
