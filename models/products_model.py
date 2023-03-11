from sqlalchemy import Column, Integer, String, Text, Float, Boolean, ForeignKey
from db import db


class ProductsModel(db.Model):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    description = Column(Text)
    price = Column(Float)
    image = Column(Text)
    stock = Column(Integer)
    category_id = Column(Integer, ForeignKey('categories.id'))
    status = Column(Boolean, default=True)

    def __init__(self, name, description, price, image, stock, cat_id):
        self.name = name
        self.description = description
        self.price = price
        self.image = image
        self.stock = stock
        self.category_id = cat_id

    def convertToJson(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'image': self.image,
            'stock': self.stock,
            'category_id': self.category_id
        }