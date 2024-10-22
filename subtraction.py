from flask import Blueprint, jsonify

subtraction_bp = Blueprint('subtraction', name)

@subtraction_bp.route('/minus/<float:A>/<float:B>', methods=['GET'])
def minus(A, B):
    result = A - B
    return jsonify({'status': 200, 'result': result})