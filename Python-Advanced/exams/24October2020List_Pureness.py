def best_list_pureness(*test):
    ll = test[0]
    rotation = test[1]
    result = 0
    final = []
    best = 0
    for i in range(0, rotation + 1):
        if i == 0:
            for num in ll:
                best += num * ll.index(num)
                if best > result:
                    result = best

        if i > 0:
            needed = ll[-1]
            ll.remove(needed)
            ll.insert(0, needed)
            for num in ll:
                best += num * ll.index(num)
                if best > result:
                    result = best
        final.append(best)
        best = 0
    index = None
    for nums in final:
        index = final.index(max(final))
    return f"Best pureness {int(result)} after {index} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)