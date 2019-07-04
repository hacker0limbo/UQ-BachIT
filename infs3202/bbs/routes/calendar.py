from flask import Blueprint, render_template

main = Blueprint('calendar_bp', __name__)


@main.route("/")
def index():
    return render_template('calendar.html')