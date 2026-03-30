class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s == "+":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 + val1)
            elif s == "-":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 - val1)
            elif s == "*":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 * val1)
            elif s == "/":
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val2 / val1))
            else:
                stack.append(int(s))
            print(stack)

        return stack.pop()