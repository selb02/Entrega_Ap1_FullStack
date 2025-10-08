from extensions import db

class Admin(db.Model):
    __tablename__ = "admins"
    username = db.Column(db.String(80), primary_key=True)
    password = db.Column(db.String(120), nullable=False)

    def to_dict(self):
        return {"username": self.username}
