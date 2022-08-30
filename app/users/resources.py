import datetime

import flask_bcrypt
from flask import request
from flask_jwt_extended import create_access_token, jwt_required
from flask_restful import Resource

from app.base.exceptions import BadRequest
from app.base.models import save, get, set_model_dict
from app.users.model import User, Profile
from app.users.schemas import UserSchema, ProfileSchema
from db import db


class UserRegistration(Resource):
    def post(self):
        data = request.get_json()
        user_schema = UserSchema()
        errors = user_schema.validate(data)
        if errors:
            return {"error": True, "errors": str(errors)}, 400

        user = User(**data)
        if self.validate_existing_email(user.email):
            error = BadRequest(f"email {user.email} already exists")
            return {"error": str(error)}, error.status_code
        if self.validate_existing_phone(user.phone_number):
            error = BadRequest(
                f"phone_number {user.phone_number} already exists"
            )
            return {"error": str(error)}, error.status_code
        user.password = flask_bcrypt.generate_password_hash(
            user.password
        ).decode("utf-8")
        try:
            save(user)
            schema = UserSchema(exclude=["password"])
            return {
                "message": "registration, successful",
                "user": schema.dump(user),
            }, 201
        except Exception as e:
            return {"error": e.args}, 500

    def validate_existing_email(self, email):
        return bool(db.session.query(User).filter(User.email == email).first())

    def validate_existing_phone(self, phone_number):
        return bool(
            db.session.query(User)
            .filter(User.phone_number == phone_number)
            .first()
        )


class UserLogin(Resource):
    def post(self):
        try:
            data = request.get_json()
            email = data["email"]
            password = data["password"]
            user = db.session.query(User).filter(User.email == email).first()
            profile = db.session.query(Profile).filter(
                Profile.user_id==user.user_id).first()
            if user is not None and flask_bcrypt.check_password_hash(
                user.password, password
            ):
                access_token = create_access_token(
                    user.user_id,
                    expires_delta=datetime.timedelta(seconds=86400),
                )

                response = {
                    "message": "login successful",
                    "access_token": access_token,
                    "user_id": str(user.user_id),
                }
                if profile is not None:
                    response["profile_id"] = str(profile.profile_id)
                return response, 200
            else:
                return {"error": "invalid credentials"}, 401
        except Exception as e:
            return {"error": str(e)}, 500


class ProfileResource(Resource):
    schema = ProfileSchema()

    @jwt_required()
    def post(self):
        data = request.get_json()

        errors = self.schema.validate(data)
        if errors:
            return {"error": True, "errors": str(errors)}, 400

        profile = Profile(**data)

        try:
            save(profile)
            return self.schema.dump(profile), 201
        except Exception as e:
            return {"error": e.args}, 500

    @jwt_required()
    def get(self, pk):
        profile = get(Profile, pk)
        if profile is not None:
            return self.schema.dump(profile), 200
        return {"error": "profile not found"}, 404

    @jwt_required()
    def put(self, pk):
        profile = get(Profile, pk)
        if profile is not None:
            data = request.get_json()
            profile = set_model_dict(profile, data)
            try:
                save(profile)
                return self.schema.dump(profile), 200
            except Exception as e:
                return {"error": e.args}, 500
        return {"error": "profile not found"}, 404
