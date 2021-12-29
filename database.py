from flask_login import UserMixin

from db import db


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    product_name = db.Column(db.String, unique=True, nullable=False)
    price = db.Column(db.FLOAT, nullable=False)
    image_url = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return '<Products %r>' % self.product_name


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Orders(db.Model):
    order_id_default = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    product_id = db.Column(db.Integer, unique=True, nullable=False)
    customer_id = db.Column(db.Integer,  nullable=False)
    date = db.Column(db.DateTime, unique=True, nullable=False)

    def __repr__(self):
        return '<Order %r>' % self.order_id_default


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    product_id = db.Column(db.Integer, nullable=False)
    customer_id = db.Column(db.Integer,  nullable=False)

    def __repr__(self):
        return '<Cart Product %r>' % self.product_id













product_1 = Products(product_name="Life's Amazing Secrets: How to Find Balance and Purpose in Your Life |", price=300,
                     image_url='https://images-na.ssl-images-amazon.com/images/I/51PJyvcfPGL._SX321_BO1,204,203,'
                               '200_.jpg')
product_2 = Products(product_name="Ikigai: The Japanese secret to a long and happy life", price=200,
                     image_url='https://images-na.ssl-images-amazon.com/images/I/51T8OXMiB5L._SX356_BO1,204,203,'
                               '200_.jpg')
product_3 = Products(product_name="Atomic Habits: The life-changing million copy bestseller", price=227,
                     image_url='https://images-na.ssl-images-amazon.com/images/I/51-nXsSRfZL._SX328_BO1,204,203,'
                               '200_.jpg')
product_4 = Products(product_name="The Subtle Art of Not Giving a F*ck: A Counterintuitive Approach to Living a Good "
                                  "Life", price=334,
                     image_url='https://images-na.ssl-images-amazon.com/images/I/516pmXNNmCL._SX324_BO1,204,203,'
                               '200_.jpg')
product_5 = Products(product_name="The Psychology of Money", price=212,
                     image_url='https://images-na.ssl-images-amazon.com/images/I/41r6F2LRf8L._SX323_BO1,204,203,'
                               '200_.jpg')
product_6 = Products(product_name="The Intelligent Investor (English) Paperback", price=421,
                     image_url='https://images-na.ssl-images-amazon.com/images/I/51DLoxAJ68L._SX324_BO1,204,203,'
                               '200_.jpg')

product_list = [product_1, product_2, product_3, product_4, product_5, product_6]

