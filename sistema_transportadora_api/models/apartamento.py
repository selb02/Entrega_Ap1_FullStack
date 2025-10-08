from extensions import db

class Apartamento(db.Model):
    __tablename__ = "apartamentos"
    numero_ap = db.Column(db.String(20), primary_key=True)
    status = db.Column(db.Boolean, nullable=False, default=True)

    moradores = db.relationship("Morador", back_populates="apartamento")
    contas = db.relationship("Conta", back_populates="apartamento")

    def to_dict(self):
        return {"numero_ap": self.numero_ap, "status": self.status}
