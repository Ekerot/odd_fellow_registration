import os
from flask import Flask, render_template, redirect, url_for
from libs.connect_usb import start_usb

app = Flask(__name__)

start_usb()

PORT = os.environ.get("PORT", 8080)


@app.route('/register')
def start():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(host="localhost", port=PORT)
