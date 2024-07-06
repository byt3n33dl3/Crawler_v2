from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from validation import validate_user_input
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webapp.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

@app.route('/register', methods=['POST'])
def register():
    username = request.json.get('username')
    password = request.json.get('password')
    
    if not validate_user_input(username, password):
        return jsonify({"error": "Invalid input"}), 400

    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=os.getenv('PORT', 5000))
