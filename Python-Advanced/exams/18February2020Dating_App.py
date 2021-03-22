from collections import deque

males = deque([int(x) for x in input().split()])
females = deque([int(x) for x in input().split()])

matches = 0
while males and females:
    if males[-1] <= 0:
        males.pop()
        continue
    elif females[0] <= 0:
        females.popleft()
        continue
    else:
        if males[-1] % 25 == 0:
            males.pop()
            continue
        elif females[0] % 25 == 0:
            females.popleft()

            continue
        else:
            if males[-1] == females[0]:
                males.pop()
                females.popleft()
                matches += 1
                continue
            else:
                females.popleft()
                males[-1] -= 2
                continue


print(f"Matches: {matches}")
result = []

if males:
    while males:
        result.append(males.pop())
    print(f'Males left: {", ".join(map(str, result))}')
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join(map(str, females))}")
else:
    print("Females left: none")
