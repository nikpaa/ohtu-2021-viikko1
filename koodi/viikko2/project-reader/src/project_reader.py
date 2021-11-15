from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        parsed_toml = toml.loads(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        poetry_toml = parsed_toml["tool"]["poetry"]

        name = poetry_toml["name"]
        desc = poetry_toml["description"]
        deps = poetry_toml["dependencies"]
        devdeps = poetry_toml["dev-dependencies"]

        return Project(name, desc, deps, devdeps)
