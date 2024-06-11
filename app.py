from flask import Flask, request, render_template
import src
from flask_cors import CORS
import json
from ply.lex import LexToken

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://sigmachar-interprete.onrender.com/"}})

def find_lex_token(dictionary):
    if isinstance(dictionary, LexToken):
        return dictionary

    try:
        for key, value in dictionary.items():
            if isinstance(value, LexToken):
                return value
            elif isinstance(value, dict):
                result = find_lex_token(value)
                if result:
                    return result
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, LexToken):
                        return item
                    elif isinstance(item, dict):
                        result = find_lex_token(item)
                        if result:
                            return result
    except:
        return None
    
@app.route('/')
def start():
    return render_template('index.html')
    

@app.route('/parser', methods=['POST'])
def parser_route():
    result = None
    ast = None
    if request.method == 'POST':
        data = request.json['codeInput']
        src.lexer.input(data)
        while True:
            tok = src.lexer.token()
            if not tok:
                break
        try:
            ast = src.show_parser(data)
        except:
            result = find_lex_token(ast)
        if result is not None:
            resultJSON = {}
            resultJSON[0] = {
                'error': 'errorLex', 'line': result.lineno
            }
            return json.dumps(resultJSON)
        resultJSON = {}
        i = 0
        for statement in ast:
            resultado = src.evaluate_statement(statement)
            print(resultado)
            if(resultado != None):
                resultJSON[i] = {
                    'result' : 'resultado', 'content' : resultado
                }
                i += 1
        return json.dumps(resultJSON)

@app.route('/lexer', methods=['POST'])
def lexer_route():
    result = None
    ast = None
    resultJSON = {}
    if request.method == 'POST':
        data = request.json['codeInput']
        src.lexer.input(data)
        while True:
            tok = src.lexer.token()
            if not tok:
                break
        ast = src.show_parser(data)
        try:
            for statement in ast:
                pass
        except:
            resultJSON[0] = {
                'result' : 'incorrecto', 'content' : 'Hay errores en el código!!'
            }
            return json.dumps(resultJSON)
        
        print(result)
        if result is None:
            resultJSON[0] = {
                'result': 'correcto', 'content': 'No hay errores en el código :)' 
            }
            return json.dumps(resultJSON)
        else:
            resultJSON[0] = {
                'result' : 'incorrecto', 'content' : 'Hay errores en el código !!'
            }
            return json.dumps(resultJSON)

if __name__ == '__main__':
    app.run(debug=True)
