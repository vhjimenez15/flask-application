# from datetime import datetime
from app import db
import random


class ElementsToProcess(db.Model):
    __tablename__ = 'ElementsToProcess'

    id = db.Column(db.Integer, primary_key=True)
    idBulk = db.Column(db.Integer)
    retries = db.Column(db.Integer, nullable=True)
    status = db.Column(db.Integer)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name, status, retries=0, idBulk=None):
        self.name = name
        self.status = status
        self.retries = retries
        self.idBulk = random.randint(0, 1000) if idBulk is None else idBulk

    def serialize(self):
        return {
            "id": self.id,
            "idBulk": self.idBulk,
            "retries": self.retries,
            "status": self.status,
            "name": self.name
        }


    # created_at = db.Column(
    #     db.DateTime(),
    #     nullable=False,
    #     default=db.func.current_timestamp()
    # )
