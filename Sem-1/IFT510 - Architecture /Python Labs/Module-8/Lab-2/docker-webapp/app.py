## Student Name: Harsh Siddhapura
## Student ID: 1230169813
## Date: 11/23/2023

from flask import Flask 

app = Flask(__name__)
@app.route('/')
def hello():
    return 'Hello, I am a graduate student Harsh Siddhapura IFT 510 2023!'
if __name__ == '__main__':
    app.run(host='0.0.0.0')