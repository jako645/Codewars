import unittest

from Python.ExplodingRobots import will_robots_collide

class TestRobotCollision(unittest.TestCase):
    def test_collision(self):
        self.assertTrue(will_robots_collide(0, 0, 1, 0, "UL"))
        self.assertTrue(will_robots_collide(5, 1, 1, 5, "LRUURLDDLR"))
        self.assertTrue(will_robots_collide(4, 2, 3, 2, "R"))
        self.assertTrue(will_robots_collide(8, 6, 8, 6, ""))

    def test_no_collision(self):
        self.assertFalse(will_robots_collide(0, 0, 0, 1, "LRLR"))
        self.assertFalse(will_robots_collide(5, 0, 1, 5, "LRUURLDDLR"))
        self.assertFalse(will_robots_collide(4, 2, 3, 2, "D"))
        self.assertFalse(will_robots_collide(8, 6, 8, 7, ""))
