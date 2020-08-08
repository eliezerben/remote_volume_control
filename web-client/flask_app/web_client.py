import os
import sys

from flask import Flask, render_template, request

MY_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(MY_PATH, '..', 'bin'))
import client


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.jinja')


@app.route('/servers/<location>/send-command/', methods=['POST'])
def send_command(location):
    req_data = request.get_json()
    command_name = req_data['command']
    command_value = req_data['value']
    full_command = (command_name + ' ' + command_value) if command_value else command_name
    response = client.send_command(full_command, location)
    return response


if __name__ == '__main__':
    app.run()