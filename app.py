from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect



app = Flask(__name__)
app.secret_key = "qwertyuiop"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

logged_in = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=False, nullable=False)
    username = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), unique=False, nullable=False)

    def __repr__(self):
        return f'User {self.name}'

#Home
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


#Network
@app.route('/network')
def network():
    user = 'Login'
    return render_template('network.html', user=user)


#Login
@app.route('/login', methods=['POST', 'GET'])
def login():
    global logged_in
    if request.method=='POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']

        session["user"] = username


        found_username = False

        for entry in User.query.all():
            if  entry.username == username and entry.password==password:
                found_username = True

        if found_username:
            logged_in = True

            return redirect(url_for('user'))
            
        else:
            return redirect('/login')
            
    else:
        return render_template('login.html')

@app.route("/user")
def user():
    if 'user' in session:
        user = session['user']
        contacts = []
        search_results = User.query.all()
        return render_template('network.html', user=user, contacts=contacts, sr=search_results)
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)