from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect ("/menu", code=302) 
@app.route("/menu")
def menu ():
    return """
<!doctype html>
<html>
    <head>
        <title> НГТУ,ФБ,Лабораторные работы </title> 
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB- программирование, часть 2. Список лабораторных, меню
        </header>

        <h1>web-сервер на flask</h1>
        <ol>
                <li>
                    <a href="/lab1" target="_blank"   > Лабораторная работа 1 </a>
                </li>

        <footer>
            &copy; Давоян Карине, ФБИ-11, 3 курс, 2023
        </footer>
    </body>
</html>
"""
@app.route("/lab1")
def lab1():
    return """
<!doctype html>
<html>
    <head>
        <title> Давоян Карине Горовна, лабораторная 1  </title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>
        <h1> Flask — фреймворк для создания веб-приложений на языке
        программирования Python, использующий набор инструментов
        Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
        называемых микрофреймворков — минималистичных каркасов
        веб-приложений, сознательно предоставляющих лишь самые базовые возможности.</h1>
        
        <footer>
            &copy; Давоян Карине, ФБИ-11, 3 курс, 2023
        </footer>
    </body>
</html>
"""
@app.route('/lab1/oak')
def oak():
    return '''
<!doctype html>
<html>
    <body>
        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='oak.jpg') + '''">
        <link rel="stylesheet" href="''' +url_for('static', filename='lab1.css')+'''"
        <h2>f</h2>
    </body>
</html>
'''



    




   





