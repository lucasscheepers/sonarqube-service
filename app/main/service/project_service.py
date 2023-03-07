import json
from ..config import CONFIG

import requests
from ..model.project import Project, ProjectEncoder


def search_projects(query):
    # TODO: ORGANIZATION PARAMETER IS ONLY FOR SONARCLOUD.IO, SO THIS HAS TO BE DELETED
    # TODO: TRY MULTIPLE SCENARIOS FOR ERROR HANDLING
    params = {'organization': 'lucasscheepers', 'q': query}

    url = f'{CONFIG.SONARQUBE_API}/projects/search'
    response_json = requests.get(url, params=params, auth=(f'{CONFIG.SONARQUBE_TOKEN}', '')).json()

    projects = []
    for i in response_json['components']:
        project = Project(i['key'], i['name'])
        projects.append(project)

    return json.dumps(projects, indent=4, cls=ProjectEncoder)


def import_project(alm_key, gitlab_project_id):
    return f"ALM key: {alm_key} & gitlab project id: {gitlab_project_id}"


# def set_project_binding(alm_key, project_key, monorepo, gitlab_project_id):
#     return f"ALM key: {alm_key} & sonarqube project key: {project_key} & monorepo: {monorepo} " \
#            f"& gitlab project id: {gitlab_project_id}"
