from flask import Flask, redirect, url_for, render_template
from lab1 import lab1

app = Flask(__name__)
app.register_blueprint(lab1)


@app.route('/lab2/example')
def example():
    name = 'Давоян Карине'
    num = "2."
    group = "ФБИ-11"
    kurs = '3 курс'
    fruits = [
        {'name': 'яблоко', 'price':100},
        {'name': 'груша', 'price':120},
        {'name': 'киви', 'price':80},
    ]
    books = [
        {'namee': 'Три мушкетера', 'author': 'Дюма', 'genre': 'Роман', 'str': '400 стр.' },
        {'namee': 'Джейн Эйр', 'author': 'Бронте', 'genre': 'Роман', 'str': '200 стр.' },
        {'namee': 'Три товарища', 'author': 'Ремарк', 'genre': 'Роман', 'str': '300 стр.' },
        {'namee': 'Война и мир', 'author': 'Толстой', 'genre': 'Роман', 'str': '800 стр.' },
        {'namee': 'Ревизор', 'author': 'Гоголь', 'genre': 'Комедия', 'str': '200 стр.' },
        {'namee': 'Отцы и дети', 'author': 'Тургенев', 'genre': 'Роман', 'str': '300 стр.' },
        {'namee': 'Идиот', 'author': 'Достоевский', 'genre': 'Роман', 'str': '200 стр.' },
        {'namee': 'Дубровский', 'author': 'Пушкин', 'genre': 'Роман', 'str': '200 стр.' },
        {'namee': 'Старик и море', 'author': 'Бронте', 'genre': 'Роман', 'str': '200 стр.' },
        {'namee': 'Джейн Эйр', 'author': 'Бронте', 'genre': 'Роман', 'str': '200 стр.' },
    ]
    return render_template('example.html', name= name, num = num, group = group, kurs = kurs,fruits = fruits, books = books)

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/flowers')
def flowers():
    return render_template('flowers.html') 





   





