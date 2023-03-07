from dotenv import load_dotenv
load_dotenv()

from main.controller.project_controller import project_controller
from main.config import CONFIG

from flask import Flask, jsonify
from flasgger import Swagger
from logging.config import dictConfig
import logging


def setup_api():
    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://flask.logging.wsgi_errors_stream',
            'formatter': 'default'
        }},
        'root': {
            'level': CONFIG.LOGGING_LEVEL,
            'handlers': ['wsgi']
        }
    })

    _api = Flask(__name__)
    _api.register_blueprint(project_controller)
    _api.config.from_object(CONFIG)
    Swagger(_api, config={
        'title': 'Sonarqube Automation API',
        'version': f'{CONFIG.VERSION}',
        'description': 'This service is written to automate the creation of Sonarqube projects '
                       'based on the Gitlab projects',
        'termsOfService': None,
        'specs_route': f'/{CONFIG.VERSION}/apidocs/'

    }, merge=True, template_file='main/docs/definitions.yml')

    return _api


api = setup_api()


# TODO: ADD LOGS & ERROR HANDLING


@api.route('/v1', methods=['GET'])
def more_information():
    """ More information  """
    return jsonify(
        message="Go to API_URL/apidocs for more information about this API"
    )


if __name__ == '__main__':
    logging.info('Starting the API')
    api.run()
