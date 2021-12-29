import os

from flask import Flask

from flask_login import LoginManager
from flask_session import Session

from database import db, Cart

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/adityajoshi/PycharmProjects/Joshi Store/store.db'
app.config['SECRET_KEY'] = os.urandom(32)
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
app.secret_key = os.urandom(40)
# app.config.from_object(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# FOR FIRST TIME, UNCOMMENT THE LINES BELOW

# with app.app_context():
#      db.create_all()
#     for product in product_list:
#         db.session.add(product)
#         db.session.commit()


import routes

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

    # Cart.__table__.drop(db.engine)
    # Cart.__table__.create(db.session.bind, checkfirst=True)
