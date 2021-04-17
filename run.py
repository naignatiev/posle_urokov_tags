from flask import Flask
from flask_restful import Api, request
from flask.json import jsonify

app = Flask(__name__)
api = Api(app)


from naive_tagger import NaiveTagger


@app.route('/get_tags', methods=['GET', 'POST'])
def get_tags():
    name = request.args.get('name', '')
    desc = request.args.get('desc', '')
    print(name, desc)
    return jsonify({'tags': NaiveTagger(name + ' ' + desc).get_tag(),
                    'params': {'name': name, 'desc': desc}})


@app.route('/get_events', method=['GET', 'POST'])
def get_top_events():
    raise NotImplementedError


@app.route('/get_section', method=['GET', 'POST'])
def get_best_section():
    raise NotImplementedError
