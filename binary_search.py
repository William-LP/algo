def find(tableau : list, to_find : int) -> bool :
    print("iteration")
    if tableau == [] :
        return False
    pivot = tableau[len(tableau)//2]
    if pivot == to_find :
        return True
    elif len(tableau) == 1 and tableau[0] != to_find:
        return False
    elif pivot > to_find :
        return find(tableau[:len(tableau)//2],to_find)
    else:
        return find(tableau[len(tableau)//2:],to_find)

assert find([], 5) == False
assert find([5], 5) == True
assert find([1,3,8,9], 5) == False
assert find([1,2,3,8,9], 5) == False
assert find([1,3,5,8,9], 5) == True
assert find([1,2,3,5,8,9], 5) == True
assert find([-3,-1,8,9], 5) == False
assert find([-3,-1,5,8,9], 5) == True
    


