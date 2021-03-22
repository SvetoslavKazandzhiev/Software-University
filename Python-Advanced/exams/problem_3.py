def stock_availability(*args):
    param = []
    for arg in args:
        param.append(arg)

    inventory_list = param[0]
    command = param[1]
    if command == 'delivery':
        inventory_list += param[2:]
        return inventory_list
    if command == 'sell':
        if len(param) < 3:
            inventory_list.pop(0)
            return inventory_list
        elif len(param) == 3 and type(param[2]) == int:
            cycles = param[2]
            inventory_list = inventory_list[cycles:]
            return inventory_list
        elif len(param) >= 3 and type(param[2]) == str:
            length = len(param) - 1
            while length >= 0:
                if type(param[length]) == str:
                    while param[length] in inventory_list:
                        inventory_list.remove(param[length])
                length -= 1

            return inventory_list

# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate", 'cookie'))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))