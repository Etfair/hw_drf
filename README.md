Инструкция по запуску проекта:
Шаг 1. Клонирование репозитория

https://github.com/Etfair/hw_drf/tree/hw_4

Шаг 2. Установка зависимостей
1. Убедитесь, что в системе установлен Python3.x. Если нет, установите его в соответствии с инструкциями для вашей операционной системы.
2. Создайте виртуальное окружение

python3 -m venv venv

3. Активировать виртуальное окружение

source ./venv/Scripts/activate
venv/Scripts/activate.bat

4. Установить зависимости проекта, указанные в файле requirements.txt

pip install -r requirements.txt

Шаг 3. Установка и настройка Redis
1. Установить Redis, если он не установлен. Например, для Ubuntu выполнить следующую команду 

sudo apt-get install redis-service

2. Запустить Redis

sudo service redis-server start

Это запустит Redis сервер и он будет слушать на стандартном порту 6379
3. Убедиться что Redis работает правильно, командой

redis-cli ping

Если Redis работает должным образом, в ответ придёт PONG.

Шаг 4. Установка и настройка PostgreSQL
1. УСтановить PostgreSQL, если он не установлен. Например, для Ubuntu выполнить следующую команду

sudo apt-get install postgresql

2. Выполнить вход в интерактивную оболочку PostgreSQL от имени пользователя postgres

sudo -u postgres psql

3. Внутри интерактивной оболочки PostgreSQL создать базу данных с помощью следующей команды:

CREATE DATABASE name_db;

name_db - Название БД(можно указать другое название)

4. Закрыть интерактивную оболочку PostgreSQL

\q

Шаг 5. Настройка окружения
1. В директории проекта создать файл .env

touch .env

2. Открыть файл

nano .env

3. Записать в файл следующие настройки

DATABASES_DEFAULT_ENGINE=django.db.backends.postgresql_psycopg2
DATABASES_DEFAULT_NAME=name_db
DATABASES_DEFAULT_USER=имя_пользователя
DATABASES_DEFAULT_PASSWORD=пароль_пользователя
DATABASES_HOST=хост

EMAIL_HOST_USER=почта_для_аутентификации
EMAIL_HOST_PASSWORD=пароль

В каталоге проекта есть шаблон файла .env

Шаг 6. Применение миграций
1. Из каталога проекта выполнить команду

python manage.py migrate

Шаг 7. Запуск сервера Django
1. Открыть новое окно терминала
2. Если виртуальное окружение неактивно, активируйте его

source venv/Scripts/activate

3. Из каталога проекта запустить сервер

python manage.py runserver

Шаг 8. Для создания администратора запустить команду:

python3 manage.py ccsu

Шаг 9. Для запуска celery:

celery -A config worker --loglevel=info

Шаг 10. Для запуска django-celery-beat:

celery -A config beat -l info -S django

Шаг 11. Для запуска Docker:

Установите Docker desktop;
В терминале введите команду для создания контейнера:
docker compose build
и
docker compose up

Для применения миграция:
docker compose exec app python manage.py migrate
