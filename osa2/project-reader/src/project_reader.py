from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url
    
    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        # print(content)
        with open('pyproject.toml', 'r') as f:
            config = toml.load(f)

        name = config.get('tool', {}).get('poetry', {}).get('name', 'Unnamed project')
        description = config.get('tool', {}).get('poetry', {}).get('description', 'No description')
        licenses = config.get('tool', {}).get('poetry', {}).get('license', 'no license')

        authors = config.get('tool', {}).get('poetry', {}).get('authors', {})
        dependencies = config.get('tool', {}).get('poetry', {}).get('dependencies', {})
        group_dev_dependencies = config.get('tool', {}).get('poetry', {}).get('group', {}).get('dev', {}).get('dependencies', {})

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, licenses, authors, dependencies, group_dev_dependencies)