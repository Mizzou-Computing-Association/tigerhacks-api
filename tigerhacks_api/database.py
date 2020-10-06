# -*- coding: utf-8 -*-
"""Database module, including the SQLAlchemy database object and DB-related utilities."""

import sqlalchemy as s
import logging


logger = logging.getLogger(__name__)

def init_database_connection(app):

    database_connection_string = app.config['SQLALCHEMY_DATABASE_URI']

    engine = s.create_engine(database_connection_string, poolclass=s.pool.NullPool,
        connect_args={}, pool_pre_ping=True)

    try:
        engine.connect().close()
        return engine
    except s.exc.OperationalError as e:
        logger.error("Unable to connect to the database. Terminating...")
        raise(e)

    return engine
