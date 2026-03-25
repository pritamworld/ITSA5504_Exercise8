from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="ok"), 200

@app.route("/")
def hello():
    return jsonify(message="hello, world"), 200

@app.route("/greet")
def greet():
    return jsonify(message="Welcome to Docker and GitHub Action"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
