#!/usr/bin/env python
# -*- coding: utf-8 -*-

from creadr.app import app
import unittest
import json


class MainTestCase(unittest.TestCase):

    def test_templates(self):
        app.testing = True
        client = app.test_client()

        r = client.get('/')
        assert r.status_code == 200
        assert 'Pretty Cool' in r.data.decode('utf-8')

        r = client.get('/notExistURL')
        assert r.status_code == 404
        assert '404' in r.data.decode('utf-8')
        # print 'templates ok'

    def test_route(self):
        app.testing = True
        client = app.test_client()

        r = client.get('/api')
        assert isinstance(json.loads(r.data.decode('utf-8')), (object))
        # print 'route ok'



if __name__ == '__main__':
    unittest.main()
