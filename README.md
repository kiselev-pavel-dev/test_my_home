# Тестовое задание для компании Мой Дом Онлайн

# Запуск и работа с проектом
Чтобы развернуть проект, вам потребуется:
1) Клонировать репозиторий GitHub:
```python
git clone git@github.com:kiselev-pavel-dev/test_my_home.git
```
2) Перейти в папку с проектом
```python
cd test_my_home
```

3) Создать и активировать виртуальное окружение
```python
python -m venv venv
source venv/scripts/activate
```

4) Перейти в директорию с проектом
```python
cd my_home
```

5) Установить зависимости
```python
pip install -r requirements.txt
```

6) Собрать и выполнить миграции, создать суперпользователя
```python
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

Админка: _http://127.0.0.1:8000/admin/_

Для доступа к API необходимо создать токен, можно через админку.

Ендпоинт: _http://127.0.0.1:8000/api/entities/_ 



### <br /> Автор проекта:
Киселев Павел<br />
neznika2@mail.ru<br />
