from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api")
def api():
    return jsonify({'data':None})

if __name__ == "__main__":
    app.run(port=4000, debug=True)