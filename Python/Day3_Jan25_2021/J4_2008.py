def prefixToPostfix(expression):
    
    return postfix

while True:
    exp = input()
    if exp.isdigit():
        if int(exp)==0:
            break
    postfix = prefixToPostfix(exp)
    print(postfix)