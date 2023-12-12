from flask import Blueprint,render_template, request
lab4 = Blueprint('lab7', __name__)

@lab7.route('/lab7/')
def main():
    return render_template('lab7/index.html')  