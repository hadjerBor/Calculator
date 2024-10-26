from flask import jsonify


@app.route('/add/<int:num1>/<int:num2>', methods=['GET'])
def add(num1, num2):
    result = num1 + num2
    return jsonify({'status': 200, 'result': result})
