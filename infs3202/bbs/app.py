from flask import Flask


from models.user import User
from models.topic import Topic
from models.reply import Reply
from models.message import Messages
from models.board import Board

from models.base_model import db

import os

from routes import current_user
from routes.index import main as index_routes
from routes.topic import main as topic_routes
from routes.reply import main as reply_routes
from routes.board import main as board_routes
from routes.message import main as mail_routes, mail
from routes.map import main as map_routes
from routes.calendar import main as calendar_routes

# blueprint is in __init__, need all its dependency
# 导入相关 api 路由
from routes.api import api_topic
from routes.api import main as api_routes
# 导入相关 chat 路由
from routes.chat import chat_events, chat_main
from routes.chat import main as chatroom_routes

from routes.admin import admin

from routes.chat.chat_events import socketio


def register_routes(app):
    """
    在 flask 中，模块化路由的功能由 蓝图（Blueprints）提供
    蓝图可以拥有自己的静态资源路径、模板路径（现在还没涉及）
    用法如下
    """
    # 注册蓝图
    # 有一个 url_prefix 可以用来给蓝图中的每个路由加一个前缀

    app.register_blueprint(index_routes)
    app.register_blueprint(topic_routes, url_prefix='/topic')
    app.register_blueprint(reply_routes, url_prefix='/reply')
    app.register_blueprint(board_routes, url_prefix='/board')
    app.register_blueprint(mail_routes, url_prefix='/mail')
    # 蓝图注册在 __init__.py 里面, 因此需要导入其他相关包
    app.register_blueprint(api_routes, url_prefix='/api')
    app.register_blueprint(chatroom_routes, url_prefix='/chatroom')
    app.register_blueprint(map_routes, url_prefix='/map')
    app.register_blueprint(calendar_routes, url_prefix='/calendar')


app = Flask(__name__)

app.secret_key = 'infs3202'

# set sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(app.root_path, 'db', 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = 'secret!'


# init app
db.init_app(app)
mail.init_app(app)
admin.init_app(app)
socketio.init_app(app)

register_routes(app)


# 自动 reload jinja
app.jinja_env.auto_reload = True
app.jinja_env.globals.update(current_user=current_user)

app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


if __name__ == '__main__':
    context = ('cert.crt', 'key.key')
    config = dict(
        # app=app,
        debug=True,
        host='0.0.0.0',
        port=4000,
        # ssl_context='adhoc',
    )
    app.run(**config)
