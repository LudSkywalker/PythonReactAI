from flask import Flask, jsonify, request
from flask_cors import CORS
import fullConected

fullConected.create()
app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'application/json'

@app.route("/api")
def api():
    return jsonify({'data':None})

@app.route("/dense",methods=['POST'])
def dense():
    xy=request.json["XY"]
    z=request.json["Z"]
    y=fullConected.graph(xy,z)
    return jsonify({'y':y})

if __name__ == "__main__":
    app.run(port=4000, debug=True)