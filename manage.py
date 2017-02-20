#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
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

    errno = pytest.main(args=['-v', './test'])
    return errno

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
