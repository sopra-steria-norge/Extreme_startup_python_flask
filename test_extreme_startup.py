import unittest
from extreme_startup import test_calculate_answer


class TestMyServer(unittest.TestCase):
    def test_level_1_yellow(self):
        answer = test_calculate_answer("What is the color of the sun?")
        self.assertEqual("Yellow", answer)

    def test_level_2(self):
        pass
