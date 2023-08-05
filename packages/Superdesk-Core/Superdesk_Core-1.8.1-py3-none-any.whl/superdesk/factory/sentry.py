
import logging
from raven.contrib.flask import Sentry
from raven.contrib.celery import register_signal, register_logger_signal


class SuperdeskSentry():
    """Sentry proxy that will do nothing in case sentry is not configured."""

    def __init__(self, app):
        if app.config.get('SENTRY_DSN'):
            app.config.setdefault('SENTRY_NAME', app.config.get('SERVER_NAME'))
            self.sentry = Sentry(app, register_signal=False, wrap_wsgi=False, logging=True, level=logging.WARNING)
            register_logger_signal(self.sentry.client)
            register_signal(self.sentry.client)
        else:
            self.sentry = None

    def captureException(self, exc_info=None, **kwargs):
        if self.sentry:
            self.sentry.captureException(exc_info, **kwargs)

    def captureMessage(self, message, **kwargs):
        if self.sentry:
            self.sentry.captureMessage(message, **kwargs)
