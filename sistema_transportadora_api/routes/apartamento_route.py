from flask import Blueprint, request, jsonify
from extensions import db
from models.apartamento import Apartamento

bp = Blueprint('apartamento', __name__)

@bp.route('/', methods=['POST'])
def create_apartamento():
    """Cria um apartamento. JSON: numero_ap, status (true/false)"""
    data = request.get_json() or {}
    numero = data.get('numero_ap')
    status = data.get('status', True)
    if not numero:
        return jsonify({'error': 'numero_ap obrigatório'}), 400
    if Apartamento.query.get(numero):
        return jsonify({'error': 'Apartamento já existe'}), 400
    a = Apartamento(numero_ap=numero, status=bool(status))
    db.session.add(a)
    db.session.commit()
    return jsonify(a.to_dict()), 201

@bp.route('/', methods=['GET'])
def list_apartamentos():
    """Lista apartamentos."""
    items = Apartamento.query.all()
    return jsonify([i.to_dict() for i in items])

@bp.route('/<numero_ap>', methods=['GET'])
def get_apartamento(numero_ap):
    """Retorna apartamento por numero."""
    a = Apartamento.query.get(numero_ap)
    if not a:
        return jsonify({'error': 'Não encontrado'}), 404
    return jsonify(a.to_dict())

@bp.route('/<numero_ap>', methods=['PUT'])
def update_apartamento(numero_ap):
    """Atualiza apartamento."""
    a = Apartamento.query.get(numero_ap)
    if not a:
        return jsonify({'error': 'Não encontrado'}), 404
    data = request.get_json() or {}
    a.status = bool(data.get('status', a.status))
    db.session.commit()
    return jsonify(a.to_dict())

@bp.route('/<numero_ap>', methods=['DELETE'])
def delete_apartamento(numero_ap):
    """Remove apartamento."""
    a = Apartamento.query.get(numero_ap)
    if not a:
        return jsonify({'error': 'Não encontrado'}), 404
    db.session.delete(a)
    db.session.commit()
    return '', 204
