# Тестовое задание IS-ART

## Запуск:

    sudo docker-compose up

## Модели базы данных

[models](https://github.com/Jumas-Cola/test_task_isart2/blob/main/isart2/shop/models.py)

## Аккаунт администратора

Логин: admin  
Пароль: admin

## Страницы

- / - корень api
- /html/ - список продуктов
- /html/orders.html - список заказов
- /html/registration.html - страница регистрации
- /html/auth.html - страница авторизации
- /admin/ - админка Django

## Технологии

- Фреймворк Django 3.2
- Django REST framework - для создания API
- Модули:
    - django-filter - модуль фильтрации данных
    - django-rest-registration - модуль регистрации
    - django-seed - модуль заполнения базы фейковыми данными

## Окружение

Для маршрутизации запросов в директорию со статическими файлами и в Django приложение 
используется NGINX.

## API

Регистрация (POST):

    curl --data '{"password": "username123", \
                  "username": "user", \
                  "first_name": "Вася", \
                  "last_name": "Пупкин", \
                  "email": "user@mail.ru", \
                  "password_confirm": "username123"}' \
    --header "Content-Type: application/json" \
    http://127.0.0.1/accounts/register/

Авторизация (POST):

    curl --data "username=admin&password=admin" http://127.0.0.1/api-token-auth/

Список пользователей (GET) [Auth Admin]:

    curl -X GET "http://127.0.0.1/users/?format=json" \
    -H 'Authorization: Token a292f188f66bba1922092af0c7895183caea439f'

Список групп (GET) [Auth Admin]:

    curl -X GET "http://127.0.0.1/groups/?format=json" \
    -H 'Authorization: Token a292f188f66bba1922092af0c7895183caea439f'

Список заказов авторизованного пользователя (GET) [Auth]:

    curl -X GET "http://127.0.0.1/orders/?format=json" \
    -H 'Authorization: Token a292f188f66bba1922092af0c7895183caea439f'

Создать заказ (POST) [Auth]:

    curl -X POST "http://127.0.0.1/orders/?format=json" \
    -d "product=1" \
    -H 'Authorization: Token f55824f0972eba00e97d8035d10f17f75d65d1c2'

Список категорий (GET):

    curl -X GET "http://127.0.0.1/categories/?format=json"

Список подкатегорий (GET):

    curl -X GET "http://127.0.0.1/subcategories/?format=json"

Список продуктов (GET):

    curl -X GET "http://127.0.0.1/products/?format=json"

Get параметры страницы продуктов:

    page=2 - пагинация
    category=1 - категория
    subcategory=5 - подкатегория
    ordering=name|-name|price|-price|count|-count - сортировка
    min_price=1 - минимальная цена
    max_price=2800 - максимальная цена
    min_count=3 - минимальное количество
    search=space - поисковый запрос

