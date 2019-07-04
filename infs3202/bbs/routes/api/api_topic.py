from flask import (
    jsonify,
)
from routes.api import main
from models.topic import Topic


@main.route('/topic/all')
def topic_all():
    topics = Topic.all()
    ts = []
    for t in topics:
        dictret = dict(t.__dict__)
        dictret.pop('_sa_instance_state', None)
        ts.append(dictret)
    return jsonify(ts)


@main.route("/topic/title/all")
def title_all():
    topics = Topic.all()
    titles = []
    for t in topics:
        titles.append(t.title)
    return jsonify(titles)


