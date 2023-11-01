def evaluate(exp):
    stack=[]
    for i in exp:
        if i in ['+','-']:
            op2=stack.pop()
            op1=stack.pop()
            if i=='+':
                stack.append(op2+op1)
          
            
        else:
            stack.append(int(i))
    return stack.pop()