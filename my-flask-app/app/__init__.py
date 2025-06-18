from flask import Flask

app = Flask(__name__)

# Load configuration from a separate config file if needed
# app.config.from_object('config')

from app import routes