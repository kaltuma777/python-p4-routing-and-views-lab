from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:number>')
def count(number):
    l = [n for n in range(number)]
    w = '\n'.join(map(str, l))
    return f'{w}\n'

@app.route('/math/<int:num1>/<operator>/<int:num2>')
def math(num1, operator, num2):
    if operator == '+':
        return f'{num1 + num2}'
    if operator == '-':
        return f'{num1 - num2}'
    if operator == '*':
        return f'{num1 * num2}'
    if operator == 'div':
        return f'{num1 / num2}'
    if operator == '%':
        return f'{num1 % num2}'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
