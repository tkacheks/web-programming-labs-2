


from flask import Blueprint, render_template, request, jsonify, abort

lab9 = Blueprint('lab9', __name__)


@lab9.route('/lab9/')
def main():
    return render_template('lab9/index.html')


@lab9.app_errorhandler(404)
def not_found(e):
    return render_template('404.html')


@lab9.app_errorhandler(500)
def error500(e):
    return render_template('500.html')


@lab9.route('/lab9/500')
def error():
    result = 1 / 0
    return result

@lab9.route('/lab9/otk', methods=['GET', 'POST'])
def otk():
    otk = ""
    username = request.form.get('username')
    username2 = request.form.get('username2')
    sex = request.form.get('sex')

    if username and username2 and sex == 'м':
        otk = f'Желаю, чтобы {username2} был счастливым в новом 2024 году! от {username}'

    if username and username2 and sex == 'ж':
        otk = f'Желаю, чтобы {username2} была счастливой в новом 2024 году! от {username}'
    return render_template('otk.html', otk=otk)