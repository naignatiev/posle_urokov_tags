# Posle Urokov Tags
Репозиторий API работы с тэгами секций, ивентов и детей.

# Описание модуля
Рекомендательная система представляет из себя REST API, реализованное с помощью flask.

На данном этапе реализованы методы извлечения тегов из текстовых данных и 
рекомендация секций на основе child_id.

# Installation
```shell
pip3 install -r requirements.txt
export FLASK_APP=run.py
flask run
```

# Example
```python3
import requests

name = "Школа Let's Go"
desc = "Наша школа английского языка самая лучшая, а ещё мы учим детей играть в баскетбол"
flask_app_addr = 'http://127.0.0.1:5000/'
response = requests.get(f'{flask_app_addr}get_tags?name={name}&desc={desc}')
print(response.json()['tags']) # ['Английский язык', 'Баскетбол']
```

# License
Code is [MIT licensed](./LICENSE)
