from flask import Flask,render_template

app = Flask(__name__)

@app.route('/') #  http://127.0.0.1:5000/
def index():
    return render_template('index.html')
@app.route('/login') # http://127.0.0.1:5000/login
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)