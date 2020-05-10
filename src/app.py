import falcon

from src.controller.google_search import GoogleSearchController


api = falcon.API()
api.add_route('/google_search', GoogleSearchController)
