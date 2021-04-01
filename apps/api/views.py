from apps.base.views import BaseView
from utility.utility import StatusCode as status


class HealthCheckView(BaseView):
    def get(self):
        return self.render_json_response(status_code=status.HTTP_200_OK, res="OK")


class ExercisesView(BaseView):

    # TODO: Add exercise here or in other blueprints
    pass
