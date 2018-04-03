
from flask import Flask, request, jsonify, url_for
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
import os
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
from user import *
from video_tools import concat_video_files


app = Flask(__name__)
app.config.from_object('config')
jwt = JWT(app, authenticate, identity)
# not going to use SQLAlchemy, but would if we need an ORM
#db = SQLAlchemy(app)

@app.route('/pinghs256')
@jwt_required()
def pinghs256():
    """" Sanity Check Route """
    return 'current identity: {}'.format(current_identity.username)


@app.route('/videomagic')
@jwt_required()
def videomagic():
    # More likely this would publish the job to another service via RabbitMQ, Kafka, Redis, etc...
    result = concat_video_files.apply_async(args=[
      'assets/SnowboardArchivesVideo1.mp4',
      'assets/VailDreamVideo1.mp4',
      'assets/FinalVailVideo.mp4']
    )

    return jsonify({'Location': url_for('taskstatus', task_id=result.id)}), 202


# Taken from Using Celery with Flask article
# https://blog.miguelgrinberg.com/post/using-celery-with-flask
@app.route('/status/<task_id>')
@jwt_required()
def taskstatus(task_id):
    task = concat_video_files.AsyncResult(task_id)
    if task.state == 'PENDING':
        # job did not start yet
        response = {
            'state': task.state,
            'current': 0,
            'total': 1,
            'status': 'Pending...'
        }
    elif task.state != 'FAILURE':
        response = {
            'state': task.state,
            'current': task.info.get('current', 0),
            'total': task.info.get('total', 1),
            'status': task.info.get('status', '')
        }
        if 'result' in task.info:
            response['result'] = task.info['result']
    else:
        # something went wrong in the background job
        response = {
            'state': task.state,
            'current': 1,
            'total': 1,
            'status': str(task.info),  # this is the exception raised
        }
    return jsonify(response)


# Default port:
if __name__ == '__main__':
    app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
