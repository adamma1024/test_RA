from flask import Flask
from flask_cors import CORS
from routes.user_routes import user_bp
from routes.post_routes import post_bp

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

app.register_blueprint(user_bp)
app.register_blueprint(post_bp)

if __name__ == '__main__':
    app.run(debug=True)
