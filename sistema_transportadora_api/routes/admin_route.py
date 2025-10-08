from flask import Blueprint, request, jsonify
from extensions import db
from models.admin import Admin

bp = Blueprint('admin', __name__)

@bp.route('/', methods=['POST'])
def create_admin():
    """Cria um admin (username,password)."""
    data = request.get_json() or {}
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'username e password são obrigatórios'}), 400
    if Admin.query.get(username):
        return jsonify({'error': 'Admin já existe'}), 400
    a = Admin(username=username, password=password)
    db.session.add(a)
    db.session.commit()
    return jsonify(a.to_dict()), 201

@bp.route('/', methods=['GET'])
def list_admins():
    """Lista admins (apenas usernames)."""
    items = Admin.query.all()
    return jsonify([i.to_dict() for i in items])

@bp.route('/<username>', methods=['DELETE'])
def delete_admin(username):
    """Remove admin."""
    a = Admin.query.get(username)
    if not a:
        return jsonify({'error': 'Não encontrado'}), 404
    db.session.delete(a)
    db.session.commit()
    return '', 204
