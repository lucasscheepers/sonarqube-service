from json import JSONEncoder


class Project:
    def __init__(self, project_key, project_name):
        self.project_key = project_key
        self.project_name = project_name


class ProjectEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
