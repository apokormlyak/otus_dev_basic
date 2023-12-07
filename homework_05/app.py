"""
Домашнее задание №5
Первое веб-приложение

создайте базовое приложение на Flask
создайте index view /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""
from flask import Flask, render_template
import os.path

app = Flask(__name__)


@app.get("/", endpoint="index")
def get_home_page():
    return render_template("base.html")


@app.get("/about/")
def about_page():
    content_path = os.path.dirname(__file__)
    filename = "lorem_ipsum.txt"
    with open(os.path.join(content_path, filename), "r") as f:
        content = "\n".join(line.strip() for line in f)
    return content


if __name__ == "__main__":
    app.run(port=8000, debug=True)
