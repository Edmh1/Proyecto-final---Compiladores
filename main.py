from flask import Flask

app = Flask(__name__)

@app.route('/parser')
def parser():
    lexer()#codigo
    pass

@app.route('/lexer')
def lexer():
    pass

if __name__ == '__main__':
    app.run(debug=True)