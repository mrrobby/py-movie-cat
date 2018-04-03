
from flask import Flask, render_template, request
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
import os


app = Flask(__name__)
app.config.from_object('config')
#db = SQLAlchemy(app)

@app.route('/login')
def login():
    return 'login!'


@app.route('/logout')
def logout():
    return 'logout!'


@app.route('/videomagic')
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