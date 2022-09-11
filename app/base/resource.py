from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from app.base.models import save, get, set_model_dict


class BaseResource(Resource):
    schema = None
    model = None

    @jwt_required()
    def post(self):
        data = request.get_json()

        errors = self.schema.validate(data)
        if errors:
            return {"error": True, "errors": str(errors)}, 400

        item = self.model(**data)
        try:
            save(item)
            return self.schema.dump(item), 201
        except Exception as e:
            return {"error": e.args}, 500

    @jwt_required()
    def get(self, pk=None):
        item = get(self.model, pk)
        if item is not None:
            if pk:
                return self.schema.dump(item), 200
            return self.schema.dump(item, many=True), 200
        return {"error": f"{self.model.__class__} not found"}, 404

    @jwt_required()
    def put(self, pk):
        item = get(self.model, pk)
        if item is not None:
            data = request.get_json()
            item = set_model_dict(item, data)
            try:
                save(item)
                return self.schema.dump(item), 200
            except Exception as e:
                return {"error": e.args}, 500
        return {"error": f"{self.model.__class__} not found"}, 404
