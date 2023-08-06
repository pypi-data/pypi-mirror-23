Python JSON Logging In File
===========================

Данная библиотека позволяет легко и безболезненно логировать ваши
метрики в файл, чтобы потом скормить Ваш лог Kibana.

Коротенькая инструкция
----------------------

Установка
~~~~~~~~~

::

    sudo pip3 install -r requirements.txt


Код
~~~

::

    from json_logger import CustomJsonLogger

    logger = CustomJsonLogger(__name__)

    logger.error("oshibka",params={"email":"mojkot@mail.ru"})

Результат
~~~~~~~~~

::

    {"message": "oshibka", "email": "mojkot@mail.ru", "level": "ERROR", "time": "2017-05-16T11:17:11.731508", "log_id": "0b2c5904-dad5-4b3b-9f1e-40b5fc5c96b9"}


