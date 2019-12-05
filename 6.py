# Adnotacje

def is_isogram(word: str) -> bool:
    return len(word) == len(set(word))

print(is_isogram("asd"))

from typing import Dict, List

def extract_keys(my_dict: Dict[str, int]) -> List[str]:
    return list(my_dict.keys())

