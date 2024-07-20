
# Установка и настройка Flask

## Структура папок
```
my_flask_api/
│
├── app.py # основной файл программы
├── models.py # модели базы данных
├── resources.py # пути ресурсов API
├── database.db # файл базы данных SQLite
└── README-ru.md # документация проекта
```

### Сначала убедитесь, что Flask установлен:

```
pip install Flask Flask-SQLAlchemy Flask-HTTPAuth
```


### Инициализируйте базу данных:

```
from app import db
db.create_all()
```
### Запустите приложение Flask:
```
python app.py
```

### Доступ к API:
```
Маршрут Index: http://127.0.0.1:5000/
```
```
Маршрут Items: http://127.0.0.1:5000/api/items/
```

## Использование:

#### GET /api/items/: Получить все элементы.
#### GET /api/items/<id>: Получить определенный элемент по ID.
#### POST /api/items/: Создать новый элемент. Пример тела JSON:
```
{
  "name": "New Item",
  "description": "This is a new item."
}

```
#### PUT /api/items/<id>: Обновить существующий элемент по ID. Пример тела JSON:
```
{
  "name": "Updated Item",
  "description": "This is an updated item."
}

````
#### DELETE /api/items/<id>: Удалить элемент по ID.

## Аутентификация

#### Этот API использует базовую аутентификацию. Используйте следующие учетные данные для доступа к конечным точкам:

```
Имя пользователя: admin
Пароль: password123

```

## Обработка ошибок

API включает обработку ошибок для распространенных проблем:

#### 404 Not Found: Возвращается, когда ресурс не найден.
#### 400 Bad Request: Возвращается, когда запрос некорректен.
#### 500 Internal Server Error: Возвращается, когда происходит неожиданная ошибка.

<img src='https://keyper.dbsentry.com/post/rest-api-using-python-flask/featured.png'>

# Лицензия
#### Этот проект распространяется под лицензией MIT.
#### Этот пример предоставляет комплексную настройку для RESTful API с использованием Flask.


