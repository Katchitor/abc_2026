# todo: добавьте во Flask маршруты для страниц (endpoint)
# - О компании
# - Контакты
# - Список постов
from flask import Flask

app = Flask(__name__)

@app.route("/about_company")
def about_company():
    return "<p>Информация о компании</p>"

@app.route("/contacts")
def contacts():
    return "<p>Контакты</p>"

@app.route("/posts")
def posts():
    return "<p>Список постов</p>"

if __name__== "__main__":
    app.run(host="0.0.0.0", port=5000)