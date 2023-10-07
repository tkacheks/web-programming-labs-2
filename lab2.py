from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2',__name__)

@lab2.route('/lab2/example')
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


@lab2.route('/lab2/')
def laba2():
    return render_template('lab2.html')


@lab2.route('/lab2/flowers')
def flowers():
    return render_template('flowers.html') 