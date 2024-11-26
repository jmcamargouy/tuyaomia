from flask import Flask, request, jsonify

app = Flask(__name__)

agreements = []  # Lista temporal para acuerdos

@app.route('/')
def home():
    return "Bienvenido a Tuyaomia!"

@app.route('/create_agreement', methods=['POST'])
def create_agreement():
    data = request.json
    agreements.append(data)
    return jsonify({"message": "Acuerdo creado!", "agreement": data}), 201

@app.route('/list_agreements', methods=['GET'])
def list_agreements():
    return jsonify(agreements), 200

if __name__ == '__main__':
    app.run(debug=True)
