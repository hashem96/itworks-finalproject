from operator import concat
import flask, flask_login
from . import app, db
from . import forms
from flask import request , session

from .models import User,Product

from decimal import Decimal

from datetime import date


# def add_Products():
#     #adding products to database 
# product=Product(name="Wet Wipes", price=1.5,image ="/static/images/wet-wipes.jpg",category="Paper Products")
#     product=Product(name="Macbook Pro", price=1000.99,category="technology")

#     db.session.add(product)
#     db.session.commit()

checkoutProducts = []

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def index():
    query_form = forms.QueryForm()
    select_form = forms.SelectForm()
    if query_form.query.data and query_form.validate_on_submit():
        return flask.redirect(f"/search/by-name/{query_form.query.data}")
    else:
        print(query_form.errors)
    if select_form.submit.data and select_form.validate_on_submit():
        return flask.redirect(f"/search/by-category/{select_form.categories.data.lower()}")
    else:
        print(query_form.errors)
    return flask.render_template("index.html",query_form=query_form , select_form = select_form)


@app.route("/search/by-name/<product_name>" , methods=["GET", "POST"] )
@flask_login.login_required
def filter_product_by_name(product_name):
    query_form = forms.QueryForm()
    for product in Product.query.all():
        if product.name.lower() == product_name.lower():
            break
    else:
        return "Product not found"
    if query_form.query.data and query_form.validate_on_submit():
            return flask.redirect(f"/search/by-name/{query_form.query.data}")
    return flask.render_template("product_by_name.html", 
    product_name = product.name ,
    product_price =  product.price , 
    product_image =  product.image , product_category = product.category , query_form=query_form)


@app.route("/search/by-category/<category>")
@flask_login.login_required
def search_product_by_category(category):
    query_form = forms.QueryForm()
    category_products = []
    print(category)
    for product in Product.query.all():
        if product.category.lower() == category.lower() :
            category_products.append(product)
    return flask.render_template("products_by_category.html" , query_form = query_form , filtred_products = category_products)


@app.route("/sign-up", methods=["GET", "POST"])
def signup():
    query_form = forms.QueryForm()
    form = forms.SignupForm()
    if request.method == "POST":
        if form.validate_on_submit():

            user = User()
            user.name = form.username.data
            user.password = form.password.data
            user.save()

            return flask.redirect('/')
        else:
            print("Form errors:", form.errors)

    return flask.render_template("signup.html", form=form , query_form = query_form)


@app.route("/sign-in", methods=["GET", "POST"])
def signin():
    form = forms.SigninForm()
    if form.validate_on_submit():
        user = User.login_user(form.username.data, form.password.data)
        session["username"] = form.username.data
        if user:
            return flask.redirect('/')

    return flask.render_template("signin.html", form=form)

@app.route("/checkout" , methods=["GET", "POST"])
@flask_login.login_required
def checkout():
    query_form = forms.QueryForm()
    if query_form.query.data and query_form.validate_on_submit():
        return flask.redirect(f"/search/by-name/{query_form.query.data}")
    try :
        checkoutProductsDict = {}
        checkoutProductsDict["product_name"] = request.values.get("product_name")
        checkoutProductsDict["product_price"] = (Decimal(request.values.get("product_price").strip()))
        checkoutProductsDict["product_price_per_quantity"] = (Decimal(request.values.get("product_price").strip())) * (int(request.values.get("product_quantity")))
        checkoutProductsDict["product_quantity"] = int(request.values.get("product_quantity"))
        checkoutProducts.append(checkoutProductsDict)
    except AttributeError: 
        pass

    return flask.render_template("checkout.html" , query_form = query_form , checkoutProducts = checkoutProducts )

@app.route("/confirm" , methods=["GET", "POST"])
def confirm():
    query_form = forms.QueryForm()
    if query_form.query.data and query_form.validate_on_submit():
        return flask.redirect(f"/search/by-name/{query_form.query.data}")
    return flask.render_template("confirm.html" , query_form = query_form)

@app.route("/purchases" , methods=["GET", "POST"])
def purchases():
    query_form = forms.QueryForm()
    today = date.today()
    purchase_date = today.strftime("%b-%d-%Y")
    if query_form.query.data and query_form.validate_on_submit():
        return flask.redirect(f"/search/by-name/{query_form.query.data}")
    return flask.render_template("purchases.html", query_form = query_form, checkoutProducts=checkoutProducts,purchase_date=purchase_date , total_price = total_price)


@app.route("/about-us" , methods=["GET", "POST"])
def about_us():
    query_form = forms.QueryForm()
    if query_form.query.data and query_form.validate_on_submit():
        return flask.redirect(f"/search/by-name/{query_form.query.data}")
    return flask.render_template("aboutus.html" , query_form = query_form)


@app.route("/sign-out")
def signout():
    flask_login.logout_user()
    return flask.redirect('/')

