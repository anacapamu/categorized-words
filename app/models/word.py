from app import db

class Word(db.Model):
    word_id = db.Column(db.Integer, primary_key=True, nullable=False)
    word = db.Column(db.String, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'))
    category = db.relationship("Category", back_populates="words")

    def to_dict(self):
        return dict(
            id = self.word_id,
            word = self.word,
            category_id = self.category_id
        )