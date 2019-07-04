from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
)

from routes import *
from utils import *
from models.topic import Topic
from models.board import Board

main = Blueprint('topic', __name__)


@main.route("/")
def index():
    board_id = int(request.args.get('board_id', -1))
    if board_id == -1:
        ms = Topic.all()
    else:
        ms = Topic.all(board_id=board_id)
    bs = Board.all()
    u = current_user()
    if u is None:
        # form = {
        #     'username': 'guest1',
        #     'password': '1be6af03717a0906a774a129ac467fcea8f89849df003548a8039cffffb12baf',
        # }
        # u = User.new(form)
        u = User.one(username='guest')
        # u.username = 'guest'
    format_ts = format_time(ms)
    return render_template("topic/index.html", ms=ms, ct=format_ts, u=u, bs=bs, bid=board_id)


@main.route('/<int:id>')
def detail(id):
    m = Topic.get(id)
    t = format_time(m)
    board_id = int(request.args.get('board_id', -1))
    # 传递 topic 的所有 reply 到 页面中
    return render_template("topic/detail.html", topic=m, t=t, u=current_user(), bid=board_id)


@main.route("/delete")
def delete():
    id = int(request.args.get('id'))
    u = current_user()
    print('删除 topic 用户是', u, id)
    Topic.delete(id)
    return redirect(url_for('.index'))


@main.route("/new")
def new():
    board_id = int(request.args.get('board_id', -1))
    bs = Board.all()
    # return render_template("topic/new.html", bs=bs, bid=board_id)
    token = new_csrf_token()
    log('topic token:', token)
    # get content form url parameter
    content = request.args.get('content', '')
    return render_template("topic/new.html", bs=bs, token=token, bid=board_id, md=content)


@main.route("/add", methods=["POST"])
def add():
    form = request.form.to_dict()
    u = current_user()
    Topic.new(form, user_id=u.id)
    return redirect(url_for('.index'))


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in set(['txt', 'md'])


@main.route('/upload', methods=['POST'])
def md_upload():
    file = request.files['custom-md']
    if file and allowed_file(file.filename):
        content = file.read()
        return redirect(url_for('.new', content=content))