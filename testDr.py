import unittest

from app import Dice_Roller


class TestDR(unittest.TestCase):
    def test_get_score(self):
        d = Dice_Roller(3)
        d.values = [1, 1, 1]
        self.assertEqual(d.determine_points(), 500)

    def test_get_score_100(self):
        d = Dice_Roller(3)
        d.values = [1, 3, 3]
        self.assertEqual(d.determine_points(), 100)


if __name__ == "__main__":
    unittest.main()