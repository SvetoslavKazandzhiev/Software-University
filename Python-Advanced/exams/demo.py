num = int(input())

my_dict = {}

for i in range(num):
    line = input().split("|")
    piece = line[0]
    compositor = line[1]
    keys = line[2]
    if piece not in my_dict:
        my_dict[piece] = []
        my_dict[piece] = my_dict[piece][0]
        # my_dict = [keys]
print(my_dict)