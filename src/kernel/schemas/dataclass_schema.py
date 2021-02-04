from marshmallow import Schema
from marshmallow.decorators import post_load


class DataclassSchema(Schema):
    @post_load
    def make_object(self, data, **kwargs):
        return self.__model__(**data)
