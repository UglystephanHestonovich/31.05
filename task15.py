from flask import Flask, request
import sqlite3

app = Flask(__name__)


@app.route('/store/<id>/', methods=['GET'])
def store_id(id):
    sqlite_connection = sqlite3.connect('database.db')
    cursor = sqlite_connection.cursor()
    print("Подключен к SQLite")
    print(id)

    sqlite_select_query = f"""SELECT * from store where id = {id}"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    print("Всего строк:  ", len(records))
    print("Вывод каждой строки")
    if len(records) > 0:
        for row in records:
            print("Имя:", row[0])
            print("id:", row[1])
            name = row[0]
        cursor.close()
        return {'status': 'ok', 'exist': True, 'name': name}
    else:
        cursor.close()
        return {'status': 'ok', 'exist': False, 'name': ''}


@app.route('/store/', methods=['POST'])
def store():
    id_request = request.json['id']
    name_request = request.json['name']
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    sqlite_select_query = """SELECT * from STORE WHERE id = ?"""
    cursor.execute(sqlite_select_query, (id_request,))
    records = cursor.fetchall()
    f = False
    for row in records:
        if row[1] == id_request:
            f = True
    if f == False:
        sqlite_insert_query = """INSERT INTO STORE
                                            (id, name)
                                            VALUES (?, ?);"""
        tuple = (id_request, name_request)
        cursor.execute(sqlite_insert_query, tuple)
        connection.commit()
    cursor.close()
    return {'status': 'ok'}


@app.route('/product/<id>/', methods=['GET'])
def product_id(id):
    sqlite_connection = sqlite3.connect('database.db')
    cursor = sqlite_connection.cursor()
    print("Подключен к SQLite")
    print(id)

    sqlite_select_query = f"""SELECT * from product where id = {id}"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    print("Всего строк:  ", len(records))
    print("Вывод каждой строки")
    if len(records) > 0:
        for row in records:
            print("Имя:", row[0])
            print("id:", row[1])
            name = row[0]
        cursor.close()
        return {'status': 'ok', 'exist': True, 'name': name}
    else:
        cursor.close()
        return {'status': 'ok', 'exist': False, 'name': ''}





@app.route('/product/', methods=['POST'])
def product():
    id_request = request.json['id']
    name_request = request.json['name']
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    sqlite_select_query = """SELECT * from product WHERE id = ?"""
    cursor.execute(sqlite_select_query, (id_request,))
    records = cursor.fetchall()
    f = False
    for row in records:
        if row[1] == id_request:
            f = True
    if f == False:
        sqlite_insert_query = """INSERT INTO product
                                            (id, name)
                                            VALUES (?, ?);"""
        tuple = (id_request, name_request)
        cursor.execute(sqlite_insert_query, tuple)
        connection.commit()
    cursor.close()
    return {'status': 'ok'}














app.run(host="128.1.12.94", port=5003)
