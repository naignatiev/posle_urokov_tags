from flask import Flask
from flask_restful import Api, request
from flask.json import jsonify

app = Flask(__name__)
api = Api(app)


from tagger import NaiveTagger
from recommendations import Recommendation


@app.route('/get_tags', methods=['GET', 'POST'])
def get_tags():
    name = request.args.get('name', '')
    desc = request.args.get('desc', '')
    print(name, desc)
    return jsonify({'tags': NaiveTagger(name + ' ' + desc).get_tag(),
                    'params': {'name': name, 'desc': desc}})


@app.route('/get_events', methods=['GET', 'POST'])
def get_top_events():
    raise NotImplementedError


@app.route('/get_organizations', methods=['GET', 'POST'])
def get_best_section():
    child_id = request.args.get('child_id', '1')
    return {'org_ids': Recommendation(default_score=3).get_organizations(child_id),
            'params': {'child_id': child_id}}
