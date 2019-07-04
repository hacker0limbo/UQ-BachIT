from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
    jsonify,
)

from routes import *

from models.board import Board


main = Blueprint('board_bp', __name__)


@main.route("/admin")
def index():
    return render_template('board/admin_index.html')


@main.route("/add", methods=["POST"])
def add():
    form = request.form
    u = current_user()
    m = Board.new(form)
    return redirect(url_for('topic.index'))


@main.route("/addjson", methods=["POST"])
def add_json():
    form = request.get_json()
    u = current_user()
    m = Board.new(form)
    return jsonify(request.json)

