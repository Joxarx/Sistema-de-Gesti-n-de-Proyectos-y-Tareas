from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/integrate', methods=['POST'])
def integrate_with_calendar():
    data = request.get_json()
    calendar_id = data['calendar_id']
    # Lógica para integrar con el calendario
    return jsonify({'message': 'Integration successful'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)