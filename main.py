from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+pymysql://admin:password@endpoint/table_name"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "SECRET_KEY"

db = SQLAlchemy(app)


class Megadb(db.Model):
    __tablename__ = "Megadb"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ticket = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(100), nullable=False)
    delete_code = db.Column(db.String(20))
    datetime = db.Column(db.DateTime, default=datetime.now)

    def __repr__(self):
        return f"<mega {self.name}>"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST", "GET"])
def submit():
    if request.method == "POST":
        name = request.form["name"]
        ticket = request.form["ticket"]
        message = request.form["message"]
        delete_code = request.form["delete_code"]
        new_info = Megadb(
            name=name, ticket=ticket, message=message, delete_code=delete_code
        )
        try:
            db.session.add(new_info)
            db.session.commit()
            return render_template("index.html")
        except:
            pass
    return render_template("submit.html")


@app.route("/find", methods=["POST", "GET"])
def find():
    if request.method == "POST":
        name = request.form["name"]
        infos = Megadb.query.filter_by(name=name).order_by(Megadb.datetime.desc()).all()
        return render_template("find.html", infos=infos)
    else:
        return render_template("find.html")


@app.route("/delete", methods=["POST", "GET"])
def delete():
    if request.method == "POST":
        name = request.form["name"]
        delete_code = request.form["delete_code"]
        db.session.query(Megadb).filter(
            Megadb.name == name, Megadb.delete_code == delete_code
        ).delete()
        db.session.commit()
        return render_template("index.html")
    else:
        return render_template("delete.html")


if __name__ == "__main__":
    app.run()
