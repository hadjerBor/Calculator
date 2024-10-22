# app.py

from flask import Flask
from division import division_bp  # Import the division blueprint

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(division_bp)

if __name__ == '__main__':
    app.run(debug=True)
