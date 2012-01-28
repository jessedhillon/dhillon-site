from datetime import date, datetime
from dateutil.tz import tzutc
from uuid import uuid4 as uuid

from sqlalchemy.types import TypeDecorator, DateTime, String

class UTCDateTime(TypeDecorator):
    impl = DateTime

    def process_bind_param(self, value, engine):
        if value is not None:
            if value.tzinfo is None:
                # TODO: do we want to assume that unqualified datetimes are UTC?
                return value.replace(tzinfo=tzutc())
            else:
                return value.astimezone(tzutc())

    def process_result_value(self, value, engine):
        if value is not None:
            return datetime(value.year, value.month, value.day,
                                        value.hour, value.minute, value.second,
                                        value.microsecond, tzinfo=tzutc())

class UUID(TypeDecorator):
    impl = String

    def __init__(self):
        self.impl.length = 32
        TypeDecorator.__init__(self, length=self.impl.length)

    def process_bind_param(self, value, dialect=None):
        if value and type(value) is uuid.UUID:
            return value.hex

        elif value and type(value) is not uuid.UUID:
            raise ValueError("value {0} is not a valid UUID".format(value))

        else:
            return uuid().hex

    def process_result_value(self,value,dialect=None):
        if value:
            return uuid.UUID(hex=value)

        else:
            return None

    def is_mutable(self):
        return False
