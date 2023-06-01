import json

import requests
"""Методы для проверки ответов запросов"""

class Checking():

    """Метод для проверки статус кода"""
    @staticmethod
    def checking_status_code(result, status_code):
        assert status_code == result.status_code
        print("Успешно!!! Статус код = " + str(result.status_code))

    """Метод для проверки наличия обязательных полей в ответе запроса"""

    @staticmethod
    def check_json_token(result, expected_value):                    #expected_value наш ожидаемый результат при вызове метода указываем его в тесте руками(берем из документации)
        token = json.loads(result.text)
        assert list(token) == expected_value
        print('Все поля присутствуют')

    """Метод для проверки наличия обязательных полей в ответе запроса"""

    @staticmethod
    def check_json_value(result, field_name, expected_value):        # где field_name название поля которое будем проверять(берем его из документации) (#expected_value наш ожидаемый результат при вызове метода указываем его в тесте руками(берем из документации))
        check = result.json()
        check_info = check.get(field_name)
        assert  check_info == expected_value
        print(field_name + ' верен!')

    """Метод для проверки наличия обязательных полей в ответе запроса ПО ЗАДННОМУ СЛОВУ"""
    @staticmethod
    def check_json_search_word_in_value(result, field_name, search_word):              # search_word слово, которое будем искать
        check = result.json()
        check_info = check.get(field_name)
        assert search_word in check_info
        print(f'Слово {search_word} присутствует!!!')