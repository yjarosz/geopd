from flask import request
from flask import jsonify
from flask_login import login_required
from geopd.api import api_blueprint as api
from geopd.api import jsonapi
from geopd.orm import db


@api.route('/cores/')
@login_required
def get_cores():
    response = jsonapi.get_collection(db, request.args, 'cores')
    return jsonify(response.data)


@api.route('/cores/<int:core_id>')
@login_required
def get_core(core_id):
    response = jsonapi.get_resource(db, request.args, 'cores', core_id)
    return jsonify(response.data)


@api.route('/cores/<int:core_id>/posts/')
@login_required
def get_core_posts(core_id):
    response = jsonapi.get_related(db, request.args, 'cores', core_id, 'posts')
    return jsonify(response.data)