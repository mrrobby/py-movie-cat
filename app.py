
from flask import Flask, render_template, request
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
import os
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
from user import *


app = Flask(__name__)
app.config.from_object('config')
jwt = JWT(app, authenticate, identity)
#not going to use SQLAlchemy, but would if we need an ORM
#db = SQLAlchemy(app)

@app.route('/pinghs256')
@jwt_required()
def pinghs256():
		"""" Sanity Check Route """
		return 'current identity: {}'.format(current_identity.username)

@app.route('/videomagic')
@jwt_required()
def videomagic():
    return 'videomagic!'


# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''