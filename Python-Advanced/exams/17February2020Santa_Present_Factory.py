from collections import deque

materials = deque([int(x) for x in input().split()])
magic = deque([int(x) for x in input().split()])

toys = {
    "Doll": 0,
    "Wooden train": 0,
    "Teddy bear": 0,
    "Bicycle": 0
}

is_done = False
while materials:
    if materials[-1] * magic[0] == 150:
        toys["Doll"] +=1
        materials.pop()
        magic.popleft()
    elif materials[-1] * magic[0] == 250:
        toys["Wooden train"] +=1
        materials.pop()
        magic.popleft()
    elif materials[-1] * magic[0] == 300:
        toys["Teddy bear"] +=1
        materials.pop()
        magic.popleft()
    elif materials[-1] * magic[0] == 400:
        toys["Bicycle"] +=1
        materials.pop()
        magic.popleft()
    elif materials[-1] * magic[0] < 0:
        res = materials[-1] + magic[0]
        materials.pop()
        magic.popleft()
        materials.append(res)
    elif materials[-1] == 0:
        materials.pop()
    elif magic[0] == 0:
        magic.pop()
    else:
        magic.popleft()
        materials[-1] += 15
    if len(magic) == 0:
        break
    if toys["Doll"] >= 1 and toys["Wooden train"] >= 1:
        is_done = True

    elif toys["Teddy bear"] >= 1 and toys["Bicycle"] >= 1:
        is_done = True

    else:
        is_done = False
if is_done:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if len(materials) >  0:
    materials = reversed(materials)
    print(f"Materials left: {', ' .join(map(str, materials))}")
if len(magic) > 0:
    magic = reversed(magic)
    print(f"Magic left: {', ' .join(map(str, magic))}")

toys = sorted(toys.items(), key=lambda x: (x[0]))

for x, y in toys:
    if y > 0:
       print(f"{x}: {y}")
