from flask import Blueprint, render_template
from flask_login import current_user, login_required
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/orders')
@login_required
def orders():
    return render_template('orders.html', username=current_user.name)