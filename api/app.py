import time
from flask import Flask, g
from flask_cors import CORS
from main.routes import api_routes_bp
from infra.logs import register_log

app = Flask(__name__)
CORS(app)

app.register_blueprint(api_routes_bp)


@app.before_request
def start_timer():
    g.start = time.time()


@app.after_request
def log_request(response):
    response = register_log.log_request(response)
    return response


if __name__ == "__main__":
    app.run(debug=True, port=int(8003), host="0.0.0.0")

