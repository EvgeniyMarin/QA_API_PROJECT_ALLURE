import datetime                                          # библиотека для фиксации времени и даты
import os



class Logger():
    file_name = f"logs/log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"               # сохраняем в переменную название нашего файла, который будет храниться в папке logs и начинаться на log(logs/log_) (".log" это расширение создаваемого файла)


    """Метод для открытия файла и записи в него данных"""

    @classmethod                                                                     # это означается, что метод write_log_to_file МОЖЕТ ОБРАЩАТЬСЯ к переменным шанего класса (class Logger():)
    def write_log_to_file(cls, data: str):                                           # для этого в методе нужно писать не self, а cls  (data: str это означает, что мы будем помещать наши данные в виде строки)
        with open(cls.file_name, 'a', encoding='utf=8') as logger_file:              # open (открываем файл), cls.file_name (обращаемя к переменной класса(так как переменная хранит файл, это как тут внутри своздается файл(file_write_name_character = open('/DOC/name_character.txt', 'a', encoding='utf-8') только тут приваиваение пременной происходит через "AS" а не через "=" )),
            logger_file.write(data)                                                  # записываем данные в файл (значение которого присвоили logger_file (с помощью 'AS' а не '=')



    """Метод для получения данных по запросу (по "request")"""

    @classmethod
    def add_request(cls, url: str, method: str):                    # (url: str) это мы помещаем url в наш метод, (method: str) это мы помещаем название нашего метода(GET, POST и тд) в наш метод add_request
        test_name = os.environ.get('PYTEST_CURRENT_TEST')           # с помощью этой пременной мы будем помещать название теста, который в данный момент выполняется

        data_to_add = f"\n-----\n"                                  # эта строка нужна чтобы разделять логи ("\n" это пернос с одной строки на другую)
        data_to_add += f"Test: {test_name}\n"                       # название теста
        data_to_add += f"Time: {str(datetime.datetime.now())}\n"    # время
        data_to_add += f"Request method: {method}\n"                # название метода
        data_to_add += f"Request URL: {url}\n"                      # наш url
        data_to_add += "\n"                                         # чистой строки

        cls.write_log_to_file(data_to_add)                          # обращаемя к нашему классу и методу "write_log_to_file" (он вызовет метод write_log_to_file, который создаст, откроет файл и запишет в него данные ((logger_file.write(data) это запись где data это data_to_add из метода add_request)


    """Метод для получения данных по ОТВЕТУ (по "response")"""

    @classmethod
    def add_response(cls, result):
        cookies_as_dict = dict(result.cookies)                       # обращаемся к нашим кукам (чтобы получить их )
        headers_as_dict = dict(result.headers)                       # обращаемся к нашим заголовкам (чтобы получить их )

        data_to_add = f"Response code: {result.status_code}\n"       # статус код
        data_to_add += f"Response text: {result.text}\n"             # результат запроса (в виде текста)
        data_to_add += f"Response headers: {headers_as_dict}\n"      # заголовки
        data_to_add += f"Response cookies: {cookies_as_dict}\n"      # куки
        data_to_add += f"\n-----\n"

        cls.write_log_to_file(data_to_add)