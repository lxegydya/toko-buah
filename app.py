import os
from os.path import join, dirname
from dotenv import load_dotenv

from flask import Flask, render_template, jsonify, request

from pymongo import MongoClient

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME =  os.environ.get("DB_NAME")

client = MongoClient(MONGODB_URI)
db = client[DB_NAME]

app = Flask(__name__)

buah = []

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/get_fruits', methods=["GET"])
def get_fruits():
    return jsonify({"buah" : buah})

@app.route('/store_fruit', methods=['POST'])
def store_fruit():
    nama = request.form.get('nama')
    stok = request.form.get('stok')

    buah.append({"nama" : nama, "stok" : stok})

    return jsonify({'message': 'Berhasil'})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)