import os
import json
import random
from flask import Blueprint, redirect, render_template, request, url_for, flash

views = Blueprint('views', __name__)

# Site Routing

# Homepage
@views.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        if "change_pin" in request.form:
            print("Change Pin")
            return redirect(url_for('views.change_pin'))
        elif "change_rfid" in request.form:
            return redirect(url_for('views.change_rfid'))
        elif "generate_otp" in request.form:
            return redirect(url_for('views.generate_otp'))
        else:
            pass
    return render_template('index.html')

# Login Page
@views.route('/login', methods=["GET", "POST"])
def login():
    error = ""
    if request.method == "POST":
        username = request.form['username']
        pin = request.form['pin']
        
        data = fetch_data("../Project/server/database/users.json")

        # Check if username exists in db
        for user in data['users']:
            print(user['username'])
            if user['username'] == username:
                if user['pin'] == int(pin):

                    # ! Need to transfer username to session
                    return redirect(url_for('views.index'))
                else:
                    error = "PIN is incorrect"
                    break
        else:
            error = "Username does not exist"
        
        # Check if pin is correct
        if len(pin) != 6:
            error = "PIN must be 6 digits"

    return render_template('login.html', error=error)

# Signup Page
@views.route('/signup')
def signup():
    return

# Change Pin Page
@views.route('/change_pin', methods=['GET', 'POST'])
def change_pin():
    # Empty error
    error = ""
    if request.method == 'POST':
        new_pin = request.form['new_pin']
        new_pin2 = request.form['new_pin2']
        if new_pin == new_pin2 and len(new_pin) == 6:
            # Redirect to dashboard
            flash("Pin changed successfully", "success")

            change_data("user", int(new_pin))

            return redirect(url_for('views.index'))
        elif len(new_pin) != 6:
            error = "Pin must be 6 digits long"
        else:
            # Error message
            error = "Pin did not match"
    return render_template('changePIN.html', error=error)

# Change RFID Page
@views.route('/change_rfid')
def change_rfid():
    error = ""

    return render_template('changeRFID.html')

# Generate OTP
@views.route('/generate_otp')
def generate_otp():
    error = ""

    if request.method == "POST":
        pass

    # Generate OTP that will be keyed into the keypad
    otp = random.randint(100000, 999999)
    print(otp)
    return render_template('generateOTP.html', otp=otp, error=error)

# Monitor
@views.route('/monitor')
def monitor():
    error = ""



    return render_template('monitor.html')

# End of Site Routing

# General functions

def fetch_data(filepath: str):
    with open(filepath, "r") as f:
        data = json.load(f)
    return data

def upload_data(filepath: str, data: any):
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)
    return

def change_data(username: str, pin: int):
    print(os.path.abspath(__file__))
    
    data = fetch_data("../Project/server/database/users.json")

    for user in data['users']:
        if user['username'] == username:
            user['pin'] = pin
            break

    upload_data("../Project/server/database/users.json", data)
    data2 = fetch_data("../Project/server/database/users.json")