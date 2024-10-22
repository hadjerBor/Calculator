from flask import Flask
from devision import division_bp  # Ensure this matches the filename

app = Flask(__name__)

# Register the blueprint
app.register_blueprint(division_bp)

if __name__ == '__main__':
    app.run(debug=True)  # Run in debug mode
