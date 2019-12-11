from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)

from flask import session

from werkzeug.exceptions import abort

from SastiCopy.auth import login, login_required
from SastiCopy.db import get_db

bp = Blueprint('shop',__name__, url_prefix='/shop')

#A well written company description goes here.
@bp.route('/about')
def index():
    return render_template('shop/about.html')

@bp.route('/cart')
@login_required
def cart():
    return render_template('shop/cart.html')

@bp.route('/checkout')
def checkout():
    return render_template('shop/checkout.html')

#Hardcode the category page in HTML
@bp.route('/category')
def contact():
    db = get_db()
    products = db.execute(
    'SELECT * FROM product'
    ).fetchall()
    print(products)
    return render_template('shop/category.html', products = products)

#Method should return product information
def get_product(identity):
    product = get_db().execute(
    'SELECT * FROM product WHERE id = (?);', (str(identity))
    ).fetchone()
    return product

"""
#Method should return reviews
def get_reviews(identity):
    product = get_db().execute(
    'SELECT * FROM reviewsratings WHERE product_id = (?);', (str(identity))
    ).fetchall()
    return reviews
"""
#Render product detailed view, photo, description etc.
@bp.route('/singleproduct/<int:id>/view')
def singleprod(id):
    product = get_product(id)
    print(product['name'])
    #reviews = get_reviews(id)
    #return render_template('shop/single-product.html', products = product, reviews = reviews)
    return render_template('shop/single-product.html', products = product)

@bp.route('/addtowishlist', methods=['POST'])
def add_to_wishlist():
    _code=request.form['id']
    print("Item code {} needs to be added to the user's wishlist".format(_code))
    if g.user is not None:
        db = get_db()
        wishlist = db.execute('SELECT wishlist FROM user WHERE id = 3')
        wishlist = wishlist.fetchall()
        wishlist = str(wishlist)
        wishlist = wishlist + format(_code)
        print("print 1 ", wishlist)
        print("print 1.5 id is {}".format(g.user['id']))
        wishlist2 = db.execute('UPDATE user SET wishlist = ? WHERE id = 3',(wishlist,))
        wishlist2 = wishlist2.fetchall()
        wishlist3=  db.execute('SELECT wishlist FROM user WHERE id = 3').fetchall()

        print("print 2 ", str(wishlist3))
        return render_template('land/index.html')
    else:
        return redirect_url(url_for('auth.login'))
    #Validating the recieved values
    """
    Get the username of the user who is currently logged in
    Then get the text of all the product ids of the items inside the wishlist.
    From the string that's returned from the wishlist, extract an integer array
    From the integer array, pass to the get product information tab ...
    From the get product imformation method, get the objects containing the information
    """

@bp.route('/wishlist')
def my_wishlist():
    """
    Get the prouct information and then template it out
    Extract unique codes from the user wishlist string
    Template out the product information
    """
    db = get_db()
    wishlist = db.execute(
	'SELECT wishlist FROM user WHERE id = ?;',(format(g.user['id']),)
	).fetchall()
    print(wishlist)
    wishlist_string = wishlist.split(",")
    wishlist_int = map(int, wishlist_string)
    return render_template('/shop/wishlist.html', products = wishlist_int)

#To add a product to the cart
@bp.route('/add', methods=['POST'])
def add_product_to_cart():
    cursor = None
    try:
        _quantity = int(request.form['quantity'])
        _code = request.form['id']
        print("Code reaches here")
        #Validating the recieved values.
        if _quantity and _code and request.method == 'POST':
            print("1")
            db = get_db()
            print("2")
            row = db.execute('SELECT * FROM product WHERE id = {}'.format(_code)).fetchone()
            print("3")
            if row==None:
            	print("999")
            print(row['code'])

            itemArray = { row['code'] : {'name' : row['name'], 'code' : row['code'], 'quantity' : _quantity, 'price' : row['price'], 'image' : row['image'], 'total_price': _quantity * row['price']}}

            all_total_price=0
            all_total_quantity=0
            print("4")

            session.modified=True
            if 'cart_item' in session:
                print("5")
                print("in 5", session['cart_item'])
                if row['code'] in session['cart_item']:
                    print("6")
                    for key,value in session['cart_item'].items():
                        print('7')
                        if row['code'] == key:
                            print("8")
                            old_quantity = session['cart_item'][key]['quantity']
                            total_quantity = old_quantity + _quantity
                            session['cart_item'][key]['quantity'] = total_quantity
                            session['cart_item'][key]['total_price'] = total_quantity * row['price']
                            print("9")
                else:
                    print("above 21" , session['cart_item'])
                    print("itemarray above 21", itemArray)
                    session['cart_item'] = array_merge(session['cart_item'], itemArray)
                    print("21")
                    print("after array merge ", session['cart_item'])


                print("22")
                print("in session ", session)
                print("in session", session['cart_item'])
                for key, value in session['cart_item'].items():
                    print("22.5")
                    individual_quantity = int(session['cart_item'][key]['quantity'])
                    individual_price = float(session['cart_item'][key]['total_price'])
                    all_total_quantity = all_total_quantity + individual_quantity
                    all_total_price = all_total_price + individual_price
                    print("23")
            else:
                    session['cart_item'] = itemArray
                    all_total_quantity = all_total_quantity + _quantity
                    all_total_price = all_total_price + _quantity * row['price']
                    print("25")

            session['all_total_quantity'] = all_total_quantity
            session['all_total_price'] = all_total_price
            return redirect(url_for('shop.cart'))

        else:
            return 'Error while adding item to cart'
    except Exception as e:
        print("Exception encountered!")
        print(e)


@bp.route('/delete/<string:code>')
def delete_product(code):
	try:
		all_total_price = 0
		all_total_quantity = 0
		session.modified = True

		for item in session['cart_item'].items():
			if item[0] == code:
				session['cart_item'].pop(item[0], None)
				if 'cart_item' in session:
					for key, value in session['cart_item'].items():
						individual_quantity = int(session['cart_item'][key]['quantity'])
						individual_price = float(session['cart_item'][key]['total_price'])
						all_total_quantity = all_total_quantity + individual_quantity
						all_total_price = all_total_price + individual_price
				break

		if all_total_quantity == 0:
			session.clear()
		else:
			session['all_total_quantity'] = all_total_quantity
			session['all_total_price'] = all_total_price

		#return redirect('/')
		return redirect(url_for('.cart'))
	except Exception as e:
		print(e)


@bp.route('/empty')
def empty_cart():
    try:
        session.clear()
        #Feel free to change this to whatever you feel is necessary
        #As a design feature to when the cart is emptied.
        return redirect(url_for('.cart'))
    except Exception as e:
        print(e)

def array_merge( first_array , second_array ):
	if isinstance( first_array , list ) and isinstance( second_array , list ):
		return first_array + second_array
	elif isinstance( first_array , dict ) and isinstance( second_array , dict ):
		return dict( list( first_array.items() ) + list( second_array.items() ) )
	elif isinstance( first_array , set ) and isinstance( second_array , set ):
		return first_array.union( second_array )
	return False

"""

@Prajwal : As a reference to how the functions work and how to end up
templating the products objects that are being passed to :

https://www.roytuts.com/simple-shopping-cart-using-python-flask-mysql/


"""
