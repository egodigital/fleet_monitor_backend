#!flask/bin/python
from flask import Flask, jsonify
from api_template import get_env

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]


@app.route('/environment', methods=['GET'])
def get_tasks():
    return str(get_env());

if __name__ == '__main__':
    app.run(debug=True, port=80)