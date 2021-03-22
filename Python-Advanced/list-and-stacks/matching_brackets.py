def get_subexpression(exprression):
    s = []
    result = []
    for index in range(len(exprression)):
        ch = exprression[index]
        if ch == "(":
            s.append(index)
        elif ch == ")":
            start_index = s.pop()
            result.append(exprression[start_index:index + 1])
    return result

for subexpression in get_subexpression(input()):
    print(subexpression)