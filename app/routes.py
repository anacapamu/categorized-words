from flask import Blueprint, request, jsonify
from .models.category import Category
from .models.word import Word
from .routes_helper_functions import *
from app import db

category_bp = Blueprint("categories", __name__, url_prefix="/categories")
word_bp = Blueprint("words", __name__, url_prefix="/words")

@category_bp.route("", methods=("POST",))
def post_one_category():
    request_body = request.get_json()

    try:
        new_category = Category(category=request_body["category"])
    except KeyError as err:
        error_message(f"missing required {err}", 400)

    db.session.add(new_category)
    db.session.commit()

    return jsonify(new_category.to_dict()), 201

@category_bp.route("", methods=("GET",))
def get_categories():

    categories = Category.query.all()

    result = [category.to_dict() for category in categories]

    return jsonify(result), 200

@category_bp.route("/<category_id>/words", methods=("POST",))
def post_one_word_to_category(category_id):
    request_body = request.get_json()

    validate_model(Category, category_id)

    try:
        new_word = Word(word=request_body["word"], category_id=category_id)
    except KeyError as err:
        error_message(f"missing required {err}", 400)

    db.session.add(new_word)
    db.session.commit()

    return jsonify(new_word.to_dict()), 201

@category_bp.route("/<category_id>/words", methods=("GET",))
def get_words_of_category(category_id):
    category = validate_model(Category, category_id)
    words_dict = [word.word for word in category.words]

    result = category.to_dict()
    result["words"] = words_dict

    return jsonify(result), 200

@category_bp.route("/<category_id>", methods=("DELETE",))
def delete_one_category(category_id):
    category = validate_model(Category, category_id)

    db.session.delete(category)
    db.session.commit()

    return make_response(jsonify(dict(details=f'Category #{category.category_id} "{category.category}" successfully deleted'))), 200

@word_bp.route("", methods=("GET",))
def get_words():

    words = Word.query.all()

    result = [word.to_dict() for word in words]

    return jsonify(result), 200

@word_bp.route("/<word_id>", methods=("DELETE",))
def delete_one_word(word_id):
    word = validate_model(Word, word_id)

    db.session.delete(word)
    db.session.commit()

    return make_response(jsonify(dict(details=f'Word #{word.word_id} "{word.word}" successfully deleted'))), 200