from flask import Blueprint, request, redirect, render_template


index = Blueprint('index', __name__)


@index.route('/')
def home():
    return render_template('index.html')


@index.route('/signup', methods=['POST'])
def signup():
    phone = request.form['phone']
    if phone != '' and phone.isdecimal() and len(phone.replace('-', '')) == 10:
        phone = phone.replace('-', '')
        try:
            steam = request.form['steam']
            if steam == "on":
                steam = True
            else:
                steam = False
        except:
            steam = False

    return redirect('/')
