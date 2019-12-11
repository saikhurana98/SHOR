from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)

from werkzeug.exceptions import abort

from SastiCopy.auth import login
from SastiCopy.db import get_db

bp = Blueprint('user',__name__, url_prefix='/user')

@bp.route('/confirmation')
def confirmation():
    return render_template('user/confirmation.html')

@bp.route('/tracking')
def tracking():
    return render_template('user/tracking.html')

@bp.route('/profile_change', methods=('GET','POST'))
def change_details():

    if request.method == 'POST':
        db = get_db()
        user_details = db.execute(
        	'SELECT * FROM user;'
        ).fetchall()
        print(user_details)

        _name=request.form['name']
        #_address=request.form['address']
        #_contact=request.form['contact']
        #_email=request.form['email']
        print("Hi1")
        #If nothing has been entered into the fields, don't change the data
        if _name is not None :
            print("Hi2")
            print(_name)
            db.execute("UPDATE user SET name = '?' WHERE id = ?;",(_name,str(g.user),))
            print("Hi3")
        """
        if not _address :
            db.execute("UPDATE user SET address={} WHERE id={}".format(_address, g.user))
        if not _contact :
            db.execute("UPDATE user SET contact={} WHERE id={}".format(_contact, g.user))
        if not _email :
            db.execute("UPDATE user SET email={} WHERE id={}".format(_email, g.user))
"""
    return render_template('user/user_profile.html')

#Profile details page added
@bp.route('/profile_details')
def details():
    if g.user is not None:
        db = get_db()
        products = db.execute(
        'SELECT * FROM user;'
        ).fetchall()
        return render_template('user/user_profile.html', products = products)
    else :
        return redirect(url_for(auth.login))
    return render_template('user/user_profile.html', products = products)