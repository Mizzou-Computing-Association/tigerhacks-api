# -*- coding: utf-8 -*-

import json
import logging

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

logger = logging.getLogger(__name__)

blueprint = Blueprint("admin", __name__, url_prefix="/admin")

@blueprint.route("/healthcheck", methods=["GET"])
@blueprint.route("/status", methods=["GET"])
@blueprint.route("/ping", methods=["GET"])
@blueprint.route("/", methods=["GET"])
def admin_home():
    try:
        if request.headers['X-TigerHacks-Admin-Key'] != current_app.admin_key:
                logger.error("Unauthorized request")
                return Response(
                    response=json.dumps({"status": "error", "msg": "Invalid administrator key given"}), status=401, mimetype="application/json"
                )
    except KeyError as e:
        logger.error("No administrator key given")
        return Response(
            response=json.dumps({"status": "error", "msg": "No administrator key given"}), status=400, mimetype="application/json"
        )

    return Response(
        response=json.dumps({"status": "OK", "is_admin": "true"}), status=200, mimetype="application/json"
    )

@blueprint.route("/registrations", methods=["GET"])
def registrations():
    try:
        if request.headers['X-TigerHacks-Admin-Key'] != current_app.admin_key:
                logger.error("Unauthorized request")
                return Response(
                    response=json.dumps({"status": "error", "msg": "Invalid administrator key given"}), status=401, mimetype="application/json"
                )
    except KeyError as e:
        logger.error("No administrator key given")
        return Response(
            response=json.dumps({"status": "error", "msg": "No administrator key given"}), status=400, mimetype="application/json"
        )

    result = pd.read_sql(s.sql.text("""
        SELECT * FROM registrations
    """), current_app.dbconn)
    response = result.to_json(orient='records', date_format='iso', date_unit='ms')
    return Response(
        response=response, status=200, mimetype="application/json"
    )

