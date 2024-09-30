from flask import Flask, render_template, request, redirect
from db import Database

app = Flask(__name__)
db = Database('database.db')


@app.route('/')
def list_ews():
    """
    TO IMPLEMENT
    """
    pass

@app.route('/add', methods=['POST'])
def add_ew():
    """
    TO IMPLEMENT
    """
    pass


# EXTRA CREDIT
@app.route('/<int:id>')
def view_ew(id):
    """
    TO IMPLEMENT
    """
    pass