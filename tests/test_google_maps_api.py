import json

from requests import Response
import allure
from utils.api import Google_maps_api            # импортируем созданный модуль (api - название модуля, Google_maps_api - название класса)
from utils.checking import Checking

"""Создание, измение и удаление новой локации"""

# class Test_create_place():                             # можно было бы созданть класс, но тогда в функцию (метод) test_create_new_place() нужно было бы передавать self

@allure.epic('Test create place')                                       # теги (маркер) для allure
@allure.description('Test create, update, delete new place')            # теги (маркер) для allure
def test_create_new_place():


    print('Метод POST')
    result_post = Google_maps_api.create_new_place()                         # с помощью Google_maps_api.create_new_place обращаемся к методу create_new_place из класса Google_maps_api
                                                                              # эта переменная выведет все что  есть в методе create_new_place класса Google_maps_api, НО В СЕБЕ ХРАНИТ ТОЛЬКО РЕЗУЛЬТАТ ЗАПРОСА (result_post = Http_methods.post(post_url, json_for_create_new_place)) ИЗ ФАЙЛА API(МЕТОДА create_new_place)
    check_post = result_post.json()
    place_id = check_post.get('place_id')
    Checking.checking_status_code(result_post, 200)
    Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
    Checking.check_json_value(result_post, 'status', 'OK')

    """Это блок используется для получения списка с ключами json, который потом вставляется, как ожидаемый рузультат выше"""
    token = json.loads(result_post.text)                       # переменная содержит json (результат запроса POST в тексте)(
    print(list(token))                                         # преобразует json в список, получае в список ключи)


    print('Метод GET POST')
    result_get = Google_maps_api.get_new_place(place_id)        # эта переменная выведет все что  есть в методе get_new_place класса Google_maps_api, НО В СЕБЕ ХРАНИТ ТОЛЬКО РЕЗУЛЬТАТ ЗАПРОСА (result_get = Http_methods.get(get_url))) ИЗ ФАЙЛА API(МЕТОДА get_new_place   )
    Checking.checking_status_code(result_get, 200)
    Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
    Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')
    #     "address": "29, side layout, cohen 09"
    """Это блок используется для получения списка с ключами json, который потом вставляется, как ожидаемый рузультат выше"""
    token = json.loads(result_get.text)
    print(list(token))

    print('Метод PUT')
    result_put = Google_maps_api.put_new_place(place_id)
    Checking.checking_status_code(result_put, 200)
    Checking.check_json_token(result_put, ['msg'])             ######## вызываем метод для проверки наличия обязательных полей, ОЖИДАЕМЫЙ РЕЗУЛЬТАТ ставим в [] (это ключ) ТАК КАК ОЖИДАЕМЫЕ ЗНАЧЕНИЯ ЭТО КЛЮЧИ, КОТОРЫЕ ДОЛЖНЫ ХРАНИТЬСЯ В СПИСКЕ
    Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

    print('Метод GET PUT')
    result_get = Google_maps_api.get_new_place(place_id)
    Checking.checking_status_code(result_get, 200)
    Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website','language'])
    Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')

    print('Метод DELETE')
    result_delete = Google_maps_api.delete_new_place(place_id)
    Checking.checking_status_code(result_delete, 200)
    Checking.check_json_token(result_delete, ['status'])
    Checking.check_json_value(result_delete, 'status', 'OK')

    # print('Метод DELETE')                                   # мой способ, сначала создается экземпляр класс, а потом к нему применяется метод delete_new_place(place_id) с передачей в него place_id
    # result_delete = Google_maps_api()
    # result_delete.delete_new_place(place_id)

    print('Метод GET DELETE')
    result_get = Google_maps_api.get_new_place(place_id)
    Checking.checking_status_code(result_get, 404)
    Checking.check_json_token(result_get, ['msg'])
    Checking.check_json_search_word_in_value(result_get, 'msg', 'failed')           # метод для поиска слова

    print('Тестирование создания, изменение и удаления новой локации прошло успешно!')