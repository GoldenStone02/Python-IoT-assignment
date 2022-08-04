import os
import json
import random
from flask import Blueprint, redirect, render_template, request, url_for, flash
import socket

# Socket establising connection to web_iot.py script for remote login and remote register rfid

# This function creates a new connection with the server
# it returns the socket being connected
def newConnection():
    # Connecting to server
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 8000

    try:
        soc.connect((host, port))
    except:
        print('\n' + '\33[41m' + "[ERROR] Connection Error. Cannot connect to server" + '\33[0m' )
        pass
    
    return soc

# This function receives the binary input sent from a client
# It then decodes the message and returns it as a string
# The arguments of this function are connection which is the socket connection and the max buffer size 
def receive_input(connection, max_buffer_size):
    client_input = connection.recv(max_buffer_size)
    decodedInput = client_input.decode("utf8").rstrip()
    return decodedInput

views = Blueprint('views', __name__)

global_username = ""

# Site Routing

# Homepage
@views.route('/')
def index():
    return redirect(url_for('views.login'))

# Dashboard
@views.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == "POST":
        try:
            if "change_pin" in request.form:
                print("Change Pin")
                return redirect(url_for('views.change_pin'))
            elif "change_rfid" in request.form:
                # Socket to send to request of registering RFID
                connection = newConnection() # creata a new socket 
                connection.send(b'--Register RFID--') # let client to go into registerRFID in web_iot.py

                # Server will reply with 'Success or Failure'
                serverInput = receive_input(connection,max_buffer_size=5120)
                print('Server Reply:' +'\33[31m' + serverInput + '\33[0m')

            elif "generate_otp" in request.form:
                return redirect(url_for('views.generate_otp'))
            elif "remote_unlock" in request.form:
                # Socket to send to request of remotely unlocking door
                 # Socket to send to request of registering RFID
                connection = newConnection() # creata a new socket 
                connection.send(b'--Remote Unlock Door--') # let client to go into remoteUnlock function in web_iot.py

                # Server will reply with 'RFID Registered Success!' or 'RFID Registered Failed...'
                serverInput = receive_input(connection,max_buffer_size=5120)
                print('Server Reply:' +'\33[31m' + serverInput + '\33[0m')

            else:
                pass
        except:  
            pass # if any error,such as crashes, we just pass so that whole programme will continue.
        
    return render_template('dashboard.html')

# Login Page
@views.route('/login', methods=["GET", "POST"])
def login():
    error = ""
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        
        data = fetch_data("./server/database/users.json")

        # Check if username exists in db
        for user in data['users']:
            print(user['username'])
            if user['username'] == username:
                if user['password'] == password:

                    # ! Need to transfer username to session
                    global global_username
                    global_username = username
                    return redirect(url_for('views.dashboard'))
                else:
                    error = "Password is incorrect"
                    break
        else:
            error = "Username does not exist"

    return render_template('login.html', error=error)

# Monitor
@views.route('/monitor')
def monitor():
    error = ""

    return render_template('monitor.html')

# Change Pin Page
@views.route('/change_pin', methods=['GET', 'POST'])
def change_pin():
    # Empty error
    error = ""
    if request.method == 'POST':
        new_pin = request.form['new_pin']
        new_pin2 = request.form['new_pin2']
        if new_pin == new_pin2 and len(new_pin) == 4:
            # Redirect to dashboard
            flash("Pin changed successfully", "success")

            upload_data("./server/database/password.txt", int(new_pin))

            return redirect(url_for('views.dashboard'))
        elif len(new_pin) != 4:
            error = "Pin must be 4 digits long"
        else:
            # Error message
            error = "Pin did not match"
    return render_template('changePIN.html', error=error)

# Generate OTP
@views.route('/generate_otp')
def generate_otp():
    error = ""

    # Generate OTP that will be keyed into the keypad
    otp = random.randint(1000, 9999)
    upload_data("./server/database/password.txt", int(otp))

    return render_template('generateOTP.html', otp=otp, error=error)

@views.route('/profile')
def profile():
    username = global_username

    return render_template('profile.html', username=username)

# End of Site Routing

# General functions

def fetch_data(filepath: str):

    file_split = os.path.splitext(filepath)
    if file_split[1] == ".json":
        with open(filepath, "r") as f:
            data = json.load(f)
    elif file_split[1] == ".txt":
        with open(filepath, "r") as f:
            data = f.read()
    return data

def upload_data(filepath: str, data: any):
    file_split = os.path.splitext(filepath)
    if file_split[1] == ".json":
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)
    elif file_split[1] == ".txt":
        with open(filepath, "w") as f:
            f.write(f"{data}")
    return