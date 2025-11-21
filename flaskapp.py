from flask import Flask
from flask import request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scheduler')
def scheduler():


if __name__ == "__main__":
    app.run()