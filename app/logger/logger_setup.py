import logging

import structlog
from structlog.stdlib import LoggerFactory


def setup():

    logging.basicConfig(level=logging.INFO, format="%(message)s")
    structlog.configure(
        processors=[
            structlog.processors.JSONRenderer(),
            structlog.processors.add_log_level,
            # structlog.contextvars.merge_contextvars,
            # structlog.processors.StackInfoRenderer(),
            # structlog.dev.set_exc_info,
            structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S"),
        ],
        context_class=dict,
        # logger_factory=structlog.stdlib.LoggerFactory(),
        # wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )


def configure_logging() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    structlog.configure(
        processors=[
            structlog.processors.KeyValueRenderer(key_order=["event", "status"]),
            structlog.processors.JSONRenderer(),
        ],
        context_class=dict,
        # logger_factory=LoggerFactory,
        cache_logger_on_first_use=True,
    )
