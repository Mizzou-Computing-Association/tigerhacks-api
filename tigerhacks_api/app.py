# -*- coding: utf-8 -*-
"""The app module, containing the app factory function."""
import logging
import sys

from flask import Flask, render_template
import sqlalchemy as s

from tigerhacks_api import commands, routes
from tigerhacks_api.extensions import bcrypt, cache, csrf_protect, db
from tigerhacks_api.database import init_database_connection
from tigerhacks_api.utils import generate_api_key

logger = logging.getLogger(__name__)


def create_app(config_object="tigerhacks_api.settings"):
    """Create application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__.split(".")[0])
    logger.info("Flask app initialized")

    app.config.from_object(config_object)
    logger.info("Config loaded")

    app.dbconn = init_database_connection(app)
    logger.info("Database connection successful")

    register_extensions(app)
    register_blueprints(app)
    register_shellcontext(app)
    register_commands(app)
    configure_logger(app)
    logger.info("Extensions loaded")

    configure_api_key(app)
    configure_admin_key(app)
    logger.info("API keys configured")

    logger.info("Request logs will now take over.")
    return app


def register_extensions(app):
    """Register Flask extensions."""
    bcrypt.init_app(app)
    cache.init_app(app)
    db.init_app(app)
    csrf_protect.init_app(app)
    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(routes.views.blueprint)
    app.register_blueprint(routes.admin.blueprint)
    return None


def register_shellcontext(app):
    """Register shell context objects."""

    def shell_context():
        """Shell context objects."""
        return {"db": db}

    app.shell_context_processor(shell_context)


def register_commands(app):
    """Register Click commands."""
    app.cli.add_command(commands.test)
    app.cli.add_command(commands.lint)


def configure_logger(app):
    """Configure loggers."""
    handler = logging.StreamHandler(sys.stdout)
    if not app.logger.handlers:
        app.logger.addHandler(handler)

def configure_api_key(app):
    api_key = generate_api_key()
    get_api_key_sql = s.sql.text("""
        SELECT value FROM settings WHERE setting='api_key';
    """)
    current_key = app.dbconn.execute(get_api_key_sql).fetchone()[0]
    if current_key == "invalid_key":
        update_api_key_sql = s.sql.text("""
            UPDATE settings SET VALUE = :api_key WHERE setting='api_key';
        """)

        app.dbconn.execute(update_api_key_sql, api_key=api_key)
        logger.info(f"API key has been set to: {api_key}")
        app.api_key = api_key
    else:
        logger.warning(f"Existing API key found: {current_key}")
        app.api_key = current_key

def configure_admin_key(app):
    admin_key = generate_api_key()
    get_admin_key_sql = s.sql.text("""
        SELECT value FROM settings WHERE setting='admin_key';
    """)
    current_key = app.dbconn.execute(get_admin_key_sql).fetchone()[0]

    if current_key == "invalid_key":
        update_admin_key_sql = s.sql.text("""
            UPDATE settings SET VALUE = :admin_key WHERE setting='admin_key';
        """)

        app.dbconn.execute(update_admin_key_sql, admin_key=admin_key)
        logger.info(f"Admin key has been set to: {admin_key}")
        app.admin_key = admin_key
    else:
        logger.warning(f"Existing admin key found: {current_key}")
        app.admin_key = current_key