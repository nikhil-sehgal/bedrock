from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>🌍 Simple Map Server</h2>
    <p>Static map tiles served from /tiles/ directory.</p>
    """

@app.route("/tiles/<path:filename>")
def tiles(filename):
    return send_from_directory("tiles", filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
