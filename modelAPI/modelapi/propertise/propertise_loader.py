import yaml
import os
import sys
from copy import deepcopy

class PropertiseLoader:
    __propertise: dict = None

    def __init__(self):
        self.__load_propertise_file()

    def __load_propertise_file(self):
        if self.__propertise is None:
            project_path = os.path.dirname(sys.argv[0])
            propertise_path = project_path + "/../propertise.yaml"
            with open(propertise_path) as f:
                self.__propertise = yaml.full_load(f)

    def get(self):
        return deepcopy(self.__propertise)

if __name__ == "__main__":
    raise NotImplemented