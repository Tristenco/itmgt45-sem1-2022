from flask import Flask,redirect
from flask import render_template
from flask import request
from flask import session
import ordermanagement as om
import database as db
import authentication
import logging


app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)
app.logger.setLevel(logging.INFO)

app.secret_key = b's@g@d@c0ff33!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/auth', methods = ['GET', 'POST'])
def auth():
    username = request.form.get('username')
    password = request.form.get('password')

    is_successful, user = authentication.login(username, password)
    
    app.logger.info('%s', is_successful)
    if(is_successful):
        session["user"] = user
        return redirect('/')
    else:
        return render_template('/wronglogin.html')

@app.route('/')
def index():
    return render_template('index.html', page="Index")

@app.route('/logout')
def logout():
    session.pop("user",None)
    session.pop("cart",None)
    return redirect('/')


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/products')
def products():
    product_list = db.get_products()
    return render_template('products.html', page="Products", product_list=product_list)

@app.route('/productdetails')
def productdetails():
    code = request.args.get('code', '')
    product = db.get_product(int(code))

    return render_template('productdetails.html', code=code, product=product)

@app.route('/branches')
def branches():
    branch_list = db.get_branches()
    return render_template('branches.html', page="Branches",branch_list=branch_list)

@app.route('/branchdetails')
def branchdetails():
    code = request.args.get('code', '')
    branch = db.get_branch(int(code))

    return render_template('branchdetails.html', code=code, branch=branch)

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html', page="About Us")

@app.route('/addtocart')
def addtocart():
    code = request.args.get('code','')
    product = db.get_products(int(code))
    item = dict()

    item["qty"] = 1
    item["name"] = product["name"]   
    item["subtotal"] = product["price"]*item["qty"]
    item["code"] = code  

    if(session.get("cart") is none):   
        session["cart"]={}

    cart = session["cart"]
    cart[code] = item
    session["cart"] = cart
    return redirect('/cart')

@app.route('/updatecart', methods=['POST'])
def updatecart():
    code=request.form.getlist("code")
    qty=request.form.getlist("qty")
    for code, qty in zip(code,qty):
        if(qty !=''):
            product = db.get_product(int(code))
            item=dict()

            item["qty"]=int(qty)
            item["name"]=product["name"]
            item["subtotal"] = product["price"]*item["qty"]
            item["code"] = code  

            cart = session["cart"]
            cart[code]=item
            session["cart"]=cart
    return redirect ('/cart')

@app.route('/deleteitem')
def deleteitem():
    code = request.args.get('code', '')
    carts = session["cart"]
    cart.pop(code)
    session["cart"]=cart
    return redirect ('/cart')

@app.route('/cart')
def cart():
    return render_template("cart.html")

@app.route('/checkout')
def checkout():

    
    return render_template("checkout.html")
