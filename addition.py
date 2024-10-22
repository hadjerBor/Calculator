from flask import jsonify

def add(A, B):
    result = A + B
    return jsonify({'status': 200, 'result': result})
