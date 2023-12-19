from flask import Flask, render_template, request, url_for, redirect
from werkzeug.exceptions import BadRequest
from .views import crud
from os import getenv
from .models import models
from flask_migrate import (
    Migrate,
    migrate as migrate_command,
    upgrade as upgrade_command,
)

app = Flask(__name__)
CONFIG_NAME = getenv("CONFIG_NAME", "DevelopmentConfig")
app.config.from_object(f"config.{CONFIG_NAME}")

models.db.init_app(app)
migrate = Migrate(app, models.db)


def create_migration():
    with app.app_context():
        migrate_command()


@app.cli.command("apply-migrations")
def run_migration():
    with app.app_context():
        upgrade_command()


@app.get("/", endpoint="index")
def get_home_page():
    return render_template("base.html")


@app.get("/", endpoint="list")
def get_users_list():
    return render_template(
        "users.html",
        users=crud.get_users_list(),
    )


@app.get("/<int:user_id_id>/", endpoint="details")
def get_user_by_id_or_raise(user_id: int):
    user: models.User = crud.get_user_by_id(user_id)

    return render_template(
        "user_info.html",
        user=user,
    )


@app.route("/create/", endpoint="create", methods=["GET", "POST"])
def create_new_user():
    if request.method == "GET":
        return render_template("create.html")

    name = request.form.get("user_name", "").strip()
    username = request.form.get("username", "").strip()
    email = request.form.get("email", "").strip()
    if not name or not username or not email:
        raise BadRequest("`username`, `name`, `email` fields required")

    user = crud.create_user(name=name, username=username, email=email)
    url = url_for("base")
    return redirect(url)


if __name__ == "__main__":
    app.run(port=8000, debug=False)
