from logging import DEBUG, StreamHandler, getLogger

from flask import Response, render_template
from flask_restful import Resource

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False


class BaseView(Resource):
    def __init__(self):
        pass

    def render_json_response(self, status_code: int = 200, res: str = "", **kwargs):
        response = {"res": res} if res else dict()
        response.update(kwargs)
        return response, status_code

    def render_template_response(self, template_name: str, mimetype: str = "text/html", **context) -> Response:
        return Response(render_template(template_name, mimetype=mimetype, **context))

    def render_content(self, content: str, status_code):
        return content, status_code
