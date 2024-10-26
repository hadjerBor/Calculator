from flask import Flask, render_template
from addition import add
from subtraction import subtraction_bp
from multiplication import multiply
from division import division_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(subtraction_bp)
app.register_blueprint(division_bp)

@app.route('/')
def calculator():
    return render_template('index.html')

@app.route('/add/<int:numberA>/<int:numberB>', methods=['GET'])
def add_route(numberA, numberB):
    return add(numberA, numberB)

@app.route('/multiply/<int:numberA>/<int:numberB>', methods=['GET'])
def multiply_route(numberA, numberB):
    return multiply(numberA, numberB)

if __name__ == '__main__':
    app.run(debug=True)
