from flask import Blueprint,render_template, request
import math

lab3 = Blueprint('lab3', __name__)

@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')  

@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'

    errors2 = {}
    age = request.args.get('age')
    if age == '':
        errors2['age'] = 'Заполните поле!'    
    
    sex = request.args.get('sex')
    return render_template('form1.html', user=user, age=age, sex=sex, errors=errors, errors2=errors2) 


@lab3.route('/lab3/order')
def order():
    return render_template('order.html')


@lab3.route('/lab3/pay')
def pay():
    price=0
    drink=request.args.get('drink')
# Пусть кофе стоит 120, черный чай 80, зеленый чай 70
    if drink == 'coffee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

#Добавка молока удорожает напиток на 30, а сахара на 10.
    if request.args.get('milk') == 'on':
        price +=30
    if request.args.get('sugar') == 'on':
        price +=10
    return render_template('pay.html', price=price)

@lab3.route('/lab3/success')
def success():
    return render_template('success.html')

@lab3.route('/lab3/tickets')
def tickets():
    errors3 = {}
    user2 = request.args.get('user2')
    if user2 == '':
        errors3['user2'] = 'Заполните поле!'

    errors4 = {}
    agee = request.args.get('agee')
    if agee == '':
        print("разрешено")
        errors4['agee'] = 'Заполните поле!'

    errors5 = {}
    point = request.args.get('point')
    if point == '':
        errors5['point'] = 'Заполните поле!'

    errors6 = {}
    point2 = request.args.get('point2')
    if point2 == '':
        errors6['point2'] = 'Заполните поле!'
    
    errors7 = {}
    date = request.args.get('date')
    if date == '':
        errors7['date'] = 'Заполните поле!'

    typee6 = request.args.get('typee6')
    typee3 = request.args.get('typee3')
    typee2 = request.args.get('typee2')

    return render_template('tickets.html', user2=user2,agee=agee,errors3=errors3,errors4=errors4,
    errors5=errors5,errors6=errors6,errors7=errors7,point=point,point2=point2,date=date,typee2=typee2,typee3=typee3,typee6=typee6) 






