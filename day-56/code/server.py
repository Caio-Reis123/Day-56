from flask import Flask, render_template
app = Flask(__name__)


# COMANDOS:
# set FLASK_APP=server.py
# $env:FLASK_APP = "server.py"
# flask run


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)