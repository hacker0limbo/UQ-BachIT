from flask import (
    redirect,
    url_for,
    request,
)

from flask_admin import (
    Admin,
    BaseView,
    expose,
)
from flask_admin.contrib.sqla import ModelView

from routes import current_user

from models.base_model import db
from models.topic import Topic
from models.board import Board
from models.user import User
from models.reply import Reply


class WarningView(BaseView):
    @expose('/')
    def index(self):
        return self.render('/admin/index.html')


class AdminView(ModelView):

    def is_accessible(self):
        u = current_user()
        if u is not None and u.username == 'limbo':
            return True

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('index.login', next=request.url))


admin = Admin(name='bbs manage', template_mode='bootstrap3')

admin.add_view(WarningView(name='Warning', endpoint='warning'))

admin.add_view(AdminView(Board, db.session))
admin.add_view(AdminView(User, db.session))
admin.add_view(AdminView(Reply, db.session))