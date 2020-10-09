# -*- coding: utf-8 -*-

import json
import sqlalchemy as s

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
    register_query = s.sql.text("""
        INSERT INTO
        `registrations`
            (`first_name`, `last_name`, `school`, `year`, `major`, `shirt_size`, `mailing_address`)
        VALUES
            (:first_name, :last_name, :school, :year, :major, :shirt_size, :mailing_address);

    """)

    try:
        current_app.db_engine.execute(register_query, **request.json)
        return Response(
            response=json.dumps({"status": "successful"}), status=200, mimetype="application/json"
        )
    except Exception as e:
        return Response(
            response=json.dumps({"status": "error", "msg": str(e)}), status=500, mimetype="application/json"
        )
