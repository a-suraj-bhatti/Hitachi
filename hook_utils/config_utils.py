import os
import yaml
class ConfigUtils:

    def __init__(self,pstr_current_path):
        self.current_path = pstr_current_path
        self.features_folder_path = self.get_features_folder_path()
        self.project_root_path = self.get_project_path()
        self.base_config = self.read_config_file()

    def read_config_file(self):
        try:
            with open(self.project_root_path + os.sep + "config.yml", "r") as config_options:
                config = yaml.safe_load(config_options)
            return config
        except Exception as e:
            raise Exception(e)


    def get_browser_name(self):
        try:
            browser = self.base_config["Browser"]
            return browser
        except Exception as e:
            raise Exception(e)


    def get_features_folder_path(self):
        try:
            return os.path.dirname(self.current_path)
        except Exception as e:
            raise Exception(e)

    def get_project_path(self):
        try:
            return os.path.dirname(self.features_folder_path)
        except Exception as e:
            raise Exception(e)

