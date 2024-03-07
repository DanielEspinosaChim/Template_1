from flask import Flask, jsonify, render_template
from flask_cors import CORS
app = Flask(__name__, static_folder='../frontend/dist', template_folder='../miproyectoHackathon/templates')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/mensaje')
def mensaje():
    return jsonify(mensaje="hola desde flask")

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def render_vue(path):
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)

