from collections import deque

bomb_effects = deque(int(x) for x in input().split(", "))
bomb_casings = deque(int(x) for x in input().split(", "))

datura_Bombs = 0
cherry_Bombs = 0
smoke_Decoy_Bombs = 0
is_pouch = False
is_casing_empty = False
is_effects_empty = False
while bomb_effects:
    if bomb_effects[0] + bomb_casings[-1] == 40:
        datura_Bombs += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    elif bomb_effects[0] + bomb_casings[-1] == 60:
        cherry_Bombs += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    elif bomb_effects[0] + bomb_casings[-1] == 120:
        smoke_Decoy_Bombs += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    else:
        bomb_casings[-1] -= 5
    if datura_Bombs >= 3 and cherry_Bombs >= 3 and smoke_Decoy_Bombs >=3:
        is_pouch = True
        break
    if len(bomb_effects) == 0:
        is_effects_empty = True
    if len(bomb_casings) == 0:
        is_casing_empty = True
    if not bomb_casings:
        break

if is_pouch:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if is_effects_empty:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join(map(str, bomb_effects))}")
if is_casing_empty:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join(map(str, bomb_casings))}")
print(f"Cherry Bombs: {cherry_Bombs}")
print(f"Datura Bombs: {datura_Bombs}")
print(f"Smoke Decoy Bombs: {smoke_Decoy_Bombs}")
