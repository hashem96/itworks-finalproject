import flask_login
import werkzeug
from sqlalchemy.ext.hybrid import hybrid_property

from . import db
from .utils import ModelMixin

class Product(db.Model): 
    id =db.Column(db.Integer(), primary_key=True) 
    name=db.Column(db.String(64))
    price= db.Column(db.Float())
    image=db.Column(db.String())
    category= db.Column(db.String(64))

# class Cart(db.Model): 
#     product_id = db.Column(db.Integer, db.ForeignKey("Product.id"))
#     user_name = db.Column(db.String, db.ForeignKey("User.name"))
#     product_name=db.Column(db.String(64))
#     product_price=db.Column(db.Float())
#     product_price_per_quantity = db.Column(db.Float())
#     product_quantity = db.Column(db.String(64))

# class Purchases(db.Model): 
#     id =db.Column(db.Integer(), primary_key=True) 
#     user_name=db.Column(db.String(64))
#     total_price=db.Column(db.Float())


class User(db.Model, ModelMixin, flask_login.UserMixin): 

    name= db.Column(db.String(64), nullable=False)
    _password_hash= db.Column(db.String(256))

    @classmethod
    def login_user(cls, name, pwd):
        user = cls.query.filter_by(name=name).first()
        if user and user.check_password(pwd):
            flask_login.login_user(user)
            return user
        return False

    @hybrid_property
    def password(self):
        return self._password_hash

    @password.setter
    def password(self, pwd):
        self._password_hash = werkzeug.security.generate_password_hash(pwd)

    def check_password(self, pwd):
        return werkzeug.security.check_password_hash(self._password_hash, pwd)

    def __repr__(self):
        return f"<User {self.id}-{self.name}>"

