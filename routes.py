import os

import stripe
from flask import render_template, redirect, url_for, flash, request, abort, session
from flask_login import login_required, logout_user, login_user, current_user
from database import Users, Cart
from app import app, login_manager
from database import Products
from db import db
from loginform import LoginForm, Register
import json

YOUR_DOMAIN='http://127.0.0.1:5000'

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


@app.route('/')
def home():  # put application's code here
    products = Products.query.all()
    # if len(json.loads(session.get('allCartEntries')))> 0 :
    #     cart_count =len(session.get('allCartEntries'))
    return render_template('index.html', products=products, )


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user.password != form.password.data:
            flash('Wrong Password')
        else:
            login_user(user)
            flash('Logged in successfully.')
            return redirect(url_for('home'))
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Register()
    print(form.password.data)
    if form.validate_on_submit():
        print(form.email.data)
        user = Users(email=form.email.data, password=form.password.data, username=form.username.data)
        db.session.add(user)
        db.session.commit()
        load_user(user.id)
        login_user(user)
        flash('Account Created Successfully')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/cart")
def cart():
    cart_items = Cart.query.all()

    # print(cart_items,cart_items.customer_id)
    print(current_user.id,type(current_user.id))
    current_user_cart = [Products.query.get(int(item.product_id)) for item in cart_items
                         if int(item.customer_id) == int(current_user.id)]
    return render_template('cart.html', cart_items=current_user_cart)


@app.route('/addtocart/<int:product_id>', methods=['GET', 'POST'])
def add_to_cart(product_id):
    if current_user.is_authenticated:
        print(current_user.id)
        item = Cart(product_id=product_id, customer_id=current_user.id)
        db.session.add(item)
        db.session.commit()
        flash('Product added to cart')
    else:
        redirect(url_for('register'))
        # existingCartEntries = json.loads(session.get('allCartEntries'))
        # flash('Product added to cart')
        # if existingCartEntries is None:
        #     existingCartEntries = []
        #
        # product = Products.query.get(product_id)
        # cart_item = {
        #     "title": product.product_name,
        #     "id": product.id
        # }
        # session['cart_item'] = json.dumps(cart_item)
        # existingCartEntries.push(cart_item)
        # session['allCartEntries'] = json.dumps(existingCartEntries)

    return redirect(url_for('home'))


@app.route('/create-checkout-session/<int:product_id>', methods=['GET','POST'])
def create_checkout_session(product_id):
    stripe.api_key = os.environ['stripe_api_key']

    try:
        product = Products.query.get(product_id)
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    "name": product.product_name,
                    "quantity": 1,
                    "currency": "inr",
                    "amount": int(product.price),
                }
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success',
            cancel_url=YOUR_DOMAIN + '/cancel',
        )
    except Exception as e:
        return str(e)
    print(checkout_session.url)
    return redirect(checkout_session.url)


@app.route("/success")
def success():
    return render_template('success.html')

@app.route("/cancel")
def cancel():
    return render_template('cancel.html')

