from flask import Flask, render_template, request, make_response, jsonify
from waitress import serve  # Import the serve function from Waitress
from robotToyLogic import logic

app = Flask(__name__)

# Sets the size of n*n grid
sizeOfBoard = 5


@app.route('/')
def index():
    # Pass data to the template
    x = int(request.cookies.get('x', default=-1))
    y = int(request.cookies.get('y', default=-1))
    pos = int(request.cookies.get('pos', default=-1))
    boardSize = sizeOfBoard
    return render_template('index.html', x=x, y=y, pos=pos, boardSize=boardSize)


@app.route('/place', methods=['POST'])
def place():
    # Taking form input through request
    x = request.form['x']
    y = request.form['y']
    pos = request.form['option']
    # Checking constraints and setting it as cookie
    response = make_response(jsonify({'message': 'success'}))
    if int(x) < 5 and int(x) >= 0 and int(y) < 5 and int(y) >= 0:
        response.set_cookie('x', str(x))
        response.set_cookie('y', str(y))
        response.set_cookie('pos', str(pos))

    return response


@app.route('/execute-command', methods=['POST'])
def move():
    # Takes current position from cookies
    x = int(request.cookies.get('x'))
    y = int(request.cookies.get('y'))
    pos = int(request.cookies.get('pos'))
    # Takes command to execute from body of request
    command = request.get_json()['command']
    # Executes logic function
    [x, y, pos] = logic.executeCommand(x, y, pos, command)
    response = make_response(jsonify({'message': 'success'}))
    # Checking constraints and setting it as cookie
    if int(x) < sizeOfBoard and int(x) >= 0 and int(y) < sizeOfBoard and int(y) >= 0:
        response.set_cookie('x', str(x))
        response.set_cookie('y', str(y))
        response.set_cookie('pos', str(pos))
    return response


@app.route('/reset', methods=['POST'])
def reset():
    # Resets by setting cookie value to -1
    response = make_response(jsonify({'message': 'success'}))
    response.set_cookie('x', str(-1))
    response.set_cookie('y', str(-1))
    response.set_cookie('pos', str(-1))
    return response


if __name__ == '__main__':
    # Use Waitress to serve the app
    app.run()

