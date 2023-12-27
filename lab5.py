from flask import redirect, render_template, request, Blueprint  
import psycopg2 
 
lab5 = Blueprint('lab5', __name__) 
 
def dbConnect(): 
     conn = psycopg2.connect( 
        host='127.0.0.1', 
        database = 'knowledge_base', 
        user='karina_knowledge_base', 
        password='123') 
         
     return conn; 
 
def dbClose(cursor,connection): 
    cursor.close() 
    connection.close() 
 
@lab5.route('/lab5') 
def main(): 
    visibleUser='Anon' 
    conn = dbConnect() 
    cur = conn.cursor() 
 
    cur.execute('SELECT * FROM users;') 
 
    result = cur.fetchall() 
 
    print(result) 
 
    dbClose(cur,conn) 
 
 
    return 'go to console' 

 
@lab5. route('/lab5/register', methods=["GET", "POST"]) 
def registerPage(): 
    errors = [] 
 
    if request.method == "GET": 
        return render_template ("register.html", errors=errors) 
 
    username = request. form.get ("username") 
    password = request. form.get ("password") 
 
 
    if not (username or password): 
 
        errors. append ("Пожалуйста, заполните все поля") 
        print (errors) 
        return render_template ("register html", errors=errors) 
 
    conn = dbConnect () 
    cur = conn.cursor() 
 
    cun.execute(f"SELECT username FROM users WHERE username = '{username}';") 
 
    if cur.fetchone: 
        errors.append('Пользователь с данным именем уже существует') 
        dbClose(cur,conn) 
        return render_template('register.html',errors=errors) 
    cur.execute(f"INSERT INTO users (username,password) VALUES ('{username}','{password}');") 
 
    dbClose(cur,conn) 
    return redirect('/lab5/loginn')

 @lab5.route('/lab5/users')
 def users():
    

    cur = conn.cursor()
    cur.execute('SELECT username FROM users')
    users = [row[0] for row in cur.fetchall()]
    conn.close()
    return (users)
    
    return render_template('users.html', users=users)

@lab5.route('/lab5/loginn', methods = ["GET", "POST"])
def loginnPage():
   

    errors = []

    if request.method == "GET":
        return render_template("loginn.html", errors=errors)

    username=request.form.get("username")
    password = request.form.get("password")

    if not (username or password):
        errors.append("Пожалуйста, заполните все поля")
        return render_template('loginn.html', errors=errors)

    conn = dbConnect()
    cur = conn.cursor()
    print("ffff")

    cur.execute(f"SELECT id, password FROM users WHERE username = '{username}'")


    result = cur.fetchone()

    if result is None:
        errors.append("Неправильный логин или пароль")
        dbClose(cur, conn)
        return render_template("loginn.html", errors=errors)

    userID, hashPassword = result

    if check_password_hash(hashPassword, password):
        session['id'] = userID
        session['username'] = username
        dbClose(cur, conn)
        return redirect("/lab5")

    else:
        errors.append("Неправильный логин или пароль")
        return render_template("loginn.html", errors=errors)

@lab5.route('/lab5/cozdzametki', methods = ["GET", "POST"])
def cozdzametkiArticle():
    errors=[]

    userID = session.get("id")

    if userID is not None:
        if request.method == "GET":
            return render_template("cozdzametki.html", errors=errors)
  
        if request.method == "POST":
            text_article = request.form.get("text_article")
            title = request.form.get("title_article")

            if len(text_article) == 0:
                errors.append("Заполните текст")
                return render_template("cozdzametki.html", errors=errors)

            conn = dbConnect()
            cur = conn.cursor()

            cur.execute(f"INSERT INTO articles(user_id,title,article_text) VALUES ({userID}, '{title}', '{text_article}') RETURNING id")
            new_article_id = cur.fetchone()[0]
            conn.commit()

            dbClose(cur, conn)

            return redirect(f"/lab5/articles/{new_article_id}")
    return redirect("/lab5/loginn")   



@lab5.route("/lab5/articles/<string:article_id>")
def getArticle(article_id):
    userID = session.get("id")

    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()

        cur.execute("SELECT title, article_text FROM articles WHERE id = %s and user_id = %s",(article_id, userID))

        articleBody = cur.fetchone()

        dbClose(cur, conn)

        if articleBody is None:
            return "Not found !"

        text = articleBody[1].splitlines()
        return render_template("articles.html", article_text = text, article_title = articleBody[0], username = session.get("username"))

@lab5.route("/lab5/articles")
def getAllArticles():
    userID = session.get("id")

    if userID is not None:
        conn = dbConnect()
        cur = conn.cursor()

        cur.execute("SELECT id, title, article_text FROM articles WHERE user_id = %s", (userID,))

        articles = cur.fetchall()

        dbClose(cur, conn)

        if articles is None:
            return "No articles found !"

        return render_template("articles.html", articles = articles, username = session.get("username"))



@lab5.route('/lab5/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect("/lab5/loginn")

    