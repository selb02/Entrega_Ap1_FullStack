from extensions import db

class Morador(db.Model):
    __tablename__ = "moradores"
    cpf = db.Column(db.String(11), primary_key=True)
    nome = db.Column(db.String(120), nullable=False)
    numero_ap = db.Column(db.String(20), db.ForeignKey('apartamentos.numero_ap'), nullable=False)

    apartamento = db.relationship("Apartamento", back_populates="moradores")
    contas = db.relationship("Conta", back_populates="morador")

    def to_dict(self):
        return {"cpf": self.cpf, "nome": self.nome, "numero_ap": self.numero_ap}
