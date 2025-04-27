from flask import Flask, jsonify
import datetime 
import socket

app = Flask(__name__)


@app.route('/api/v1/info')

def info():
    return jsonify({
        'time': datetime.datetime.now().strftime("%I:%M:%p on %B %d, %Y"),
        'hostname': socket.gethostname(),
        'message': 'you are doing great!!!i!<3',
        'runner': "self-hosted",
        'deployed': 'kubernetes',
        'env': 'dev',
        'app_name': 'python-app3'
    })

@app.route('/api/v1/healthz')

def health():
    return jsonify({
        'status': 'up'
    }), 200



if __name__ == '__main__':


    app.run(host="0.0.0.0")
