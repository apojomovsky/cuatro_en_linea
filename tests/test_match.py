#!/usr/bin/env python
import unittest
from game.match import Match
from game.player import Player

class TestMatch(unittest.TestCase):
    def setUp(self):
        self.match = Match()

    def test_next_turn(self):
        self.assertEqual(self.match.whos_turn(), 'red')
        self.match.next_turn()
        self.assertEqual(self.match.whos_turn(), 'blue')
        self.match.next_turn()
        self.assertEqual(self.match.whos_turn(), 'red')
