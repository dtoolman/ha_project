import os
from flask import Flask, redirect, render_template

from app.auth import login_required


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'db.sqlite'),
    )

    # load the instance config, if it exists
    app.config.from_pyfile('config.py', silent=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # the home page
    @app.route('/')
    @login_required
    def index():
        return render_template('index.html')

    # the map page
    @app.route('/map/')
    @login_required
    def map():
        return render_template('map.html')

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    return app
