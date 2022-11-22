def max_duffel_bag_value(cake_tuples: list(tuple()), capacity: int) -> int:
    rates = []
    for cake in cake_tuples:
        weight = cake[0]
        monetary_value = cake[1]
        if weight != 0 or monetary_value != 0:
            rates.append(monetary_value / weight)
        else:
            rates.append(0)
            
    full_bag = False
    value = 0
    while not full_bag:
        most_worth_cake = rates.index(max(rates))
        while cake_tuples[most_worth_cake][0] <= capacity:
            value += cake_tuples[most_worth_cake][1]
            capacity -= cake_tuples[most_worth_cake][0]
        rates[rates.index(max(rates))] = 0
        if not any(rates) or capacity == 0:
            full_bag = True
    print(f"capacity left is {capacity} kg")
    return value

cake_tuples = [(0, 0), (3, 90), (2, 15)]
capacity = 27
print(max_duffel_bag_value(cake_tuples=cake_tuples, capacity=capacity))
