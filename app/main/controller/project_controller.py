from ..service import project_service
from app.main.config import CONFIG

from flask import Blueprint, request
from flasgger import swag_from

project_controller = Blueprint('Project Controller', __name__, url_prefix=f'/{CONFIG.VERSION}')


@project_controller.route('/projects/', methods=['GET'])
@swag_from('../docs/project_controller_list_projects.yml')
def search_projects():
    """ Returns a list of projects with the possibility to filter that list  """
    query = request.args.get('query', type=str)

    return project_service.search_projects(query)


@project_controller.route('/alm/<string:almKey>/projects/', methods=['POST'])
@swag_from('../docs/project_controller_import_project.yml')
def import_project(almKey):
    """ Imports a GitLab project into SonarQube """
    alm_key = almKey
    content = request.json

    return project_service.import_project(alm_key, content['gitlabProjectId'])
