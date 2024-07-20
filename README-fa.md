
# راه‌اندازی و نصب Flask

## ساختار پوشه‌ها
```
my_flask_api/
│
├── app.py # فایل اصلی برنامه
├── models.py # مدل‌های پایگاه داده
├── resources.py # مسیرهای منابع API
├── database.db # فایل پایگاه داده SQLite
└── README-eng.md # مستندات پروژه

```

### ابتدا اطمینان حاصل کنید که Flask نصب شده است:

```
pip install Flask Flask-SQLAlchemy Flask-HTTPAuth
```


### پایگاه داده را مقداردهی اولیه کنید:

```
from app import db
db.create_all()
```
### برنامه Flask را اجرا کنید:
```
python app.py
```

### دسترسی به API:
```
Index route: http://127.0.0.1:5000/
```
```
Items route: http://127.0.0.1:5000/api/items/
```

## استفاده:

#### GET /api/items/: دریافت تمامی آیتم‌ها.
#### GET /api/items/<id>: دریافت یک آیتم خاص با استفاده از شناسه.
#### POST /api/items/: ایجاد یک آیتم جدید. نمونه بدنه JSON:
```
{
  "name": "New Item",
  "description": "This is a new item."
}

```
#### PUT /api/items/<id>: به‌روزرسانی یک آیتم موجود با استفاده از شناسه. نمونه بدنه JSON:
```
{
  "name": "Updated Item",
  "description": "This is an updated item."
}

````
#### DELETE /api/items/<id>: حذف یک آیتم با استفاده از شناسه.

## احراز هویت

#### این API از احراز هویت پایه استفاده می‌کند. برای دسترسی به انتهاها از اعتبارنامه‌های زیر استفاده کنید:

```
نام کاربری: admin
رمز عبور: password123

```

## مدیریت خطاها

API شامل مدیریت خطا برای مشکلات رایج است:

#### 404 Not Found: زمانی بازگردانده می‌شود که منبعی پیدا نشود.
#### 400 Bad Request: زمانی بازگردانده می‌شود که درخواست نامعتبر باشد.
#### 500 Internal Server Error: زمانی بازگردانده می‌شود که یک خطای غیرمنتظره رخ دهد.



# مجوز
#### این پروژه تحت مجوز MIT منتشر شده است.
#### این مثال یک راه‌اندازی جامع برای یک API RESTful با استفاده از Flask ارائه می‌دهد.



