from flask import Blueprint

bp = Blueprint('root', __name__)


@bp.route("/healthz")
def defcoisa():
    """show health
    """
    return {"status": "ok"}, 200
