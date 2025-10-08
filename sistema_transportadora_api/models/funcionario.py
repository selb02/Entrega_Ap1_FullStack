from extensions import db

class Funcionario(db.Model):
    __tablename__ = "funcionarios"
    cpf = db.Column(db.String(11), primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    registro = db.Column(db.String(50), nullable=True)
    cargo = db.Column(db.String(80), nullable=True)
    salario = db.Column(db.Float, nullable=True)

    def to_dict(self):
        return {"cpf": self.cpf, "nome": self.nome, "registro": self.registro, "cargo": self.cargo, "salario": self.salario}
