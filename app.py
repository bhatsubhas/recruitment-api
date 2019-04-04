from flask import Flask
from flask import jsonify
from flask import make_response
from flask import request
from flask import abort
from flask import url_for
from data_provider_service import DataProviderService

DATA_PROVIDER = DataProviderService(15)

app = Flask(__name__)

# ROUTING:
#   Routing configuration using @app.route() decorator
#


@app.route("/api", methods=['GET'])
def list_routes():
    result = []
    for rt in app.url_map.iter_rules():
        result.append(
            {
                'methods': list(rt.methods),
                'route': str(rt)
            }
        )
    return jsonify({'routes': result, 'total': len(result)})


def candidate():
    candidates = DATA_PROVIDER.get_candidates()
    return jsonify({'candidates': candidates, 'total': len(candidates)})


app.add_url_rule('/api/candidate', 'candidate', candidate)


@app.route('/api/candidate/<string:id>', methods=['GET'])
def candidate_by_id(id):
    candidate = DATA_PROVIDER.get_candidate(id)
    if candidate:
        return jsonify(candidate)
    else:
        abort(404)


@app.route('/api/candidate/<string:id>/name/<string:new_name>', methods=['PUT'])
def update_candidate(id, new_name):
    update_count = DATA_PROVIDER.update_name(id, new_name)
    if update_count == 0:
        return abort(404)
    else:
        return jsonify({'total_updated': update_count})


@app.route('/api/random/candidate', defaults={'nrOfItems': 1}, methods=['GET'])
@app.route('/api/random/candidate/<int:nrOfItems>', methods=['GET'])
def random(nrOfItems):
    candidates = DATA_PROVIDER.get_random_candidates(nrOfItems)
    return jsonify({'candidates': candidates, 'total': len(candidates)})


@app.route('/api/candidate/<string:id>', methods=['DELETE'])
def delete(id):
    if DATA_PROVIDER.delete_candidate(id):
        return make_response('', 200)
    else:
        return abort(404)


@app.route('/api/candidate', methods=['POST'])
def add_candidate():
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    new_candidate_id = DATA_PROVIDER.add_candidate(first_name, last_name)
    return jsonify(
        {
            'id': new_candidate_id,
            'url': url_for('candidate_by_id', id=new_candidate_id)
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
