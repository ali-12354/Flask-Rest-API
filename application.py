from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f"{self.name} - {self.description}"

@app.route('/')
def index():
    return "Hello from API 1!"

@app.route('/drinks', methods=['GET'])
def get_drinks():
    drinks_list = Drink.query.all()
    output = []
    for drink in drinks_list:
        drink_data = {'name': drink.name, 'description': drink.description}
        output.append(drink_data)
    return jsonify({'drinks': output})

@app.route('/drinks/<int:id>', methods=['GET'])
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    return jsonify({'name': drink.name, 'description': drink.description})

@app.route('/drinks', methods=['POST'])
def add_drink():
    drink_data = request.get_json()
    new_drink = Drink(
        name=drink_data['name'],
        description=drink_data.get('description')
    )
    db.session.add(new_drink)
    db.session.commit()
    return jsonify({'id': new_drink.id}), 201

@app.route('/drinks/<int:id>', methods=['DELETE'])
def delete_drink(id):
    drink = Drink.query.get_or_404(id)
    if drink is None:
        return jsonify({'message': 'Drink not found'}), 404
    db.session.delete(drink)
    db.session.commit()
    return jsonify({'message': 'Drink deleted'})

if __name__ == "__main__":
    # Create tables if they don't exist
    with app.app_context():
        db.create_all()

    print("Registered routes:")
    for rule in app.url_map.iter_rules():
        print(rule, rule.methods)

    app.run(debug=True)