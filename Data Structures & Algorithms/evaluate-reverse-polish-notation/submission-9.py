import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:


        stack = []
        ops = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,

            "/": operator.truediv,
        }


        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                rightOperator = stack.pop()
                leftOperator = stack.pop()
                stack.append(int(ops[token](leftOperator, rightOperator)))
        
        
        return stack[0]