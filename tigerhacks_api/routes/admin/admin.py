# -*- coding: utf-8 -*-

import json
import sqlalchemy as s
import pandas as pd

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

from tigerhacks_api import app

blueprint = Blueprint("admin", __name__, url_prefix="/admin")

@blueprint.route("/healthcheck", methods=["GET"])
@blueprint.route("/status", methods=["GET"])
@blueprint.route("/ping", methods=["GET"])
@blueprint.route("/", methods=["GET"])
def home():
    return Response(
        response=json.dumps({"status": "OK", "admin": "true"}), status=200, mimetype="application/json"
    )

@blueprint.route("/registrations", methods=["GET"])
def register():
    result = pd.read_sql(s.sql.text("""
        SELECT * FROM registrations
    """), current_app.db_engine)
    response = result.to_json(orient='records', date_format='iso', date_unit='ms')
    return Response(
        response=response, status=501, mimetype="application/json"
    )
