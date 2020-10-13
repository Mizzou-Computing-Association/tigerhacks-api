# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
import random
import string
import logging
import sqlalchemy as s

from flask import flash

logger = logging.getLogger(__name__)

def flash_errors(form, category="warning"):
    """Flash all errors for a form."""
    for field, errors in form.errors.items():
        for error in errors:
            flash(f"{getattr(form, field).label.text} - {error}", category)

def generate_api_key():
    """
    Generate and set a new Augur API key
    """
    key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))
    return key

