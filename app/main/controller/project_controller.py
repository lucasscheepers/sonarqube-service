from ..service import project_service

from flask import Blueprint, request
from flasgger import swag_from

project_controller = Blueprint('Project Controller', __name__)


@project_controller.route("/alm/<string:alm_key>/projects/", methods=['GET'])
@swag_from('../docs/project_controller.yml')
def list_projects(alm_key):
    """ returns a list of all projects or projects that matches the search input if specified  """
    search_input = request.args.get('search_input', type=str)

    if search_input is None:
        return project_service.list_projects(alm_key)
    else:
        return project_service.search_projects(alm_key, search_input)


@project_controller.route("/alm/<string:alm_key>/projects/", methods=['POST'])
@swag_from('../docs/project_controller.yml')
def import_project(alm_key):
    """ imports a gitlab project into sonarqube """
    content = request.json

    return project_service.import_project(alm_key, content['gitlab_project_id'])


# @project_controller.route("/alm/<string:alm_key>/projects/<string:project_key>", methods=['PUT'])
# def set_project_binding(alm_key, project_key):
#     """ binds a gitlab project to a sonarqube project """
#     content = request.json
#
#     return project_service.set_project_binding(alm_key, project_key, content['monorepo'], content['gitlab_project_id'])
