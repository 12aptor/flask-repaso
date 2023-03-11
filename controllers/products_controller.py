from models.products_model import ProductsModel
from db import db

class ProductsController:
    
    def list(self):
        records = ProductsModel.query.all()
        print(records)
        response = []
        for record in records:
            response.append(record.convertToJson())
        return response
    
    def create(self, data):
        record = ProductsModel(
            data['name'],
            data['description'],
            data['price'],
            data['image'],
            data['stock'],
            data['category_id']
        )
        db.session.add(record)
        db.session.commit()
        return record.convertToJson()