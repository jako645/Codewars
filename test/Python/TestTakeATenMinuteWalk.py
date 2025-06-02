import unittest

from Python.TakeATenMinuteWalk import is_valid_walk

class TestNumberOfDirections(unittest.TestCase):
    def test_too_few_directions(self):
        walk = ['n'] * 3
        self.assertFalse(is_valid_walk(walk))

    def test_too_many_directions(self):
        walk = ['n'] * 13
        self.assertFalse(is_valid_walk(walk))

    def test_boundary_number_of_directions(self):
        walk = ['n'] * 9
        self.assertFalse(is_valid_walk(walk))
        walk = ['n', 's'] * 5
        self.assertTrue(is_valid_walk(walk))
        walk = ['n'] * 11
        self.assertFalse(is_valid_walk(walk))

class TestReturnDirections(unittest.TestCase):
    def test_return_to_start_vertically(self):
        walk = ['n', 's'] * 5
        self.assertTrue(is_valid_walk(walk))

    def test_not_return_to_start_vertically(self):
        walk = ['n', 's'] * 4 + ['s', 's']
        self.assertFalse(is_valid_walk(walk))

    def test_return_to_start_horizontal(self):
        walk = ['w', 'e'] * 5
        self.assertTrue(is_valid_walk(walk))

    def test_not_return_to_start_horizontal(self):
        walk = ['w', 'e'] * 4 + ['e', 'e']
        self.assertFalse(is_valid_walk(walk))
