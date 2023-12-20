from flask import Blueprint, redirect, url_for
lab1 = Blueprint('lab1',__name__)

@lab1.route("/")
@lab1.route("/index")
def start():
    return redirect ("/menu", code=302) 


@lab1.route("/menu")
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
                <li>
                    <a href="/lab2" target="_blank"   > Лабораторная работа 2 </a>
                </li>
                <li>
                    <a href="/lab3" target="_blank"   > Лабораторная работа 3 </a>
                </li>
                <li>
                    <a href="/lab4" target="_blank"   > Лабораторная работа 4 </a>
                </li>
                 <li>
                    <a href="/lab5" target="_blank"   > Лабораторная работа 5 </a>
                </li>
                <li>
                    <a href="/lab7" target="_blank"   > Лабораторная работа 7 </a>
                </li>
                <li>
                    <a href="/lab8" target="_blank"   > Лабораторная работа 8 </a>
                </li>
                <li>
                    <a href="/lab9" target="_blank"   > Лабораторная работа 9 </a>
                </li>

        </ol>
        </ol>
        <footer>
            &copy; Давоян Карине, ФБИ-11, 3 курс, 2023
        </footer>
    </body>
</html>
"""


@lab1.route("/lab1")
def lab():
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
        <ol>
                <li>
                    <a href="/menu" target="_blank"   > Меню </a>
                </li>
        </ol>
        <h2>Реализованные роуты</h2>
         <ol>
                <li>
                    <a href="/lab1/oak" target="_blank"   > Картинка дуба</a>
                </li>
                <li>
                    <a href="/lab1/student" target="_blank"   > ФИО студента НГТУ </a>
                </li>
                <li>
                    <a href="/lab1/python" target="_blank"   > Информация про python </a>
                </li>
                <li>
                    <a href="/lab1/color" target="_blank"   > Произвольная страница </a>
                </li>
                
                
        </ol>
        <footer>
            &copy; Давоян Карине, ФБИ-11, 3 курс, 2023
        </footer>
    </body>
</html>
"""


@lab1.route('/lab1/oak')
def oak():
    return '''
<!doctype html>
<html>
    <header>
            НГТУ, ФБ, WEB- программирование, часть 2. 
    </header>
    <body>
        <h1>Дуб</h1>
        <img src="''' + url_for('static', filename='oak.jpg') + '''">
        <link rel="stylesheet" href="''' +url_for('static', filename='lab1.css')+'''">
        <footer>
            &copy; Давоян Карине, ФБИ-11, 3 курс, 2023
        </footer>
    </body>
</html>
'''
@lab1.route('/lab1/student')
def nstu():
    return '''
<!doctype html>
<html>
    <header>
            НГТУ, ФБ, WEB- программирование, часть 2. 
    </header>
    <body>
        <h1>Давоян Карине Горовна</h1>
        <img src="''' + url_for('static', filename='nstu.jpeg') + '''">
        <link rel="stylesheet" href="''' +url_for('static', filename='lab1.css')+'''">

        <footer> 
            &copy; Давоян Карине, ФБИ-11, 3 курс, 2023
        </footer>
    </body>
</html>
'''


@lab1.route('/lab1/python')
def python():
    return '''
<!doctype html>
<html>
    <header>
            НГТУ, ФБ, WEB- программирование, часть 2. 
    </header>
    <body>
        <h1>Python — это язык программирования, который широко используется в интернет-приложениях, разработке
         программного обеспечения, науке о данных и машинном обучении (ML). Разработчики используют Python,
          потому что он эффективен, прост в изучении и работает на разных платформах. Программы на языке 
          Python можно скачать бесплатно, они совместимы со всеми типами систем и повышают скорость разработки.</h1>
        <img src="''' + url_for('static', filename='python.jpg') + '''">
        <link rel="stylesheet" href="''' +url_for('static', filename='lab1.css')+'''">
        <footer>
            &copy; Давоян Карине, ФБИ-11, 3 курс, 2023
        </footer>
    </body>
</html>
'''


@lab1.route('/lab1/color')
def color():
    return '''
<!doctype html>
<html>
    <header>
            НГТУ, ФБ, WEB- программирование, часть 2. 
    </header>
    <body>
        <h1> Воздействие цветов на мозг</h1> <br>
        <p> <b>Черный.</b> Одежда черного цвета стройнит людей, а мозгу помогает принимать более эффективные решения. <br>
            <b>Желтый.</b> Он оказывает самое сильное воздействие на мозг, повышая вашу самооценку и креативность. <br>
            <b>Синий/голубой.</b> Цвет спокойствия, помогает снять стресс и агрессию. В японском городе Нара на одной из опасных улиц города установили синие фонари, после чего количество преступлений снизилось там на 9% <br>
            <b>Зеленый.</b> Снижает усталость, раздражение и физическую боль.Обратите внимание на то, что в больницах часто используют именно голубые и зеленые халаты.<br>
Покрасьте комнату в <b>фиолетовый</b>  и в ней станет прохладнее. В <b>оранжевый</b> - станет теплее. 
Эти цвета помогают мозгу сильнее воспринимать температуру.</p> 
        <img src="''' + url_for('static', filename='color.jpg') + '''">
        <link rel="stylesheet" href="''' +url_for('static', filename='lab1.css')+'''">
        <footer>
            &copy; Давоян Карине, ФБИ-11, 3 курс, 2023
        </footer>
    </body>
</html>
'''