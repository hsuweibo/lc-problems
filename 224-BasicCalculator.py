operators = ['+', '-']


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Start processing at the first char after a bracket, and return the computed value and the index of the closing bracket
        def helper(s, start):
            # The stack stores the tokens (numbers and operators)
            stack = []

            i = start
            while i < len(s) and s[i] != ')':
                if s[i] == ' ':
                    i += 1
                elif s[i] in operators:
                    stack.append(s[i])
                    i += 1

                # If the current char is not an operator or blank space, it is a digit or an opening bracket
                else:
                    # Get the computed value of the bracketed expression, and increment i to the char after the closing bracket
                    if s[i] == '(':
                        res = helper(s, i + 1)
                        num = res[0]
                        i = res[1] + 1
                    # If the current char is a digit, obtain the full number
                    else:
                        num = 0
                        while i < len(s) and s[i].isdigit():
                            num = num * 10 + int(s[i])
                            i += 1

                    if len(stack) > 0 and stack[-1] in operators:
                        op = stack.pop()
                        left = stack.pop()
                        right = num

                        if op == '+':
                            stack.append(left + right)
                        elif op == '-':
                            stack.append(left - right)
                    else:
                        stack.append(num)

            return stack[-1], i

        return helper(s, 0)[0]
