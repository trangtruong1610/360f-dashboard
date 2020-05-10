import falcon


class HealthResource:

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_OK
