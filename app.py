import os
from flask import Flask, render_template, request, redirect

from libs.connect_usb import usb
from libs.write_to_goole_sheet import getresult

app = Flask(__name__)

PORT = os.environ.get("PORT", 8080)


@app.route('/', methods=['GET'])
def start():
    return render_template('register.html')


@app.route('/register', methods=['POST'])
def store_guest():
    name = getresult(request.form['membernumber'], request.form['name'], request.form['lodge'])
    return redirect('/')


if __name__ == '__main__':
    u = usb()
    u.start()
    app.run(host="localhost", port=PORT)

