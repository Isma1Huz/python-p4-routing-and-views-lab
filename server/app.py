#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):  # Fixed the typo here
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    result = ''
    for i in range(parameter):
        result += f'{i}\n'
    return result

@app.route('/math')
def math():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    operation = request.args.get('operation')
    
    result = 0
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return 'Error: Division by zero!'
    elif operation == '%':
        result = num1 % num2
    else:
        return 'Invalid operation'
    
    return f'Result: {result}'
if __name__ == '__main__':
    app.run(port=5555, debug=True)
