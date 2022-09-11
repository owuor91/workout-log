from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api

from app.exercises.resources import ExerciseCategoryResource, ExerciseResource
from app.users.resources import UserRegistration, UserLogin, ProfileResource
from db import db


def create_app():
    app = Flask(__name__)
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = "postgresql+psycopg2:///workout_log"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = "xQUwFkHeHWcP6BVE"
    api = Api(app)
    jwt = JWTManager(app)

    db.init_app(app)
    with app.app_context():
        db.create_all()

    api.add_resource(UserRegistration, "/register")
    api.add_resource(UserLogin, "/login")
    api.add_resource(ProfileResource, "/profile", "/profile/<uuid:pk>")
    api.add_resource(
        ExerciseCategoryResource,
        "/exercise-categories",
        "/exercise-categories/<uuid:pk>",
    )
    api.add_resource(
        ExerciseResource,
        "/exercises",
        "/exercises/<uuid:pk>",
    )

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
