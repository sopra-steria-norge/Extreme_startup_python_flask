import socket
import requests
from flask import Flask, request

app = Flask(__name__)


def test_calculate_answer(question):
    if 'sun' in question:
        return 'Yellow'
    return ''


def calculate_answer(question):
    return ''


@app.route("/")
def answer():
    q = request.args.get("q", "")
    r = request.args.get("r", "")
    print(q)
    print(r)
    return calculate_answer(q)


if __name__ == "__main__":
    ip = socket.gethostbyname(socket.gethostname())
    respons = requests.get("http://SERVER_IP_HERE:5000", {'ip':ip})

    app.run(debug=True, host='0.0.0.0')
