#!/usr/bin/env python

import unittest
from game.match import Match

class TestMatch(unittest.TestCase):
    def setUp(self):
        self.match = Match()

    def test_automatic_playing(self):
        self.assertTrue(self.match.automatic_playing())


if __name__ == '__main__':
    unittest.main()
