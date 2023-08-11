from flask import Flask
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
