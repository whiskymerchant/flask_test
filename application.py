from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
db = SQLAlchemy(app)


class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    purchase_date = db.Column(db.Date)
    original_cost = db.Column(db.Integer)
    depriciated_cost = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.name} - {self.description} - {self.purchase_date} - {self.original_cost} - {self.depriciated_cost}'

@app.route('/')
def index():
    return 'Hello, world'


@app.route('/items')
def get_items():
    items = Items.query.all()
    output = []
    for item in items:
        item_data = {
            'name': item.name, 
            'description': item.description, 
            'purchase_date': item.purchase_date, 
            'original_cost': item.original_cost, 
            'depricated_cost': item.deprecated_cost,
            }
        output.append(item_data)
    return {'items': output}


@app.route('/items/<id>')
def get_item(id):
    item = Items.query.get_or_404(id)
    return {
        'name': item.name,
        'description': item.description,
        'purchase_date': item.purchase_date,
        'original_cost': item.original_cost,
        'depricated_cost': item.deprecated_cost,
        }


@app.route('/items', methods=['POST'])
def add_item():
    item = Items(
      name=request.json['name'],
      description=request.json['description'],
      purchase_date=request.json['purchase_date'],
      original_cost=request.json['original_cost'],
      depreciated_cost=request.json['depreciated_cost'],
      )
    db.session.add(item)
    db.session.commit()
    return {'id': item.id}

""""
{
    "name": "Chair",
    "description": "Soft wooden chair with armrest painted in oak",
    "purchase_date": "15.06.2021",
    "original_cost": "6000",
    "depricated_cost": "5000"
}
"""