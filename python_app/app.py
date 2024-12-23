'''from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Функция для подключения к базе данных
def get_db_connection():
    conn = psycopg2.connect(
        host='my_pg',  # имя сервиса базы данных из docker-compose.yml
        database='my_database',
        user='postgres',
        password='password'
    )
    return conn

# Эндпоинт для получения данных из таблицы emp
@app.route('/emp')
def emp():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM emp;')
    emp = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(emp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)'''

from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    pass

server_address = ('', 8000)
httpd = HTTPServer(server_address, MyHandler)

print("Starting server on port 8000...")
httpd.serve_forever()
