from marshmallow import fields

from src.balance.domain.balance import Balance
from src.kernel.schemas.dataclass_schema import DataclassSchema


class BalanceSchema(DataclassSchema):
    __model__ = Balance

    cycle_group = fields.Integer(data_key="CYCLE_GROUP")
    year = fields.Integer(data_key="YEAR")
    month = fields.Integer(data_key="MONTH")
    cycle_date = fields.Date(data_key="CYCLE_DATE")
    payment_due_date = fields.Date(data_key="PAYMENT_DUE_DATE")
    deliquency_date = fields.Date(data_key="DELIQUENCY_DATE")
