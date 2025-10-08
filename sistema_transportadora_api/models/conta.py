from extensions import db

class Conta(db.Model):
    __tablename__ = "contas"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    valor = db.Column(db.Float, nullable=False)
    numero_ap = db.Column(db.String(20), db.ForeignKey('apartamentos.numero_ap'), nullable=False)
    cpf_morador = db.Column(db.String(11), db.ForeignKey('moradores.cpf'), nullable=False)
    pendente = db.Column(db.Boolean, default=True)

    apartamento = db.relationship("Apartamento", back_populates="contas")
    morador = db.relationship("Morador", back_populates="contas")

    def to_dict(self):
        return {"id": self.id, "valor": self.valor, "numero_ap": self.numero_ap, "cpf_morador": self.cpf_morador, "pendente": self.pendente}
