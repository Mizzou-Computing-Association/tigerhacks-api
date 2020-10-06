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
from tigerhacks_api import app

blueprint = Blueprint("api", __name__)

@blueprint.route("/healthcheck", methods=["GET"])
@blueprint.route("/status", methods=["GET"])
@blueprint.route("/ping", methods=["GET"])
@blueprint.route("/", methods=["GET"])
def home():
    return Response(
        response=json.dumps({"status": "OK"}), status=200, mimetype="application/json"
    )

@blueprint.route("/register", methods=["POST"])
def register():
    return Response(
        response=json.dumps({"status": "NOT IMPLEMENTED"}), status=501, mimetype="application/json"
    )
