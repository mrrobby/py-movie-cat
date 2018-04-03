Flask App.  Here's the setup

First make sure you have python3.6 install (see homebrew install if not), 
```
$ brew update
$ brew install python
```
or for more (info)[http://docs.python-guide.org/en/latest/starting/install3/osx/]
https://gist.github.com/alyssaq/f60393545173379e0f3f

Check if `pip` is installed:
```
$ which pip
$ pip --version
pip 9.0.1
```

Now from the project root, configure the app with:
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

We'll also use Redis and celery for Job queueing. I'd rather use RabbitMQ for something like that, redis configuration is much simpler in the context of a 4 hour test. To get that setup make sure you have redis installed and running. You can always use a docker container for it if you want, or just use homebrew. Assuming maybe your local config is not docker-ready, add and start redis with homebrew.
```
$ brew update
$ brew install redis
```

You can see services with:
```
$ brew services list
```

Start and stop with:
```
$ brew services start redis
```

Start redis now. We are assuming it starts on the default port `6379`.

Start the celery worker. This handles queuing jobs in redis. It will print log info so you can monitor
```
$ celery -A video_tools.celery worker --loglevel=info
```

The `app` entry is just `app.py` right now for simplicity. That needs to be set in the environment and started. The easiest way is to enter:
```
$ export FLASK_APP=app.py
$ flask run
```

This should open by default at `http://127.0.0.1:5000/`

Get a JWT token first. Use postman or Paw and make the following request
```
POST /auth HTTP/1.1
Host: localhost:5000
Content-Type: application/json

{
    "username": "tyler",
    "password": "123456"
}
```

This will return a JWT in the form:
```
{
	"access_token": "header.payload.signature"
}
```

Take the token and save for future requests. It will expire in 5 minutes.

In future requests, the token should be submitted in the header as
```
Authorization JWT the.jwt.token
```

Create two more requests adding the token at the following endpoints:
```
GET /videomagic
GET /status/<task-id>
```

We'll convert the first to POST later. 





Libraries:
- Flask-JWT: https://pythonhosted.org/Flask-JWT/
- Flask: 
- Moviepy: https://pypi.python.org/pypi/moviepy
- Numpy
- Their dependencies (run pip list to see)

