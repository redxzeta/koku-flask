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


@koku.route('/koku/<_id>/category/<_category_id>', methods=['GET'])
def get_item_of_category_by_id(_id, _category_id):
    return jsonify(koku_service.get_item_of_category_by_id(_id, _category_id))


@koku.route('/koku/<_id>/category/<_category_id>/picture', methods=['PUT'])
def update_category_picture(_id, _category_id):
    return jsonify(koku_service.update_category_picture(_id, _category_id))


@koku.route('/koku/<_id>/category/<_category_id>/<update_type>', methods=['PUT'])
def update_type(_id, _category_id, update_type):
    key = request.get_json()[update_type]
    print(key)
    return jsonify(koku_service.get_kokus())


@koku.route('/koku/<_id>/category/<_category_id>/item/remove', methods=['PUT'])
def delete_list_of_items(_id, _category_id):
    obj = request.get_json()
    return jsonify(koku_service.remote_list_of_items(_id, _category_id, obj['items']))
