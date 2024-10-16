from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/json', methods=['GET'])
def get_json():
    return jsonify({"message": "Hello from Flask!"})

@app.route('/convert', methods=['POST'])
def convert_to_json():
    data = request.get_json()  # Get JSON data from request
    return jsonify(data)  # Return the received data as JSON

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
