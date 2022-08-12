from app import db

class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True, nullable=False)
    category = db.Column(db.String, nullable=False)
    words = db.relationship("Word", back_populates="category")

    def to_dict(self):
        return dict(
            id = self.category_id,
            category = self.category,
        )