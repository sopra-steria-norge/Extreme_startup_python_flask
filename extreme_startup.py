import socket

import requests
from flask import Flask, request
app = Flask(__name__)

def solve_add_question(question):
    return '4'

def calculate_answer(question):
    if '+' in question:
        return solve_add_question(question)
    if 'sun' in question:
        return "Yellow"
    return ''

@app.route("/")
def answer():
    q = request.args.get("q", "")
    print(q)
    return calculate_answer(q)

if __name__ == "__main__":
    ip = socket.gethostbyname(socket.gethostname())
    respons = requests.get("http://150.106.227.80:5000", {'ip':ip})

    app.run(debug=True, host='150.106.227.80')
    # app.run(debug=True, host='0.0.0.0')

