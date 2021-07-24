from flask import Flask, render_template
app = Flask(__name__)


#Home
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


#Network
@app.route('/network')
def network():
    contacts=["Name 1", "Name 2", "Name 3", "Name 1", "Name 2", "Name 3" ]
    search_results=["Account1", "Account2", "Account3"]
    return render_template('network.html', contacts=contacts, sr=search_results)


#Login
@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)