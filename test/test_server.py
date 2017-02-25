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

    def route_api(self):
        # request /api
        app.testing = True
        client = app.test_client()
        r = client.get('/api')
        return r

    def route_api_getResult(self):
        # request /api/getResult
        app.testing = True
        client = app.test_client()
        r = client.post('/api/getResult',data={'text': '需要注意的是'}, follow_redirects=True)
        return r
    def test_route(self):
        # test /api and /api/getResult
        print(self.route_api_getResult().data)
        assert isinstance(json.loads(self.route_api().data.decode('utf-8')), (object))

        assert isinstance(json.loads(self.route_api_getResult().data.decode('utf-8')), (object))

        # print 'route ok'


if __name__ == '__main__':
    unittest.main()
