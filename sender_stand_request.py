import configuration
import requests
import data


# Шаг 1: Запрос на создание заказа
def post_new_order (body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки

response = post_new_order (data.order_body)
print(response.status_code)

# Шаг 2: Получение заказа по номеру
def get_order_by_track(order_number):
    return requests.get(configuration.URL_SERVICE + configuration.POST_ORDER_PATH + str(order_number),
                        headers=data.headers)