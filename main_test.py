#!/usr/bin/env python
# -*- coding: utf-8 -*-

import main
import unittest


class MainTestCase(unittest.TestCase):

    def test_index(self):
        main.app.testing = True
        client = main.app.test_client()

        r = client.get('/')
        assert r.status_code == 200
        assert 'Hello World' in r.data.decode('utf-8')
        print 'hello'

if __name__ == '__main__':
    unittest.main()
