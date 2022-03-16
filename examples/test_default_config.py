import os

from pf_py_ymlenv.pfpy_config_loader import yaml_env
from pf_py_ymlenv.pfpy_config_obj import PFPYConfigObj

if __name__ == '__main__':
    app_root = os.path.dirname(os.path.abspath(__file__))
    data = yaml_env.load(project_root_path=app_root, config_obj=PFPYConfigObj())
    print(data)
