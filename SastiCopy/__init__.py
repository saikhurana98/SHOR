import os

from flask import Flask

def create_app(test_config=None):
    #Creating and configuring the applications
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'sasticopy_sqlite')
    )

    if test_config is None:
        #Loading the instance config if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        #Loading the test config if passed in
        app.config.from_mapping(test_config)

    #Ensuring that the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except:
        pass

    #Now setting up a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello! Welcome to SHOR!'

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import land
    app.register_blueprint(land.bp)
    app.add_url_rule('/', endpoint='index')

    from . import blog
    app.register_blueprint(blog.bp)

    from . import shop
    app.register_blueprint(shop.bp)

    from . import user
    app.register_blueprint(user.bp)

    return app
