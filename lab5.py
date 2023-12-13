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
 
    return redirect('/lab5/login')

    