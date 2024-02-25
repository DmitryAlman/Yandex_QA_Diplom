import requests
import config
import data

def create_new_order(body):
    return requests.post(config.URL_SERVICE + config.CREATE_ORDER_PATH, json=body)

def get_order_track():
    answer = create_new_order(data.order_body)
    return answer.json()["track"]

def get_order(track):
    return requests.get(config.URL_SERVICE + config.GET_ORDER_PATH + str(track))
