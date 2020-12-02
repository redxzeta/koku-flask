from flask import Blueprint, request, jsonify
from service.koku import KokuService

koku = Blueprint("koku", __name__)
koku_service = KokuService()


@koku.route('/koku/<_id>', methods=['POST'])
def add_koku(_id):
    obj = request.get_json()
    return jsonify(
        koku_service.add_koku(_id=_id, koku=obj)
    )


@koku.route('/koku', methods=['GET'])
def get_kokus():
    return jsonify(koku_service.get_kokus())


@koku.route('/koku/<_id>', methods=['GET'])
def get_koku_by_id(_id):
    return jsonify(koku_service.get_koku_by_id(_id))


@koku.route('/koku/<_id>/category', methods=['GET'])
def get_koku_categories_by_id(_id):
    return jsonify(koku_service.get_koku_categories_by_id(_id)['categories'])


@koku.route('/koku/<_id>/category/<category_id>', methods=['GET'])
def get_koku_categories_items_by_id(_id, category_id):
    return jsonify(koku_service.get_koku_categories_by_id(_id)['categories'])
