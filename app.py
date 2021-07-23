from flask import Flask, template_render
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return template_render('index.html')


if __name__ == '__main__':
    app.run('FLASK_DEBUG=1')