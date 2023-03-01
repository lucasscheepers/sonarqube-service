from ..service import project_service
from app.main.config import VERSION

from flask import Blueprint, request
from flasgger import swag_from

project_controller = Blueprint('Project Controller', __name__, url_prefix=f'/{VERSION}')


@project_controller.route('/alm/<string:almKey>/projects/', methods=['GET'])
@swag_from('../docs/project_controller_list_projects.yml')
def search_projects(almKey):
    """ Returns a list of projects with the possibility to filter that list  """
    alm_key = almKey
    query = request.args.get('query', type=str)

    return project_service.search_projects(alm_key, query)


@project_controller.route('/alm/<string:almKey>/projects/', methods=['POST'])
# @swag_from('../docs/project_controller_list_projects.yml')
def import_project(almKey):
    """ Imports a GitLab project into SonarQube """
    alm_key = almKey
    content = request.json

    return project_service.import_project(alm_key, content['gitlab_project_id'])


# @project_controller.route("/alm/<string:alm_key>/projects/<string:project_key>", methods=['PUT'])
# def set_project_binding(alm_key, project_key):
#     """ binds a gitlab project to a sonarqube project """
#     content = request.json
#
#     return project_service.set_project_binding(alm_key, project_key, content['monorepo'], content['gitlab_project_id'])
