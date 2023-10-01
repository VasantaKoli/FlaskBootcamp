from flask import Flask
from keys.apiToken import SITE_API_KEY


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SITE_API_KEY

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    return app
