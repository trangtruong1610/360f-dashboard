import json


class GoogleSearchController:

    def on_post(self, req, resp):
        r = {
            'TODO': 'run pytest and show result here',
        }
        resp.body = json.dumps(r, sort_keys=False)

