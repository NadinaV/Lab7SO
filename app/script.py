from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Dockerized App!"

@app.route('/data')
def data():
    try:
        conn = mysql.connector.connect(
            host="database",
            user="root",
            password="1234",
            database="my_database"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM data_table")
        data = cursor.fetchall()
        return jsonify(data)
    except Exception as e:
        print(f"Error: {e}")  
        return "Internal Server Error", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

