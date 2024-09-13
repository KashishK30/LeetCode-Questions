class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []

        # Iterate over each character in the expression
        for char in expression:
            if char == ')': # If closing character is found, we evaluate the sub-expression
                sub_exp = []
                while stack[-1] != '(':
                    sub_exp.append(stack.pop())
                stack.pop() # Remove the '(' char
                operator = stack.pop() # Get the operator before '('
            
                if operator == '!':
                    stack.append('t' if sub_exp[0] == 'f' else 'f')
                elif operator == '&':
                    stack.append('t' if all(x == 't' for x in sub_exp) else 'f')
                elif operator == '|':
                    stack.append('t' if any(x == 't' for x in sub_exp) else 'f')
            elif char != ',':
                # Push any non-parenthesis character (except commas) in the stack
                stack.append(char)

        #The result will be the only character left in the stack
        return stack[0] == 't'
    

                
