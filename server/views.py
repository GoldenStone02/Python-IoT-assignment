from flask import Blueprint, redirect, render_template, request, url_for

views = Blueprint('views', __name__)

@views.routes('/')
def index():
    return redirect("/login")

# Login Page
@views.route('/login')
def login():
    return render_template('login.html')

# Logout
@views.route('/logout')
def logout():
    return