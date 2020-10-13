"""Main application package."""
import logging
import coloredlogs

from tigerhacks_api.app import create_app

logger = logging.getLogger(__name__)
simple_format_string = "[%(process)d] %(name)s [%(levelname)s] %(message)s"
coloredlogs.install(level=logging.DEBUG, logger=logger, fmt=simple_format_string)

app = create_app()