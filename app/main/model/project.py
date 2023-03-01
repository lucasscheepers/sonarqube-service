import json


class Project:
    def __init__(self, project_key, project_name):
        self.project_key = project_key
        self.project_name = project_name


class ProjectEncoder(json.JSONEncoder):
    def default(self, obj):
        return [obj.x, obj.y]
