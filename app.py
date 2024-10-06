from flask import Flask, render_template, request, redirect
from db import Database
import os

app = Flask(__name__)
db = Database('database.db')


@app.route('/')
def list_ews():
    return render_template("list.html", rows=db.get_ews())

@app.route('/add', methods=['POST'])
def add_ew():
    title = request.form["title"]
    subject = request.form["subject"]
    beak = request.form["beak"]
    due_date = request.form["due_date"]
    db.create_ew(title, subject, beak, due_date)
    return redirect("/")


# EXTRA CREDIT
@app.route('/<int:id>')
def view_ew(id):
    ew = db.get_ew(id)
    return render_template("detail.html", ew=ew)


@app.route('/delete/<int:id>', methods=['POST'])
def delete_ew(id):
    db.delete_ew(id)
    return redirect("/")


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
