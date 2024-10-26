from flask import Blueprint, jsonify

subtraction_bp = Blueprint('subtraction', name)


def minus(A, B):
    result = A - B
    return jsonify({'status': 200, 'result': result})
