from flask import Blueprint, request, jsonify
from extensions import db
from models.funcionario import Funcionario

bp = Blueprint('funcionario', __name__)

@bp.route('/', methods=['POST'])
def create_funcionario():
    """Cria um funcionário. JSON: cpf, nome, registro, cargo, salario"""
    data = request.get_json() or {}
    cpf = data.get('cpf')
    nome = data.get('nome')
    if not cpf or not nome:
        return jsonify({'error':'cpf e nome obrigatórios'}), 400
    if Funcionario.query.get(cpf):
        return jsonify({'error':'Funcionário já existe'}), 400
    f = Funcionario(cpf=cpf, nome=nome, registro=data.get('registro'), cargo=data.get('cargo'), salario=data.get('salario'))
    db.session.add(f)
    db.session.commit()
    return jsonify(f.to_dict()), 201

@bp.route('/', methods=['GET'])
def list_funcionarios():
    """Lista funcionários."""
    items = Funcionario.query.all()
    return jsonify([i.to_dict() for i in items])

@bp.route('/<cpf>', methods=['GET'])
def get_funcionario(cpf):
    """Retorna funcionário por CPF."""
    f = Funcionario.query.get(cpf)
    if not f:
        return jsonify({'error':'Não encontrado'}), 404
    return jsonify(f.to_dict())

@bp.route('/<cpf>', methods=['PUT'])
def update_funcionario(cpf):
    """Atualiza funcionário."""
    f = Funcionario.query.get(cpf)
    if not f:
        return jsonify({'error':'Não encontrado'}), 404
    data = request.get_json() or {}
    f.nome = data.get('nome', f.nome)
    f.registro = data.get('registro', f.registro)
    f.cargo = data.get('cargo', f.cargo)
    f.salario = data.get('salario', f.salario)
    db.session.commit()
    return jsonify(f.to_dict())

@bp.route('/<cpf>', methods=['DELETE'])
def delete_funcionario(cpf):
    """Remove funcionário."""
    f = Funcionario.query.get(cpf)
    if not f:
        return jsonify({'error':'Não encontrado'}), 404
    db.session.delete(f)
    db.session.commit()
    return '', 204
