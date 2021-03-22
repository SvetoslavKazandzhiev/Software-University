from math import floor

user_input = list(input().split())
result = None
numbers = []
for i in user_input:
    operand = None

    if i not in ["+", "-", "*", "/"]:
        numbers.append(int(i))
    else:
        operand = i
        if result is None:

            result = numbers[0]
            del numbers[0]

        for num in numbers:
            if operand == "+":
                result += num
            elif operand == "-":
                result -= num
            elif operand == "*":
                result *= num
            elif operand == "/":
                result /= num
                result = floor(result)
        numbers = []
print(result)