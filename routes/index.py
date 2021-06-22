from flask import Blueprint, request, redirect, render_template
from utils import default
from . import steam, db

index = Blueprint("index", __name__)
config = default.get("config.json")


@index.route("/")
def home():
    return render_template("index.html", free_steam=steam.get_free_games())


@index.route("/signup", methods=["POST"])
def signup():
    phone = request.form["phone"]
    email = request.form["email"]
    if (phone != "" and phone.isdecimal() and len(phone.replace("-", "")) == 10) or (
        email != "" and email.__contains__("@")
    ):
        phone = phone.replace("-", "")

        try:
            notify_email = request.form["notify_email"]
            if notify_email == "on":
                notify_email = True
            else:
                notify_email = False
        except:
            notify_email = False

        try:
            notify_text = request.form["notify_text"]
            if notify_text == "on":
                notify_text = True
            else:
                notify_text = False
        except:
            notify_text = False

        try:
            steam = request.form["steam"]
            if steam == "on":
                steam = True
            else:
                steam = False
        except:
            steam = False

        db.db_connect()
        db.db_insert(
            phone=phone,
            email=email,
            notify_email=notify_email,
            notify_text=notify_text,
            steam=steam,
        )

    return redirect("/")
