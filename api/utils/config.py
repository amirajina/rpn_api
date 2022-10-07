import os
from flask.config import Config


def get_config_file_path():
    return os.path.abspath(os.path.join(
        os.path.dirname(__file__), '..', 'conf', 'app_conf.py'))


def load_config():
    cfg = Config('')
    cfg.from_pyfile(get_config_file_path())
    return cfg
