from sqlalchemy import Column, Integer, String, Boolean
from db import db


class CategoriesModel(db.Model):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45))
    status = Column(Boolean, default=True)


    def __init__(self, name):
        self.name = name

    def convertToJson(self):
        return {
          'id': self.id,
          'name': self.name,
          'status': self.status
        }