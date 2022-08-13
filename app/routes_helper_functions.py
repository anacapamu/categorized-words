from flask import jsonify, abort, make_response
from .models.category import Category
from .models.word import Word

def error_message(message, status_code):
    abort(make_response(jsonify(dict(details=message)), status_code))

def validate_model(model, id):
    if model == Category:
        model_name = "Category"
    elif model == Word:
        model_name = "Word"

    try:
        id = int(id)
    except:
        error_message(f"{model_name} #{id} is invalid", 400)

    model_instance = model.query.get(id)

    if not model_instance:
        error_message(f"{model_name} #{id} is not found", 404)

    return model_instance