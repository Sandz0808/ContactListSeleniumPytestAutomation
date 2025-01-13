import json
from pathlib import Path
import tomllib

def open_config():

    root_dir = Path(__file__).resolve().parent.parent
    config_path = root_dir / 'config/config.toml'

    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")


    with open(config_path, 'rb') as f:
        config = tomllib.load(f)
        return config


def user_sign_up_data():
    data = open_config()['jsonFile']['jsonPath']
    with open(data, 'r') as f:
        file = json.load(f)
        user = file['userSignUpTestData']
        return user


def user_login_data():
    data = open_config()['jsonFile']['jsonPath']
    with open(data, 'r') as f:
        file = json.load(f)
        user = file['userLoginTestData']
        return user

def user_update_data():
    data = open_config()['jsonFile']['jsonPath']
    with open(data, 'r') as f:
        file = json.load(f)
        user = file['UpdateData']
        return user


def get_current_url():
    url = open_config()['Website']['siteUrl']
    return url


def user_login_data1(user_data):
    data = open_config()['jsonFile']['jsonPath']
    with open(data, 'r') as f:
        file = json.load(f)
        user = file[user_data]
        return user

