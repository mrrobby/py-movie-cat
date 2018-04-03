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

The `app` entry is just `app.py` right now for simplicity. That needs to be set in the environment and started. The easiest way is to enter:
```
$ export FLASK_APP=app.py
$ flask run
```

This should open by default at `http://127.0.0.1:5000/`
or if you want to change the local ip, say to `0.0.0.0`
```
$ flask run --host=0.0.0.0
```

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






Libraries:
- Flask-JWT: https://pythonhosted.org/Flask-JWT/
- Flask: 
- Moviepy: https://pypi.python.org/pypi/moviepy
- Numpy
- Their dependencies (run pip list to see)

