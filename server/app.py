from flask import Flask

app = Flask(__name__)

# Index view
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Print String view
@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return param

# Count view
@app.route('/count/<int:param>')
def count(param):
    numbers = '\n'.join(str(i) for i in range(param + 1))
    return numbers

# Math view
@app.route('/math/<float:num1><string:operation><float:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
    elif operation == '%':
        result = num1 % num2

    if result is not None:
        return f'<p>Result of {num1} {operation} {num2} is: {result}</p>'
    else:
        return '<p>Invalid operation or division by zero.</p>'

if __name__ == '__main__':
    app.run(port=5555)
