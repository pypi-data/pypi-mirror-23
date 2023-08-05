import argparse
import logging
import unittest

import django.test.runner
from django.utils import six

from django_admin_testutils.selenium import SeleniumTestCaseBase


class ActionSelenium(argparse.Action):
    """
    Validate the comma-separated list of requested browsers.
    """
    def __call__(self, parser, namespace, values, option_string=None):
        browsers = values.split(',')
        for browser in browsers:
            if browser.lower() in ("skip", "none"):
                continue
            try:
                SeleniumTestCaseBase.import_webdriver(browser)
            except ImportError:
                raise argparse.ArgumentError(
                    self, "Selenium browser specification '%s' is not valid." % browser)
        setattr(namespace, self.dest, browsers)


class NoFailFastUnexpectedSuccessTestResultMixin(object):
    """Overridden test result class that doesn't failfast on unexpected success"""

    def addUnexpectedSuccess(self, test):
        self.unexpectedSuccesses.append((test, 'Success'))
        if self.showAll:
            self.stream.writeln("unexpected success")
        elif self.dots:
            self.stream.write("u")
            self.stream.flush()

    def printErrors(self):
        super(NoFailFastUnexpectedSuccessTestResultMixin, self).printErrors()
        self.printErrorList('UNEXPECTED SUCCESS', self.unexpectedSuccesses)


class TextTestResult(NoFailFastUnexpectedSuccessTestResultMixin, unittest.TextTestResult):
    pass


class DebugSQLTextTestResult(
        NoFailFastUnexpectedSuccessTestResultMixin,
        django.test.runner.DebugSQLTextTestResult):

    def addUnexpectedSuccess(self, test):
        super(DebugSQLTextTestResult, self).addUnexpectedSuccess(test)
        self.debug_sql_stream.seek(0)
        self.unexpectedSuccesses[-1] += (self.debug_sql_stream.read(),)


class DiscoverRunner(django.test.runner.DiscoverRunner):
    """Overridden DiscoverRunner that doesn't failfast on unexpected success"""

    default_log_by_verbosity = False

    def __init__(self, **kwargs):
        self.log_by_verbosity = kwargs.pop('log_by_verbosity')
        browsers = kwargs.pop('selenium')
        if not browsers:
            try:
                SeleniumTestCaseBase.import_webdriver('phantomjs')
            except:
                browsers = ['skip']
            else:
                browsers = ['phantomjs']
        SeleniumTestCaseBase.browsers = browsers
        super(DiscoverRunner, self).__init__(**kwargs)

    def get_resultclass(self):
        return DebugSQLTextTestResult if self.debug_sql else TextTestResult

    @classmethod
    def add_arguments(cls, parser):
        super(DiscoverRunner, cls).add_arguments(parser)
        parser.add_argument(
            '--selenium', action=ActionSelenium, metavar='BROWSERS',
            help='A comma-separated list of browsers to run the Selenium '
                 'tests against. Defaults to "phantomjs".')
        parser.add_argument(
            '--%slog-by-verbosity' % ('no-' if cls.default_log_by_verbosity else ''),
            action=('store_false' if cls.default_log_by_verbosity else 'store_false'),
            default=cls.default_log_by_verbosity,
            dest='log_by_verbosity',
            help='%s matching log levels to the verbosity flag' % (
                'Disable' if cls.default_log_by_verbosity else 'Enable'))

    verbosity_log_levels = {
        0: logging.ERROR,
        1: logging.WARNING,
        2: logging.INFO,
        3: logging.DEBUG,
    }

    @property
    def log_level(self):
        return self.verbosity_log_levels[self.verbosity]

    def setup_test_environment(self, **kwargs):
        super(DiscoverRunner, self).setup_test_environment(**kwargs)
        from django.conf import settings
        if self.log_by_verbosity:
            loggers = settings.LOGGING.get('loggers') or {}
            for _, logger_opts in six.iteritems(loggers):
                if 'level' not in logger_opts:
                    continue
                level = logging._checkLevel(logger_opts['level'])
                if level > self.log_level:
                    logger_opts['level'] = logging.getLevelName(self.log_level)
