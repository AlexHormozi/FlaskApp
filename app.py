from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/json', methods=['GET'])
def get_json():
    return jsonify({"message": "Hello from Flask!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)  # Use port 3000 for Replit
