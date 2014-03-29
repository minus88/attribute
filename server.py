from flask import Flask
import logging

server = Flask(__name__)
server.config.from_pyfile('config.py')

import app

@server.route('/')
def hello_world():
    return app.hello()


@server.route('/listUsers')
def listUsers():
    return app.listUsers()

@server.route('/getUser')
def getUser():
    return app.getUser()


@server.route('/display')
def display_connection():
    return app.display_connection()

@server.route('/v1/health',methods = ['POST'])
def health():
    return app.is_healthy()

