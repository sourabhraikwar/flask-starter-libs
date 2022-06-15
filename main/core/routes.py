from flask import Blueprint, render_template

core_bp = Blueprint(
    "core_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static/core",
)


@core_bp.route("/")
def index():
    return render_template("index.html")
