from flask import request
from flask import jsonify
from flask import Flask

app = Flask(__name__)

@app.route('/static/hello',methods=['POST'])
def hello():
    message = request.get_json(force=True)
    name = message['name']
    response = {
        'greeting': 'Hello, ' + name + '!'
    }
    return jsonify(response)
# Run in terminal
# \flask_apps>set FLASK_APP=hello_app.py
# \flask_apps>flask run --host=0.0.0.0
# Then in browser
# http://localhost:5000/static/hello.html