#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)
# refers to the name of the current module

@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

# __name__ is equal to the name of the module in question unless it is the module being run from the command line. In this case, it is set to '__main__'. This is very helpful for writing scripts!
# When the instance receives a URL pointing to that route, the view function is called and the return value is added to the response by the instance


@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

# Anything included in the route passed to the app.route decorator with angle brackets <> surrounding it will be passed to the decorated function as a parameter. We can make sure that the username is a valid string, int, float, or path  by specifying this in the route

# Flask has to parse "string" and "username" from the route. How can you use Python to remove brackets and get parameters out of a string

if __name__== '__main__':
     app.run(port=5555, debug=True)
# With str methods:

# url = '/<string:username>'

# url = url.replace('/<', '')

# url = url.replace('>', '')

# type, parameter = url.split(':')

# With re:

# exp = re.compile('[A-z]+')

# type, parameter = exp.findall(url)




