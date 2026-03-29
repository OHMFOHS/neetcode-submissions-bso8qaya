class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c in "+-*/":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if c == '+':
                    stack.append(num1 + num2)
                elif c == '-':
                    stack.append(num2 - num1)
                elif c == '*':
                    stack.append(num1 * num2)
                elif c == '/':
                    stack.append(int(float(num2) / num1))
            else:
                stack.append(int(c))
        return stack[0]
