from flask import Blueprint,render_template, request
lab4 = Blueprint('lab4', __name__)

@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')  


@lab4.route('/lab4/login', methods= ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')  
    
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'Alex' and password == '123':
        return render_template('success1.html',username=username)
    
    error = 'Неверные логин и/или пароль' 
    return render_template ('login.html', error=error, username=username,password=password)

@lab4.route('/lab4/fridge', methods= ['GET','POST'])
def fridge():
    error = ''
    if request.method=='GET':
        return render_template('fridge.html', error=error)

    temperature=request.form.get('temperature')

    if temperature == '':
        error = 'Не задана температура'
    else:
        temperature = int(temperature)
        if temperature < -12:
            error = "Не удалось установить температуру, значение слишком низкое "
        elif temperature > -1:
            error = 'Не удалось установить температуру, значение слишком высокое'
        elif (temperature >= -12) and (temperature <= -9):
            error = f'Температура установлена: {temperature}❄️❄️❄️'
        elif (temperature >= -8) and (temperature <= -5):
            error = f'Температура установлена: {temperature}❄️❄️'
        elif (temperature >= -4) and (temperature <= -1):
            error = f'Температура установлена: {temperature}❄️'
    return render_template('fridge.html',temperature=temperature, error=error)
        
@lab4.route('/lab4/zerno', methods= ['GET','POST'])
def zerno():
    if request.method == 'GET':
      return render_template('zerno.html')
    price = 0
    error = ''
    error1= ''
    zerno = request.form.get('zerno')
    weight = request.form.get('weight')

    if weight=='':
        error = "Нужный вес не задан"
        return render_template('zerno.html',error=error)
    weight = int(weight)


    if zerno == 'barley':
        price = 12000 * weight
    elif zerno == 'oats':
        price = 8500 * weight
    elif zerno == 'wheat':
        price = 8700 * weight
    else:
        zerno = 'rye'
        price = 14000 * weight
    if weight <= 0:
        error = "Значение неверно"
        return render_template('zerno.html', error=error)
    elif weight > 500:
        error = "Нужного объема зерна в наличии нет"
        return render_template('zerno.html',error=error)
    elif weight > 50:
        price = price - (price * 10/100)
        error1 = "Скидка 10% за большой объем"
    return render_template('zernosk.html',price=price, zerno=zerno, weight=weight, error=error,error1=error1)

        
@lab4.route('/lab4/zernosk')
def zernosk():
    return render_template('zernosk.html')


@lab4.route('/lab4/cookies', methods = ['GET', 'POST'])
def cookies():
    if request.method == 'GET':
        return render_template('cookies.html')

    color = request.form.get('color')
    b_color = request.form.get('background-color')
    f_size = request.form.get('font-size')
    error=''

    if color ==b_color:
        error = 'цвет текста не должен совпать с цветом фона'
        return render_template('cookies.html', error=error)
    elif color !=b_color:
        color = color
    
    if f_size == '':
        error = 'Задайте размер текста'
        return render_template('cookies.html',error=error)
    
    if f_size.isdigit() and 5 <= int(f_size) <= 30:
        f_size = str(f_size)+'px'
    else:
        error = 'Размер текста должен быть от 5px до 30px'
        return render_template('cookies.html', error=error)

    headers = {
        'Set-Cookie':'color=' + color + f_size + b_color + '; path=/',
        'Set-Cookie':'font-size=' + f_size + '; path=/',
        'Set-Cookie':'background-color='  + b_color + '; path=/',
        'Location': '/lab4/cookies'
    }
    return '', 303, headers
