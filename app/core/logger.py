import logging
import sys
import structlog


def configure_logging():

    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        stream=sys.stdout,
    )

    structlog.configure(
        # context_class=structlog.threadlocal.wrap_dict(dict),
        # wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
        # logger_factory=structlog.stdlib.LoggerFactory(),
        # cache_logger_on_first_use=True,
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.JSONRenderer(),
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
        cache_logger_on_first_use=True,
    )

    return structlog.get_logger()


logger = configure_logging()


# structlog.configure(
#     processors=[
#         # If log level is too low, abort pipeline and throw away log entry.
#         structlog.stdlib.filter_by_level,
#         # Add the name of the logger to event dict.
#         # structlog.stdlib.add_logger_name,
#         # Add log level to event dict.
#         structlog.stdlib.add_log_level,
#         # Perform %-style formatting.
#         structlog.stdlib.PositionalArgumentsFormatter(),
#         # Add a timestamp in ISO 8601 format.
#         structlog.processors.TimeStamper(fmt="iso"),
#         # If the "stack_info" key in the event dict is true, remove it and
#         # render the current stack trace in the "stack" key.
#         structlog.processors.StackInfoRenderer(),
#         # If the "exc_info" key in the event dict is either true or a
#         # sys.exc_info() tuple, remove "exc_info" and render the exception
#         # with traceback into the "exception" key.
#         structlog.processors.format_exc_info,
#         # If some value is in bytes, decode it to a Unicode str.
#         structlog.processors.UnicodeDecoder(),
#         # Add callsite parameters.
#         structlog.processors.CallsiteParameterAdder(
#             {
#                 structlog.processors.CallsiteParameter.FILENAME,
#                 structlog.processors.CallsiteParameter.FUNC_NAME,
#                 structlog.processors.CallsiteParameter.LINENO,
#             }
#         ),
#         # Render the final event dict as JSON.
#         structlog.processors.JSONRenderer()
#     ],
#     # `wrapper_class` is the bound logger that you get back from
#     # get_logger(). This one imitates the API of `logging.Logger`.
#     wrapper_class=structlog.stdlib.BoundLogger,
#     # `logger_factory` is used to create wrapped loggers that are used for
#     # OUTPUT. This one returns a `logging.Logger`. The final value (a JSON
#     # string) from the final processor (`JSONRenderer`) will be passed to
#     # the method of the same name as that you've called on the bound logger.
#     logger_factory=structlog.stdlib.LoggerFactory(),
#     # Effectively freeze configuration after creating the first bound
#     # logger.
#     cache_logger_on_first_use=True,
# )
