'''
This problem was asked by Google.

Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.

Do this faster than the naive method of repeated multiplication.

For example, pow(2, 10) should return 1024.
'''
import unittest


def fast_pow(no, power):
    ans = no
    rem = 1
    while power > 1:
        if power % 2 == 1:
            rem *= ans
        power //= 2
        if power > 0:
            ans *= ans
    ans *= rem
    return ans


class FastPowerTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(2048, fast_pow(2, 11))

    def test_2(self):
        self.assertEqual(1594323, fast_pow(3, 13))


if __name__ == "__main__":

    unittest.main()
