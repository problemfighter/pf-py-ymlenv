import os
import yaml
# from pf_py_common.pf_exception import PFException
from pf_py_ymlenv.pfpy_config_obj import PFPYConfigObj
from pf_py_ymlenv.pfpy_file_util import PFPYFileUtil


class PFPYConfigLoader:
    default_env_file_name = "env.yml"
    project_root_path: str
    config_obj: PFPYConfigObj = None
    env_file: str = None
    raise_error_if_not_found: bool = False

    def load(self,
             env_file: str = None,
             config_obj: PFPYConfigObj = None,
             project_root_path: str = PFPYFileUtil.PROJECT_ROOT_DIR,
             raise_error_if_not_found: bool = False, ):
        self.project_root_path = project_root_path
        self.config_obj = config_obj
        self.env_file = env_file
        self.raise_error_if_not_found = raise_error_if_not_found
        yaml_dict = self._load_yaml()
        if not yaml_dict and config_obj:
            return config_obj
        elif yaml_dict and config_obj and isinstance(config_obj, PFPYConfigObj):
            return self._map_to_config_object(yaml_dict)
        return yaml_dict

    def _load_yaml(self):
        env_file = self._get_env_file(self.env_file)
        self._raise_exception(env_file, "YAML file not found!")
        if not env_file:
            return None
        try:
            stream = open(env_file, 'r')
            yaml_content = stream.read()
            return yaml.full_load(yaml_content)
        except Exception as e:
            self._raise_exception(env_file, str(e))
        return None

    def _map_to_config_object(self, yaml_dict: dict):
        for dict_key in yaml_dict:
            setattr(self.config_obj, dict_key, yaml_dict[dict_key])
        return self.config_obj

    def _get_env_file(self, env_file: str = None):
        if not env_file:
            env_file_name = self._get_config_file_name()
            env_file = PFPYFileUtil.concat_path(self.project_root_path, env_file_name)
        if PFPYFileUtil.is_exists_path(env_file):
            return env_file
        return None

    def _get_config_file_name(self):
        env = os.environ.get('env')
        if env:
            return "env-" + env + ".yml"
        return self.default_env_file_name

    def _raise_exception(self, value, message="Value Not Found"):
        if not value and self.raise_error_if_not_found:
            pass
            # raise PFException(message)
        return value


yaml_env = PFPYConfigLoader()
