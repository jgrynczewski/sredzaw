print("Adnotacje typów")

def is_isogram(word: str) ->bool:
    return len(word) == len(set(word))

print(is_isogram('ala'))


from typing import Dict, List
#parametrem funkcji jest słownik, któ©ego klucze są stringmi a wartości intami,  # funkcja zwraca listę, która zawiera inty
def extract_keys(my_dict: Dict[str, int]) -> List[str]:
    return list(my_dict.keys())

#do testowania typów można użyć narzędzi, np mypy
#komenda w konsoli mypy my6.py

