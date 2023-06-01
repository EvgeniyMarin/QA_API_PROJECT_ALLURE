import allure
import  requests

from utils.logger import Logger

"""Список HTTP методов"""

class Http_methods:
    headers = {'Content-Type': 'application/json'}                                                   # все наши заголовни будут передаваться в формате json
    cookie = ''

    @staticmethod                                                                                    # делаем метод статическим чтобы вызывать в любом классе(тесте) без привязки к классу Http_methods
    def get(url):
        with allure.step('GET'):                                                                     # шаг allure и указываем, что он делает
            Logger.add_request(url, method='GET')                                                    # (это нужно чтобы фиксировать в логах результат запроса) вызываем метод add_request класса Logger ( из ФАЙЛА Logger.py) и передаем в него url и название метода
            result = requests.get(url, headers=Http_methods.headers, cookies=Http_methods.cookie)
            Logger.add_response(result)                                                              # (это нужно чтобы в логах фиксировать наш ответ)
            return result

    @staticmethod                                                                                    # делаем метод статическим чтобы вызывать в любом классе(тесте) без привязки к классу Http_methods
    def post(url, body):
        with allure.step('POST'):
            Logger.add_request(url, method='POST')                                                              # (это нужно чтобы фиксировать в логах результат запроса) вызываем метод add_request класса Logger ( из ФАЙЛА Logger.py) и передаем в него url и название метода
            result = requests.get(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            Logger.add_response(result)                                                                        # (это нужно чтобы в логах фиксировать наш ответ)
            return result

    @staticmethod                                                                                            # делаем метод статическим чтобы вызывать в любом классе(тесте) без привязки к классу Http_methods
    def put(url, body):
        with allure.step('PUT'):
            Logger.add_request(url, method='PUT')                                                     #(это нужно чтобы фиксировать в логах результат запроса) вызываем метод add_request класса Logger ( из ФАЙЛА Logger.py) и передаем в него url и название метода
            result = requests.put(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            Logger.add_response(result)                                                               # (это нужно чтобы в логах фиксировать наш ответ)
            return result

    @staticmethod                                                                                #(это нужно чтобы фиксировать в логах результат запроса) делаем метод статическим чтобы вызывать в любом классе(тесте) без привязки к классу Http_methods
    def delete(url, body):
        with allure.step('DELETE'):
            Logger.add_request(url, method='DELETE')                                                 # вызываем метод add_request класса Logger ( из ФАЙЛА Logger.py) и передаем в него url и название метода
            result = requests.delete(url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            Logger.add_response(result)                                                              # (это нужно чтобы в логах фиксировать наш ответ)
            return result

