import math
import unittest

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        OPERATORS = ['+', '-', '*', '/']
        stack = []
        for t in tokens:
            if t in OPERATORS:
                arg2 = int(stack.pop())
                arg1 = int(stack.pop())
                res = 0
                if t == '+':
                    res = arg1 + arg2
                elif t == '-':
                    res = arg1 - arg2
                elif t == '*':
                    res = arg1 * arg2
                elif t == '/':
                    res = arg1 / arg2
                    res = math.ceil(res) if res < 0 else math.floor(res)
                else:
                    return -1

                stack.append(res)
            else:
                stack.append(t)

        return stack.pop()


class TestRPN(unittest.TestCase):
    def setUp(self) -> None:
        self.sol = Solution()

    def test_input1(self):
        self.assertEqual(self.sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]), 22)


if __name__ == '__main__':
    unittest.main()