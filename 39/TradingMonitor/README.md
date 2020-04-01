### 工程创建之后
#### 初始目录结构
templates
TradingMonitor/
├── TradingMonitor
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── db.sqlite3
└── manage.py

#### 开发步骤
1.创建python package - TradingMonitor/migrations
2.开发MVC各个组件
3.代码更改后执行python manage.py makemigrations
4.执行python manage.py migrate
5.运行项目

#### 执行完步骤4后的目录结构
templates
├── positions.html
TradingMonitor/
├── TradingMonitor
│   ├── migrations
│   ├────├── 0001_initial.py
│   ├────├── __init__.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── models.py
│   ├── views.py
│   ├── asgi.py
│   └── wsgi.py
├── db.sqlite3
└── manage.py

#### 可选
1.创建admin，python manage.py createsuperuser