def find(ordered_list: list, to_find: int) -> bool:
    if ordered_list == []:
        return False
    pivot = ordered_list[len(ordered_list) // 2]
    if pivot == to_find:
        return True
    elif len(ordered_list) == 1 and ordered_list[0] != to_find:
        return False
    elif pivot > to_find:
        return find(ordered_list[: len(ordered_list) // 2], to_find)
    else:
        return find(ordered_list[len(ordered_list) // 2 :], to_find)


def verify(ordered_list: list, to_find: int, is_in_the_list: bool):
    try :
        if is_in_the_list :
            print(f"Testing integer '{to_find}' exists in list {ordered_list}: ", end="")        
            assert find(ordered_list=ordered_list, to_find=to_find)        
        else :
            print(f"Testing integer '{to_find}' does not exist in list {ordered_list}: ", end="")        
            assert not find(ordered_list=ordered_list, to_find=to_find)        
    except:
        print("ERROR...")
        return False
    print("OK!")
    
verify(ordered_list=[],to_find=5,is_in_the_list=False)
verify(ordered_list=[5],to_find=5,is_in_the_list=True)
verify(ordered_list=[1, 3, 8, 9],to_find=5,is_in_the_list=False)
verify(ordered_list=[1, 2, 3, 8, 9],to_find=5,is_in_the_list=False)
verify(ordered_list=[1, 3, 5, 8, 9],to_find=5,is_in_the_list=True)
verify(ordered_list=[1, 2, 3, 5, 8, 9],to_find=5,is_in_the_list=True)
verify(ordered_list=[-3, -1, 8, 9],to_find=5,is_in_the_list=False)
verify(ordered_list=[-3, -1, 5, 8, 9],to_find=5,is_in_the_list=True)