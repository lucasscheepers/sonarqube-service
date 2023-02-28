from flask import Flask
from flasgger import Swagger
from main.controller.project_controller import project_controller
from main.config import config_by_name


def create_api(config):
    _api = Flask(__name__)
    _api.register_blueprint(project_controller)
    _api.config.from_object(config_by_name[config])
    Swagger(_api)

    return _api


api = create_api('dev')

# TODO: ADD LOGGING & SWAGGER


@api.route("/", methods=['GET'])
def hello_world():
    """ Hello World  """
    return "Hello World"


if __name__ == '__main__':
    api.run()
