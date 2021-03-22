from collections import deque

customers = deque(int(x) for x in (input().split(", ")))
taxis = deque(int(x) for x in (input().split(", ")))
copy = sum(customers)
while customers:
    if len(customers) == 0:
        break
    if len(customers) > 0 and len(taxis) == 0:
        print("Not all customers were driven to their destinations")
        print(f"Customers left: {', '.join(map(str, customers))}")
        break
    if len(taxis) > 0:
        if customers[0] <= taxis[-1]:
            customers.popleft()
            taxis.pop()
        else:
            taxis.pop()
    if len(customers) == 0 and len(taxis) >= 0:
        print("All customers were driven to their destinations")
        print(f"Total time: {copy} minutes")



