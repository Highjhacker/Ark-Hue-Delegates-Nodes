import requests
import configparser


def get_delegate_blocks_activity():
    delegate_name = get_from_config("delegate_name")
    host = get_from_config("forging_node_host")
    return requests.get(f"{host}{delegate_name}").json()["data"]["blocks"]["missed"]


def get_from_config(key):
    config = configparser.ConfigParser()
    config.read('philips.conf')
    return config['DEFAULT'][key]
