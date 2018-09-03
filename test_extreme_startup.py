import unittest
from extreme_startup import calculate_answer

class TestMyServer(unittest.TestCase):
    def test_level_1_yellow(self):
        answer = calculate_answer("What is the color of the sun?")
        self.assertEqual("Yellow", answer)

    def test_level_2_add_4(self):
        answer = calculate_answer("What is 2+2?")
        self.assertEqual("4", answer)
        answer = calculate_answer("What is 5+2?")
        self.assertEqual("7", answer)

