from models.categories_model import CategoriesModel
from db import db

class CategoriesController:
    
    def create(self, data):
        try:
            record = CategoriesModel(data.get('name'))
            db.session.add(record)
            db.session.commit()
            return record.convertToJson()
        except Exception as e:
            return {
                'message': str(e)
            }
    
    def list(self):
        try:
            records = CategoriesModel.query.all()
            response = []
            for record in records:
                response.append(record.convertToJson())
            return response
        except Exception as e:
            return {
                'message': str(e)
            }