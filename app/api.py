from main.controller.project_controller import project_controller
from main.config import config_by_name, VERSION

from flask import Flask, jsonify
from flasgger import Swagger


def create_api(config):
    _api = Flask(__name__)
    _api.register_blueprint(project_controller)
    _api.config.from_object(config_by_name[config])
    Swagger(_api, config={
        'title': 'Sonarqube Automation API',
        'version': f'{VERSION}',
        'description': 'This service is written to automate the creation of Sonarqube projects '
                       'based on the Gitlab projects',
        'termsOfService': None,
        'specs_route': f'/{VERSION}/apidocs/'

    }, merge=True, template_file='main/docs/definitions.yml')

    return _api


api = create_api('dev')

# TODO: ADD LOGGING


@api.route('/v1', methods=['GET'])
def more_information():
    """ More information  """
    return jsonify(
        message="Go to API_URL/apidocs for more information about this API"
    )


if __name__ == '__main__':
    api.run()
