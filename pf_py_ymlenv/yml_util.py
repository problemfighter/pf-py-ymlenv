import yaml
from pf_py_ymlenv.pfpy_file_util import PFPYFileUtil


class YMLUtil:

    @staticmethod
    def load_from_file(path, default=None):
        if not PFPYFileUtil.is_exists_path(path):
            return default
        try:
            stream = open(path, 'r', encoding="utf-8")
            yaml_content = stream.read()
            return yaml.full_load(yaml_content)
        except Exception as e:
            return default

    @staticmethod
    def write_to_file(path, yaml_dict):
        PFPYFileUtil.delete_file(path)
        try:
            stream = open(path, 'w', encoding="utf-8")
            yaml_content = yaml.dump(yaml_dict, sort_keys=False)
            stream.write(yaml_content)
            stream.close()
            return True
        except Exception as e:
            return False
