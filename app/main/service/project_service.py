def search_projects(alm_key, query):
    return f"ALM key: {alm_key} & query: {query}"


def import_project(alm_key, gitlab_project_id):
    return f"ALM key: {alm_key} & gitlab project id: {gitlab_project_id}"


def set_project_binding(alm_key, project_key, monorepo, gitlab_project_id):
    return f"ALM key: {alm_key} & sonarqube project key: {project_key} & monorepo: {monorepo} " \
           f"& gitlab project id: {gitlab_project_id}"

