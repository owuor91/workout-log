from app.base.resource import BaseResource
from app.exercises.model import ExerciseCategory, Exercise
from app.exercises.schemas import ExerciseCategorySchema, ExerciseSchema


class ExerciseCategoryResource(BaseResource):
    schema = ExerciseCategorySchema()
    model = ExerciseCategory


class ExerciseResource(BaseResource):
    schema = ExerciseSchema()
    model = Exercise
