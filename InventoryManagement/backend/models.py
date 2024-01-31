from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Supplier(db.Model):
    supplier_id = db.Column(db.Integer, primary_key=True)
    supplier_name = db.Column(db.String(255), nullable=False)
    contact_name = db.Column(db.String(255))
    contact_email = db.Column(db.String(255))
    contact_phone = db.Column(db.String(255))
    address = db.Column(db.String(255))
    products = db.relationship('Product', backref='supplier', lazy=True)
    # Add any other fields relevant to a supplier

class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255), nullable=False)
    stock_quantity = db.Column(db.Integer, default=0)
    price = db.Column(db.Numeric(10, 2))
    sku = db.Column(db.String(50), unique=True)
    description = db.Column(db.Text)
    category = db.Column(db.String(100))
    cost = db.Column(db.Numeric(10, 2))
    reorder_level = db.Column(db.Integer)
    minimum_order_quantity = db.Column(db.Integer)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.supplier_id'))  # Assuming a Supplier model exists
    image_url = db.Column(db.String(255))
    creation_date = db.Column(db.DateTime, default=datetime.utcnow)
    last_updated_date = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    class Sale(db.Model):
        sale_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'), nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.supplier_id'), nullable=True)  # Optional
    quantity = db.Column(db.Integer, nullable=False)
    sale_date = db.Column(db.DateTime, default=datetime.utcnow)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.customer_id'), nullable=True)  # If you have a Customer model
    price_per_unit = db.Column(db.Numeric(10, 2))
    # Add any additional fields as necessary

    product = db.relationship('Product', backref=db.backref('sales', lazy=True))
    supplier = db.relationship('Supplier', backref=db.backref('sales', lazy=True))  # If tracking suppliers in sales