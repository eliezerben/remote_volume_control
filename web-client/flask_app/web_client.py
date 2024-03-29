import os
import sys

from flask import Flask, request, jsonify, send_from_directory

MY_PATH = os.path.dirname(os.path.abspath(__file__))
bin_path = os.path.join(MY_PATH, '..', 'bin')
if not os.path.isdir(bin_path):
    bin_path = os.path.join(MY_PATH, '..', '..', 'bin')
sys.path.append(bin_path)
import client

import client_config


app = Flask(__name__, static_folder='react-build')

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/<path:path>')
def static_data(path):
    print(path)
    return send_from_directory(app.static_folder, path)

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