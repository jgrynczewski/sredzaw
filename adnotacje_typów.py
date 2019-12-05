def funkcja(a: int, b: str) -> bool:
    print(a)
    print(b)
    if len(str(a)) == len(str(b)):
        return True
    else:
        return False


print(funkcja(1, 'a'))
print(funkcja('a',  1))



from typing import Dict, List

def extrac_keys(my_dict: Dict[str, int]) -> List[int]:
    return my_dict.keys()