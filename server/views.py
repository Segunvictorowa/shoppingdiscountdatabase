from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>Hello Home</h1>"

@views.route('/products')
def products():
    return "<h1>Products</h1>"

@views.route('/about-us')
def aboutUs():
    return "<h1>About Us</h1>"