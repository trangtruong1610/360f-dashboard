import falcon

from src.controller.google_search import GoogleSearchController
from src.controller.health import HealthController


api = falcon.API()

api.add_route('/health', HealthController())
api.add_route('/google_search', GoogleSearchController())
