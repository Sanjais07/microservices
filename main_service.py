from flask import Flask, jsonify, request
import requests


app = Flask(__name__)

@app.route('/')
def home():
    return "Main Service"

@app.route('/service-a')
def call_service_a():
    response = requests.get('http://localhost:5001')
    return jsonify(response.json())

@app.route('/service-b')
def call_service_b():
    response = requests.get('http://localhost:5002')
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(port=5000)
