import os
from flask import Flask, render_template, request, redirect, url_for

from libs.connect_usb import usb
from libs.write_to_goole_sheet import getresult

app = Flask(__name__)

PORT = os.environ.get("PORT", 8080)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        return render_template('register.html', name=request.form['name'], submission_successful=True)
    else:
        return render_template('register.html', name='', submission_successful=False)


@app.route('/register', methods=['POST'])
def store_guest():
    getresult(request.form['membernumber'], request.form['name'], request.form['lodge'])
    return redirect(url_for('index'), code=307)


if __name__ == '__main__':
    u = usb()
    u.start()
    app.run(host="localhost", port=PORT, threaded=True)

