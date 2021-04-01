from flask import Blueprint
from flask_restful import Api

from apps.api.views import HealthCheckView

api_bp = Blueprint("api", __name__)
api = Api(api_bp)

# Route
api.add_resource(HealthCheckView, "/health_check", endpoint="health_check")
