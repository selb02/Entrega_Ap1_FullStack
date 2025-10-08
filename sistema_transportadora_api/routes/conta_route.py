from flask import Blueprint, request, jsonify
from extensions import db
from models.conta import Conta
from models.morador import Morador
from models.apartamento import Apartamento

bp = Blueprint('conta', __name__)

@bp.route('/', methods=['POST'])
def create_conta():
    """Cria uma conta. JSON: valor, numero_ap, cpf_morador, pendente (true/false)"""
    data = request.get_json() or {}
    valor = data.get('valor')
    numero_ap = data.get('numero_ap')
    cpf_morador = data.get('cpf_morador')
    pendente = bool(data.get('pendente', True))
    if valor is None or not numero_ap or not cpf_morador:
        return jsonify({'error': 'valor, numero_ap e cpf_morador são obrigatórios'}), 400
    # simple integrity checks
    if not Apartamento.query.get(numero_ap):
        return jsonify({'error': 'Apartamento não existe'}), 400
    if not Morador.query.get(cpf_morador):
        return jsonify({'error': 'Morador não existe'}), 400
    c = Conta(valor=valor, numero_ap=numero_ap, cpf_morador=cpf_morador, pendente=pendente)
    db.session.add(c)
    db.session.commit()
    return jsonify(c.to_dict()), 201

@bp.route('/', methods=['GET'])
def list_contas():
    """Lista contas."""
    items = Conta.query.all()
    return jsonify([i.to_dict() for i in items])

@bp.route('/<int:id>', methods=['GET'])
def get_conta(id):
    """Retorna conta por ID."""
    c = Conta.query.get(id)
    if not c:
        return jsonify({'error': 'Não encontrado'}), 404
    return jsonify(c.to_dict())

@bp.route('/<int:id>', methods=['PUT'])
def update_conta(id):
    """Atualiza conta."""
    c = Conta.query.get(id)
    if not c:
        return jsonify({'error': 'Não encontrado'}), 404
    data = request.get_json() or {}
    c.valor = data.get('valor', c.valor)
    c.pendente = bool(data.get('pendente', c.pendente))
    db.session.commit()
    return jsonify(c.to_dict())

@bp.route('/<int:id>', methods=['DELETE'])
def delete_conta(id):
    """Remove conta."""
    c = Conta.query.get(id)
    if not c:
        return jsonify({'error': 'Não encontrado'}), 404
    db.session.delete(c)
    db.session.commit()
    return '', 204
