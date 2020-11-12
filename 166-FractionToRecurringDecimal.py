import unittest


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        negative = False

        # For simplicity, we will convert all numbers to positive values first.
        # (Technically, should convert to negative, since there are more negative int than positive ones. In python this is not an issue, since numbers don't have bounds)
        if numerator < 0:
            negative = not negative
            numerator = -numerator

        if denominator < 0:
            negative = not negative
            denominator = -denominator

        quotient = numerator // denominator
        remainder = numerator % denominator

        # As we resolve the remainders by long division, we keep track of which remainders has been seened before,
        # and at what index of the fraction string the division occurs.
        # cache is a mapping from remainders to indices
        cache = {}

        fraction = ""
        pos = 0
        while remainder != 0:
            remainder *= 10
            if remainder in cache:
                fraction = fraction[:cache[remainder]] + '(' + fraction[cache[remainder]:] + ')'
                break
            else:
                cache[remainder] = pos
                fraction += str(remainder // denominator)
                remainder = remainder % denominator
                pos += 1

        if fraction == "":
            final_ans = str(quotient)
        else:
            final_ans = str(quotient) + '.' + fraction

        if negative and final_ans != '0':
            final_ans = '-' + final_ans

        return final_ans


class TestDecimal(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_input1(self):
        self.assertEqual(self.sol.fractionToDecimal(2, 3), '0.(6)')

    def test_input2(self):
        self.assertEqual(self.sol.fractionToDecimal(2, 3), '0.(6)')

    def test_input1_negative(self):
        self.assertEqual(self.sol.fractionToDecimal(4, 333), '0.(012)')

    def test_no_decimal(self):
        self.assertEqual(self.sol.fractionToDecimal(33, 3), '11')

    def test_zero(self):
        self.assertEqual(self.sol.fractionToDecimal(0, 3), '0')


if __name__ == '__main__':
    unittest.main()