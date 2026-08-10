import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        result = 0
        stack = []
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,

            "/": operator.truediv,
        }

        if len(tokens) == 1:
            return int(tokens[0])

        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                rightOperator = stack.pop()
                leftOperator = stack.pop()
                result = int(ops[token](leftOperator, rightOperator))
                stack.append(result)
        
        
        return result