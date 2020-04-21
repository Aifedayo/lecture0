import os
from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

engine = create_engine('postgres://postgres:0417@localhost:5432/mydb')
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    flights = db.execute("SELECT * FROM flights").fetchall()
    return render_template("index.html", flights=flights)

@app.route("/book", methods=["POST"])
def book():
    """Book a flight."""

    #Get form infomation
    name = request.form.get("name")

    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid flight number.")

    #Make sure flight exists
    if db.execute("SELECT * FROM flights WHERE id = :id", {"id" : flight_id}).rowcount == 0:
        return render_template('error.html', message='No such flight with that id.')

    if name is "":
        return render_template('error.html', message="Invalid name format")
    
    db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)",
                {"name" : name, "flight_id":flight_id})
    db.commit()
    return render_template("success.html")

if __name__ == "__main__":
    app.run()



