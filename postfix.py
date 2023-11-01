def evaluate(exp):
    stack=[]
    for i in exp:
        if i in "0123456789+-*/":
            if i in ['+','-','*','/']:
                op2=stack.pop()
                op1=stack.pop()
                if i=='+':
                    stack.append(op1+op2)
                elif i=='-':
                    stack.append(op1-op2)
                elif i=='*':
                    stack.append(op1*op2)
                elif i=='/':
                    stack.append(op1//op2)
            else:
                stack.append(int(i))
        else:
            return False
    return stack.pop()
if __name__=="__main__":

    if evaluate("23>gdfg58$^^&")==False:
        print("Invalid Expression") 