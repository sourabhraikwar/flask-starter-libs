from flask import Blueprint

core_bp = Blueprint("core_bp", __name__)


@core_bp.route("/")
def index():
    return "Hello Everyone"
