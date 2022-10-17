# Оглавление

* [Запуск](#Запуск)
    * [Создание .env](#env)
    * [Старт](#Старт)

## Запуск

### env

Необходимо создать файл ".env" и поместить его в любое место проекта.  
В него записать:

```
SECRET_KEY=<Вами сгенерированый ключ>
DEBUG=False # Все как в питоне True/False
```

### Старт

```
git clone https://github.com/bfswrd/IntensiveYandex
cd IntensiveYandex
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Создать .env 
python manage.py runserver 127.0.0.1:8000
```
