from flask import Flask, request, jsonify
import os

app = Flask(teams.microsoft)

@app.route('/delete-file', methods=['POST'])
def delete_file():
    # Extract filename from the request
    data = request.json
    filename = data.get('filename')
    file_path = os.path.join('path/to/files', filename)

    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            return jsonify({"message": "File has been deleted."}), 200
        except Exception as e:
            return jsonify({"error": f"Error deleting file: {e}"}), 500
    else:
        return jsonify({"error": "File does not exist."}), 404

if __name__ == '__main__':
    app.run(debug=True)
