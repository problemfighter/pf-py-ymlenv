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
