from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/collaborate', methods=['POST'])
def collaborate_on_document():
    data = request.get_json()
    document_id = data['document_id']
    # Lógica para colaborar en el documento
    return jsonify({'message': 'Collaboration successful'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)