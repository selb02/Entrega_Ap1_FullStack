from flask import Blueprint, request, jsonify
from extensions import db
from models.morador import Morador
from models.apartamento import Apartamento

bp = Blueprint('morador', __name__)

@bp.route('/', methods=['POST'])
def create_morador():
    """Cria um morador.
    Recebe JSON com: cpf, nome, numero_ap
    """
    data = request.get_json() or {}
    cpf = data.get('cpf')
    nome = data.get('nome')
    numero_ap = data.get('numero_ap')
    if not cpf or not nome or not numero_ap:
        return jsonify({'error': 'cpf, nome e numero_ap são obrigatórios'}), 400
    if Morador.query.get(cpf):
        return jsonify({'error': 'Morador já existe'}), 400
    if not Apartamento.query.get(numero_ap):
        return jsonify({'error': 'Apartamento não existe'}), 400
    m = Morador(cpf=cpf, nome=nome, numero_ap=numero_ap)
    db.session.add(m)
    db.session.commit()
    return jsonify(m.to_dict()), 201

@bp.route('/', methods=['GET'])
def list_moradores():
    """Lista todos os moradores."""
    items = Morador.query.all()
    return jsonify([i.to_dict() for i in items])

@bp.route('/<cpf>', methods=['GET'])
def get_morador(cpf):
    """Retorna um morador pelo CPF."""
    m = Morador.query.get(cpf)
    if not m:
        return jsonify({'error': 'Não encontrado'}), 404
    return jsonify(m.to_dict())

@bp.route('/<cpf>', methods=['PUT'])
def update_morador(cpf):
    """Atualiza um morador."""
    m = Morador.query.get(cpf)
    if not m:
        return jsonify({'error': 'Não encontrado'}), 404
    data = request.get_json() or {}
    m.nome = data.get('nome', m.nome)
    m.numero_ap = data.get('numero_ap', m.numero_ap)
    db.session.commit()
    return jsonify(m.to_dict())

@bp.route('/<cpf>', methods=['DELETE'])
def delete_morador(cpf):
    """Remove um morador."""
    m = Morador.query.get(cpf)
    if not m:
        return jsonify({'error': 'Não encontrado'}), 404
    db.session.delete(m)
    db.session.commit()
    return '', 204
