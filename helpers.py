import requests
import configparser


def get_delegate_blocks_activity():
    delegate_name = get_from_config("delegate_name")
    return requests.get(f"http://178.128.248.189:4003/api/v2/delegates/{delegate_name}").json()["data"]["blocks"]["missed"]


def get_from_config(key):
    config = configparser.ConfigParser()
    config.read('philips.conf')
    return config['DEFAULT'][key]
