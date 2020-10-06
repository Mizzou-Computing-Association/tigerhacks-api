# -*- coding: utf-8 -*-

import json

from flask import (
    Blueprint,
    Response,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from tigerhacks_api.utils import flash_errors

blueprint = Blueprint("api", __name__)


@blueprint.route("/", methods=["GET", "POST"])
def home():
    return Response(
        response=json.dumps({"status": "OK"}), status=200, mimetype="application/json"
    )
