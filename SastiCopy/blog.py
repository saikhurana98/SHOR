import functools
from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)
from werkzeug.security import check_password_hash, generate_password_hash

from SastiCopy.db import get_db

bp = Blueprint('blog', __name__, url_prefix='/blog')

@bp.route('/')
def blog():
    return render_template('blog/blog.html')

@bp.route('/singleblog')
def single_blog():
    return render_template('blog/single-blog.html')

# In case this needs to be changed to use a database in the future, the code for
# the same can be found commented out in the land.py file.
