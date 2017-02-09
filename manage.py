#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from flask_script import Manager
from creadr.app import app

manager = Manager(app)

@manager.command
def runserver():

    """Overrides default runserver()"""

    app.run(host='127.0.0.1', port=8080, debug=True)

@manager.command
def test():

    """Runs the unit tests without test coverage."""

    tests = unittest.TestLoader().discover('test', pattern='test_*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def cov():

    # TODO:
    """Runs the unit tests with coverage."""
    pass


@manager.command
def create_db():

    # TODO:
    """Creates the db tables."""
    pass


@manager.command
def drop_db():

    # TODO:
    """Drops the db tables."""
    pass


if __name__ == '__main__':
    manager.run()
