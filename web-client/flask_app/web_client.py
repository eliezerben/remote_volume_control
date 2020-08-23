import os
import sys

from flask import Flask, render_template, request, jsonify

MY_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(MY_PATH, '..', '..', 'bin'))
import client

import client_config


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.jinja')


@app.route('/servers/<location>/send-command/', methods=['POST'])
def send_command(location):
    if request.method != 'POST':
        return
    req_data = request.get_json()
    command_name = req_data['command']
    command_value = req_data['value']
    full_command = (command_name + ' ' + command_value) if command_value != '' else command_name
    response = client.send_command(full_command, location)

    res_obj = {
        'status': None,
        'value': '',
    }

    if response == 'ERROR':
        res_obj['status'] = 'error'
    elif response == 'SUCCESS':
        res_obj['status'] = 'success'
    else:
        res_obj['status'] = 'success'
        res_obj['value'] = response

    response = jsonify(res_obj)
    return response


@app.route('/servers/')
def get_servers():
    print(client_config.servers)
    return jsonify(client_config.servers)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', '*')
    response.headers.add('Access-Control-Allow-Methods', '*')
    return response


if __name__ == '__main__':
    app.run()