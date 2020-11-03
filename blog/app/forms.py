import flask_wtf
import wtforms
from wtforms import validators as vld

class SignupForm(flask_wtf.FlaskForm):

    username = wtforms.StringField("Username", validators=[vld.DataRequired()])
    password = wtforms.PasswordField("Password", validators=[vld.DataRequired()])

    submit   = wtforms.SubmitField("Sign up")

class SigninForm(flask_wtf.FlaskForm):

    username = wtforms.StringField("Username", validators=[vld.DataRequired()])
    password = wtforms.PasswordField("Password", validators=[vld.DataRequired()])
    submit   = wtforms.SubmitField("Sign in")


class QueryForm(flask_wtf.FlaskForm):

    query = wtforms.StringField("",render_kw={"placeholder": "Search for a product"})
                             

class SelectForm(flask_wtf.FlaskForm):

    categories = wtforms.SelectField("selectedCategory",
    choices= [("Dairy","Dairy"),("Technology","Technology"),("Health & Beauty","Health & Beauty")
    ,("Beverages","Beverages"),  ("Paper Products","Paper Products")])
    submit  = wtforms.SubmitField("Search")


