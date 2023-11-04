from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data - You can replace this with a database or any data store.
data = {}
not_found_msg = "Record not found"
# Create operation
@app.route('/create', methods=['POST'])
def create():
    request_data = request.get_json()
    key = request_data.get('key')
    value = request_data.get('value')
    data[key] = value
    return jsonify({"message": "Record created successfully", "data": data})

# Read operation
@app.route('/read/<key>', methods=['GET'])
def read(key):
    if key in data:
        return jsonify({key: data[key]})
    return jsonify({"message": not_found_msg, "data": data})

# Update operation
@app.route('/update/<key>', methods=['PUT'])
def update(key):
    if key in data:
        request_data = request.get_json()
        data[key] = request_data.get('value')
        return jsonify({"message": "Record updated successfully", "data": data})
    return jsonify({"message": not_found_msg, "data": data})

# Delete operation
@app.route('/delete/<key>', methods=['DELETE'])
def delete(key):
    if key in data:
        del data[key]
        return jsonify({"message": "Record deleted successfully", "data": data})
    return jsonify({"message": not_found_msg, "data": data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
