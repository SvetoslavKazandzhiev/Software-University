from collections import deque

fireworks_effect = deque([int(x) for x in input().split(', ')])
explosive_power = deque([int(x) for x in input().split(', ')])

fireworks = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0,
}

is_done = False
is_enough = False
while fireworks_effect or explosive_power:
    if len(fireworks_effect) > 0:
        if fireworks_effect[0] <= 0:
            fireworks_effect.popleft()
            continue
    else:
        break
    if len(explosive_power) > 0:
        if explosive_power[-1] <= 0:
            explosive_power.pop()
            continue
    else:
        break
    if fireworks_effect[0] > 0 and explosive_power[-1] > 0:
        sum_of_first_last = fireworks_effect[0] + explosive_power[-1]
        if sum_of_first_last % 3 == 0 and sum_of_first_last % 5 != 0:
            fireworks['Palm Fireworks'] += 1
            fireworks_effect.popleft()
            explosive_power.pop()
            continue
        if sum_of_first_last % 3 != 0 and sum_of_first_last % 5 == 0:
            fireworks['Willow Fireworks'] += 1
            fireworks_effect.popleft()
            explosive_power.pop()
        if sum_of_first_last % 3 == 0 and sum_of_first_last % 5 == 0:
            fireworks['Crossette Fireworks'] += 1
            fireworks_effect.popleft()
            explosive_power.pop()
        if sum_of_first_last % 3 != 0 and sum_of_first_last % 5 != 0:
            fireworks_effect[0] -= 1
            fireworks_effect.append(fireworks_effect.popleft())

    if fireworks['Palm Fireworks'] >= 3 and fireworks['Willow Fireworks'] >= 3 and fireworks['Crossette Fireworks'] >= 3:
        is_enough = True
        break

if is_enough:
    print('Congrats! You made the perfect firework show!')
else:
    print("Sorry. You can’t make the perfect firework show.")

if len(fireworks_effect) > 0:
    print(f"Fireworks Effect left: {', '.join(map(str, fireworks_effect))}")

if len(explosive_power) > 0:
    print(f"Explosive Power left: {', '.join(map(str, explosive_power))}")

for key, val in fireworks.items():
    print(f'{key}: {val}')