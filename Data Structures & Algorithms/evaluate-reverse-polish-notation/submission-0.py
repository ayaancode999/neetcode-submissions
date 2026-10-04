class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # put numbers in temp bucket stack
        stack = []
        for char in tokens:
            if char == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
            elif char == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))
            elif char == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b)
            elif char == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            else:
                stack.append(int(char))
        return stack[0]


        # use operation whenever finding one using if statement

        # replace stack with product of numbers

        # return product after all iterations