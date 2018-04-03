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

Now from the project root:
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ export FLASK_APP=app.py
$ flask run
```
This should open by default at http://127.0.0.1:5000/

or if you want to change the local ip, say to `0.0.0.0`
```
$ flask run --host=0.0.0.0
```

