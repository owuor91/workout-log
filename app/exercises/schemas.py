from marshmallow import Schema, fields


class ExerciseCategorySchema(Schema):
    category_id = fields.UUID(dump_only=True)
    category_name = fields.String(required=True)

class ExerciseSchema(Schema):
    exercise_id = fields.UUID(dump_only=True)
    exercise_name = fields.String(required=True)
    image = fields.String()
    category_id = fields.UUID(required=True)
    description = fields.String()