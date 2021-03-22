from collections import deque

paint_colors = deque(input().split())
main_colors = []
while paint_colors:
    if paint_colors[0] + paint_colors[-1] == "red" or paint_colors[-1] + paint_colors[0] == "red":
        main_colors.append("red")
        paint_colors.pop()
        paint_colors.popleft()
    elif paint_colors[0] + paint_colors[-1] == "yellow" or paint_colors[-1] + paint_colors[0] == "yellow":
        main_colors.append("yellow")
        paint_colors.pop()
        paint_colors.popleft()
    elif paint_colors[0] + paint_colors[-1] == "blue" or paint_colors[-1] + paint_colors[0] == "blue":
        main_colors.append("blue")
        paint_colors.pop()
        paint_colors.popleft()
    elif paint_colors[0] + paint_colors[-1] == "orange" or paint_colors[-1] + paint_colors[0] == "orange":
        main_colors.append("orange")
        paint_colors.pop()
        paint_colors.popleft()
    elif paint_colors[0] + paint_colors[-1] == "purple" or paint_colors[-1] + paint_colors[0] == "purple":
        main_colors.append("purple")
        paint_colors.pop()
        paint_colors.popleft()
    elif paint_colors[0] + paint_colors[-1] == "green" or paint_colors[-1] + paint_colors[0] == "green":
        main_colors.append("green")
        paint_colors.pop()
        paint_colors.popleft()
    else:
        paint_colors[0] = paint_colors[0][:-1]
        paint_colors[-1] = paint_colors[-1][:-1]

        if len(paint_colors[0]) == 0:
            paint_colors.remove(paint_colors[0])
        else:
            index = int((len(paint_colors) - 1) / 2)
            paint_colors.insert(index, paint_colors[0])
            paint_colors.popleft()
        if len(paint_colors[-1]) == 0:
            paint_colors.remove(paint_colors[-1])
        else:
            index = int((len(paint_colors) - 1) / 2)
            paint_colors.insert(index, paint_colors[-1])
            paint_colors.pop()
    if len(paint_colors) == 1:
        if "red" in paint_colors:
            main_colors.append("red")
            paint_colors.pop()
        elif "yellow" in paint_colors:
            main_colors.append("yellow")
            paint_colors.pop()
        elif "blue" in paint_colors:
            main_colors.append("blue")
            paint_colors.pop()
        elif "orange" in paint_colors:
            main_colors.append("orange")
            paint_colors.pop()
        elif "purple" in paint_colors:
            main_colors.append("purple")
            paint_colors.pop()
        elif "green" in paint_colors:
            main_colors.append("green")
            paint_colors.pop()
        else:
            paint_colors.pop()
if "orange" in main_colors:
    if "red" not in main_colors or "yellow" not in main_colors:
        main_colors.remove("orange")
if "purple" in main_colors:
    if "red" not in main_colors or "blue" not in main_colors:
        main_colors.remove("purple")
if "green" in main_colors:
    if "yellow" not in main_colors or "blue" not in main_colors:
        main_colors.remove("green")

print(main_colors)
