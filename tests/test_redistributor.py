import unittest
from blame_redistributor.engine import BlameDistributor


class TestBlameDistributor(unittest.TestCase):
    def setUp(self):
        self.team = ["alice", "bob", "carol"]
        self.engine = BlameDistributor(self.team)

    def test_gini_coefficient_equal(self):
        equal_dist = {"alice": 0.33, "bob": 0.33, "carol": 0.33}
        gini = self.engine.compute_gini_coefficient(equal_dist)
        self.assertLess(gini, 0.05)

    def test_culpability_calculation(self):
        lines = ["alice", "alice", "bob", "carol"]
        culp = self.engine.calculate_culpability(lines)
        self.assertEqual(culp["alice"], 0.5)
        self.assertEqual(culp["bob"], 0.25)
        self.assertEqual(culp["carol"], 0.25)

    def test_redistribution_length_preserved(self):
        lines = [(1, "alice", "x = 1"), (2, "alice", "y = 2")]
        redistributed = self.engine.redistribute(lines, fairness_coefficient=1.0)
        self.assertEqual(len(redistributed), 2)
        for _, author, _ in redistributed:
            self.assertIn(author, self.team)


if __name__ == '__main__':
    unittest.main()
