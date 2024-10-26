from flask import Blueprint, jsonify

# Define the Blueprint
division_bp = Blueprint('division', __name__)


def divide(A, B):
    print(f"Received request to divide {A} by {B}")  # Debug print
    if B == 0:
        return jsonify({'status': 400, 'result': 'Division by zero error'})
    result = A / B
    return jsonify({'status': 200, 'result': result})
