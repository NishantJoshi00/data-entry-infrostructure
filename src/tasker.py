from flask import Flask, request
from driver.main import dbms

app = Flask(__name__)

# This is were you will introduce the endpoints
## This are the outgoing endpoints

from user_auth import setup
app, ums = setup(app, request)

