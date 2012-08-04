from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.orm.interfaces import MapperExtension, EXT_CONTINUE, EXT_STOP
from zope.sqlalchemy import ZopeTransactionExtension

from dhillon_site.lib.util import metaproperty

Session = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))

def initialize(engine):
    Session.configure(bind=engine)
    Model.metadata.bind = engine

    # TODO: make this conditional on debugging state
    Model.metadata.create_all(engine)

class MapperExtensionProxy(MapperExtension):
    def before_insert(self, mapper, connection, instance):
        if hasattr(instance, 'before_insert'):
            instance.before_insert()

    def after_insert(self, mapper, connection, instance):
        if hasattr(instance, 'after_insert'):
            instance.after_insert()

    def before_update(self, mapper, connection, instance):
        if hasattr(instance, 'before_update'):
            instance.before_update()

    def after_update(self, mapper, conenction, instance):
        if hasattr(instance, 'after_update'):
            instance.after_update()

    def init_instance(self, mapper, cls, oldinit, instance, args, kwargs):
        if hasattr(instance, 'init_instance'):
            instance.init_instance(*args, **kwargs)

    def create_instance(self, mapper, context, row, cls):
        if hasattr(cls, 'create_instance'):
            return cls.create_instance(row)
        else:
            return EXT_CONTINUE

    def reconstruct_instance(self, mapper, instance):
        if hasattr(instance, 'reconstruct_instance'):
            return instance.reconstruct_instance()

class MetaModel(DeclarativeMeta):
    def __new__(metacls, name, bases, d):
        if '__mapper_args__' not in d:
            d = {}

        d.get('__mapper_args__').update({
            'extension': MapperExtensionProxy()
        })

        return type.__new__(name, bases, d)

    @metaproperty
    def query(cls):
        return Session.query(cls)

    def delete(cls, instance):
        Session.object_session(instance).delete(instance)

    def get(cls, v):
        try:
            return cls.query.get(v)
        except NoResultFound:
            return None

class Model(object):
    __mapper_args__ = {'extension': MapperExtensionProxy()}

    def before_insert(self):
        if hasattr(self, 'ctime') and self.ctime is None:
            self.ctime = datetime.now()

        if hasattr(self, 'mtime'):
            self.mtime = datetime.now()

    def before_update(self):
        if hasattr(self, 'mtime'):
            self.mtime = datetime.now()

Model = declarative_base(cls=Model, metaclass=MetaModel)
