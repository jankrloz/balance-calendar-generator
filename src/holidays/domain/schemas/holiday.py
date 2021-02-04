from marshmallow import fields

from src.holidays.domain.holiday import Holiday
from src.kernel.schemas.dataclass_schema import DataclassSchema


class HolidaySchema(DataclassSchema):
    __model__ = Holiday

    holiday_id = fields.Integer(required=True, data_key="HOLIDAY_ID")
    country_code = fields.String(required=True, data_key="COUNTRY_CODE")
    date = fields.Date(required=True, data_key="DATE")
    description = fields.String(required=True, data_key="DESCRIPTION")
