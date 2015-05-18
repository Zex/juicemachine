#!/usr/bin/env python3

from flask import Flask, request, jsonify
import time

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/juicemachine/flavor', methods=['GET'])
def get_flavor():
    print('got connection ...')
    
    return jsonify({'flavor':'orange'}), 200


if __name__ == '__main__':

    app.run(port = 15113, debug = True)

