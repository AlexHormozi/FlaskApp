from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/json', methods=['GET'])
def get_json():
    return jsonify({"message": "Hello from Flask!"})

@app.route('/convert', methods=['POST'])
def convert_to_json():
    data = request.get_json()  # Get JSON data from request
    return jsonify(data)  # Return the received data as JSON

@app.route('/text-to-json', methods=['POST'])
def text_to_json():
    # Get the plain text input from the request
    text_data = request.data.decode('utf-8').strip()
    json_structure = parse_text_to_json(text_data)
    return jsonify(json_structure)

def parse_text_to_json(text):
    lines = text.splitlines()
    
    if not lines or not lines[0].strip():
        return {"name": "Root", "children": []}  # Handle empty input

    root = {"name": "Root", "children": []}
    stack = [(root, 0)]  # Stack to manage parent-child relationships

    for line in lines:
        level = len(line) - len(line.lstrip())  # Determine indentation level
        name = line.strip()

        if not name:  # Skip empty lines
            continue

        node = {"name": name, "children": []}

        # Adjust the current parent based on indentation level
        while stack and stack[-1][1] >= level:
            stack.pop()

        if stack:
            stack[-1][0]["children"].append(node)
        else:
            root["children"].append(node)

        stack.append((node, level))

    return root

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
