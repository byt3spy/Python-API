from flask import Blueprint, jsonify, request
from app import db, auth
from models import Item

# Create a blueprint for item routes
item_bp = Blueprint('item_bp', __name__)

# Route to get all items
@item_bp.route('/', methods=['GET'])
@auth.login_required
def get_items():
    items = Item.query.all()
    return jsonify([{"id": item.id, "name": item.name, "description": item.description} for item in items])

# Route to get a specific item by ID
@item_bp.route('/<int:item_id>', methods=['GET'])
@auth.login_required
def get_item(item_id):
    item = Item.query.get_or_404(item_id)
    return jsonify({"id": item.id, "name": item.name, "description": item.description})

# Route to create a new item
@item_bp.route('/', methods=['POST'])
@auth.login_required
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error": "Bad request"}), 400
    new_item = Item(name=request.json['name'], description=request.json.get('description', ""))
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"id": new_item.id, "name": new_item.name, "description": new_item.description}), 201

# Route to update an existing item by ID
@item_bp.route('/<int:item_id>', methods=['PUT'])
@auth.login_required
def update_item(item_id):
    item = Item.query.get_or_404(item_id)
    if not request.json:
        return jsonify({"error": "Bad request"}), 400
    item.name = request.json.get('name', item.name)
    item.description = request.json.get('description', item.description)
    db.session.commit()
    return jsonify({"id": item.id, "name": item.name, "description": item.description})

# Route to delete an item by ID
@item_bp.route('/<int:item_id>', methods=['DELETE'])
@auth.login_required
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({"result": True})
