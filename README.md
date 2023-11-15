## Описание проекта

* Python: 3.10.9
* Django: 4.2.7
* TinyDB: 4.8.0
* Файл БД: ./lidhit_test_task/db.json

## Запуск проекта

* Создаем директорию для проекта
* Переходим в нее
* Запусткаем клон с гитхаба: git clone https://github.com/amiddio/lidhit_test_task.git .
* Создаем виртуальное окружение: python -m venv venv
* Активируем его: venv\Scripts\activate
* Ставим зависимости: pip install -r lidhit_test_task/requirements.txt
* В директории ./lidhit_test_task создаем .env файл с перемеными окружения:
  * DEBUG=on
  * SECRET_KEY='some_key'
* Запускаем веб-сервер: python manage.py runserver

## Тестирование проекта

С корня проекта запускаем скрипты:
* python test_script1.py
* python test_script2.py
* python test_script3.py
* python test_script4.py

Запуск юниттестов:
* Переходим в директорию ./lidhit_test_task
* Запускаем: python manage.py test
