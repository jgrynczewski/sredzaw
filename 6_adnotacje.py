# adnotacje

def is_isogram(word:str="bbofij") -> bool:
    return len(word) == len(set(word))

print(is_isogram('asd'))


#biblioteka do rozszerzania typów
from typing import Dict, List

def extract_keys(my_dict: Dict) -> List[int]:
    return list(my_dict.keys())

# do sprawdzenia z mypy -> my_dict.keys wyrzuca specjalny obiekt KeysView[Any] ktory troche rozni sie od listy

