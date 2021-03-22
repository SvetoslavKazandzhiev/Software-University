def list_manipulator(*args):
    instructions = args[1]
    position = args[2]
    numbers = args[0]
    numbers_to_add =[]
    if len(args) > 3:
        numbers_to_add = list(args[3:])
        if instructions == "remove":
            if position == "end":
                return numbers[:0 - numbers_to_add[0]]
            else:
                return numbers[numbers_to_add[0]:]
        else:
            if position == "end":
                return numbers + numbers_to_add
            else:
                return numbers_to_add + numbers
    else:
        if position == "end":
            return numbers[:-1]
        else:
            return numbers[1:]



print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))