from driver.main import udb
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import re

# This are dummy variable for testing
soft = "dummy-variable"
from flask import Flask, request
app = Flask(__name__)
# ---

ums = {}
auth = HTTPBasicAuth()
db = udb(soft)

@auth.verify_password
def verify_password(username, password):
    if db.u_exists(username) and db.check_password(username, generate_password_hash(password)):
        return True
    else:
        return False

@app.route("/users/new_user", methods=['POST'])
def new_user():
    """
    This post request must contain the following data
    The request type must be `application/json`
    {
        "username": ~~Username~~,
        "email": ~~Email~~,
        "password": ~~Password~~ ( Hashed - sha256 )
    }
    return status:
    0 -> Successfully registered
    1 -> There was an error while parsing
    2 -> Email / Username already exists !!
    """

    username = request.json['username']
    if len(username) < 4:
        return '1'
    ds = "'\\\"%}{"
    for i in ds:
        if i in username:
            return '1'
    rem = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    email = request.json['email']
    if re.fullmatch(rem, email) == None:
        return '1'
    password = request.json['password']
    if len(password) != 64:
        return '1'
    _ = db.register(username, email, generate_password_hash(password))
    if _ == 0:
        return '0'
    else:
        return '2'

@app.route("/users/delete_user", methods=['GET'])
@auth.login_required
def delete_user():
    db.delete(auth.username())
    return '0'


@app.route("/users/change_user", methods=['POST'])
@auth.login_required
def change_user():
    """
    This post request must contain the following data
    The request type must be `application/json`
    {
        "password": ~~Password~~ ( Hashed - sha256 )
    }
    """
    _ = db.change_password(auth.username(), generate_password_hash(request.json['password']))
    return str(_)
    