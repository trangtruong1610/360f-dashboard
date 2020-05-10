import falcon

from src.controller.google_search import GoogleSearchController
from src.controller.health import HealthResource


api = falcon.API()

api.add_route('/health', HealthResource)
api.add_route('/google_search', GoogleSearchController)
