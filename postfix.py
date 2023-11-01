def evaluate(exp):
    stack=[]
    for i in exp:
        if i in ['+']:
            pass
        else:
            stack.append(int(i))
    return stack.pop()