from marshmallow import fields, Schema
from marshmallow_enum import EnumField

from app.base.enums import SexEnum


class UserSchema(Schema):
    user_id = fields.UUID(dump_only=True)
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.Email(required=True)
    phone_number = fields.String(required=True)
    password = fields.String(required=True)


class ProfileSchema(Schema):
    profile_id = fields.UUID(dump_only=True)
    user_id = fields.UUID(required=True)
    sex = EnumField(SexEnum, required=True)
    date_of_birth = fields.Date(required=True)
    weight = fields.Float(required=True)
    height = fields.Integer(required=True)
