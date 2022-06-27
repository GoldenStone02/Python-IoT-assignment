from flask import Blueprint, redirect, render_template, request, url_for

views = Blueprint('views', __name__)

# Login Page
@views.route('/login', method=['GET', 'POST'])
def login():
    return

# Logout
@views.route('/logout')
def logout():
    return