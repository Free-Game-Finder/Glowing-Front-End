from config import DevConfig, ProdConfig
from flask import Flask
from flask_assets import Environment, Bundle

from routes.index import index

# from routes.post import post

CONFIGS = {'dev': DevConfig, 'prod': ProdConfig}


def create_app(env):
    config = CONFIGS[env]

    # Instantiate Flask
    app = Flask(
        __name__,
        template_folder=config.TEMPLATE_FOLDER,
        static_url_path=config.STATIC_PATH,
        static_folder=config.STATIC_FOLDER
    )

    app.config.from_object(config)
    assets = Environment(app)
    # JS/CSS bundlers for minification
    js = Bundle(
        'js/jquery.min.js',
        'js/breakpoints.min.js',
        'js/browser.min.js',
        'js/main.js',
        'js/util.js',
        filters='jsmin',
        output='js/bundle.min.js')
    css = Bundle(
        'css/fontawesome-all.min.css',
        'css/main.css',
        filters='cssmin',
        output='css/bundle.min.css'
    )

    assets.register('js_modules', js)
    assets.register('css_modules', css)

    app.register_blueprint(index)

    return app
