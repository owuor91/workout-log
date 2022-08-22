import flask_bcrypt
from flask import request
from flask_restful import Resource

from app.users.schemas import UserSchema


class UserRegistration(Resource):
    def post(self):
        data = request.get_json()
        user_schema = UserSchema()
        errors = user_schema.validate(data)
        if errors:
            return {"error": True, "errors": str(errors)}, 400

        user = user_schema.load(data)
        user.password = flask_bcrypt.generate_password_hash(user.password)
        try:
            user.save()
            schema = UserSchema(exclude=["password"])
            return {
                "message": "registration, successful",
                "user": schema.dump(user),
            }, 201
        except Exception as e:
            return {"error": e.args}, 500
