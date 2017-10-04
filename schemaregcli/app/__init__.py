from flask import Flask
from flask_bootstrap import Bootstrap
import logging
import coloredlogs

def mk_app():
    web = Flask(__name__)
    web.config['SECRET_KEY'] = "s3cr3t!"
    Bootstrap(web)
    return web

app = mk_app()

logger = logging.getLogger('flask-app')

from app import views