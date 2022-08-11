import datetime
import os

import jinja2.exceptions
from flask import request, redirect, url_for, render_template, Response, session, abort, send_from_directory

from .models import count, Seed, commit, Room, db_session, Command, UUID, uuid4
from worlds.AutoWorld import AutoWorldRegister
from . import app, cache


def get_world_theme(game_name: str):
    if game_name in AutoWorldRegister.world_types:
        return AutoWorldRegister.world_types[game_name].web.theme
    return 'grass'


@app.before_request
def register_session():
    session.permanent = True  # technically 31 days after the last visit
    if not session.get("_id", None):
        session["_id"] = uuid4()  # uniquely identify each session without needing a login


@app.errorhandler(404)
@app.errorhandler(jinja2.exceptions.TemplateNotFound)
def page_not_found(err):
    return render_template('404.html'), 404


# Start Playing Page
@app.route('/start-playing')
def start_playing():
    return render_template(f"startPlaying.html")


@app.route('/weighted-settings')
def weighted_settings():
    return render_template(f"weighted-settings.html")


# Player settings pages
@app.route('/games/<string:game>/player-settings')
def player_settings(game):
    return render_template(f"player-settings.html", game=game, theme=get_world_theme(game))


# Game Info Pages
@app.route('/games/<string:game>/info/<string:lang>')
def game_info(game, lang):
    return render_template('gameInfo.html', game=game, lang=lang, theme=get_world_theme(game))


# List of supported games
@app.route('/games')
def games():
    worlds = {}
    for game, world in AutoWorldRegister.world_types.items():
        if not world.hidden:
            worlds[game] = world
    return render_template("supportedGames.html", worlds=worlds)


@app.route('/tutorial/<string:game>/<string:file>/<string:lang>')
def tutorial(game, file, lang):
    return render_template("tutorial.html", game=game, file=file, lang=lang, theme=get_world_theme(game))


@app.route('/tutorial/')
def tutorial_landing():
    worlds = {}
    for game, world in AutoWorldRegister.world_types.items():
        if not world.hidden:
            worlds[game] = world
    return render_template("tutorialLanding.html")


@app.route('/faq/<string:lang>/')
def faq(lang):
    return render_template("faq.html", lang=lang)


@app.route('/glossary/<string:lang>/')
def terms(lang):
    return render_template("glossary.html", lang=lang)


@app.route('/seed/<suuid:seed>')
def view_seed(seed: UUID):
    seed = Seed.get(id=seed)
    if not seed:
        abort(404)
    return render_template("viewSeed.html", seed=seed, slot_count=count(seed.slots))


@app.route('/new_room/<suuid:seed>')
def new_room(seed: UUID):
    seed = Seed.get(id=seed)
    if not seed:
        abort(404)
    room = Room(seed=seed, owner=session["_id"], tracker=uuid4())
    commit()
    return redirect(url_for("host_room", room=room.id))


def _read_log(path: str):
    if os.path.exists(path):
        with open(path, encoding="utf-8-sig") as log:
            yield from log
    else:
        yield f"Logfile {path} does not exist. " \
              f"Likely a crash during spinup of multiworld instance or it is still spinning up."


@app.route('/log/<suuid:room>')
def display_log(room: UUID):
    room = Room.get(id=room)
    if room is None:
        return abort(404)
    if room.owner == session["_id"]:
        return Response(_read_log(os.path.join("logs", str(room.id) + ".txt")), mimetype="text/plain;charset=UTF-8")
    return "Access Denied", 403


@app.route('/room/<suuid:room>', methods=['GET', 'POST'])
def host_room(room: UUID):
    room = Room.get(id=room)
    if room is None:
        return abort(404)
    if request.method == "POST":
        if room.owner == session["_id"]:
            cmd = request.form["cmd"]
            if cmd:
                Command(room=room, commandtext=cmd)
                commit()

    with db_session:
        room.last_activity = datetime.utcnow()  # will trigger a spinup, if it's not already running

    return render_template("hostRoom.html", room=room)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/discord')
def discord():
    return redirect("https://discord.gg/archipelago")


@app.route('/datapackage')
@cache.cached()
def get_datapackage():
    """A pretty print version of /api/datapackage"""
    from worlds import network_data_package
    import json
    return Response(json.dumps(network_data_package, indent=4), mimetype="text/plain")


@app.route('/index')
@app.route('/sitemap')
def get_sitemap():
    available_games = []
    for game, world in AutoWorldRegister.world_types.items():
        if not world.hidden:
            available_games.append(game)
    return render_template("siteMap.html", games=available_games)
