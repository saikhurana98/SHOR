from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)

from werkzeug.exceptions import abort

from SastiCopy.auth import login
from SastiCopy.db import get_db

bp = Blueprint('land', __name__)

@bp.route('/')
def index():
    db = get_db()
    products = db.execute(
    'SELECT * FROM product ORDER BY name DESC LIMIT 2;'
    ).fetchall()
    print(products)
    return render_template('land/index.html', products = products)

@bp.route('/contact')
def contact():
    return render_template('land/contact.html')

@bp.route('/searchresult')
def search_result(products):
    """
    Template out and display the search search results.
    """
    print(products)
    print("The redirect statement works!")
    return render_template('land/search.html', products = products)

@bp.route('/search', methods=['GET', 'POST'])
def search_database():
    """
    Validate the form inputs
    Search for the right name inside the field, and store the number
    of the
    """
    db=get_db()
    db.execute(
    	'SELECT * FROM user;'
    ).fetchall()

    try:
        _term = request.form['search_field']
        print (_term)
        print (request.method)
        if _term and request.method == 'POST':
            db = get_db()
            search_results = db.execute(
            'SELECT * FROM product WHERE name LIKE ?;',('%' + _term +'%',)
            ).fetchall()
            return render_template('/land/search.html', products = search_results)

            #@Prajwal if the links don't work, check if this is the right way to do this redirect
            #Incase it doesn't work, you can also alternatively directly call the search_result() function from Here
            #i.e execute either of the two lines
            print(search_results)
            #return redirect(url_for('auth.login', products=search_results))
        else:
            return 'Error while performing search'
    except ValueError:
    	print("Hi2")

