import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        self.assertEqual(katas.add(3,5), 3+5)

    def test_multiply(self):
        self.assertEqual(katas.multiply(2,4), 2*4)

    def test_power(self):
        self.assertEqual(katas.power(9,2), 9 ** 2)

    def test_factorial(self):
        self.assertEqual(katas.factorial(5), 120)

    def test_fibonacci(self):
        self.assertEqual(katas.fibonacci(10), 34)

if __name__ == '__main__':
    unittest.main()
