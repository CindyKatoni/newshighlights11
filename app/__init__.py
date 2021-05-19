from flask import Flask
# from .config import DevConfig
from instance.config import DevConfig

# Initialize application
app = Flask(__name__, instance_relative_config=True)

# Setting configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views
