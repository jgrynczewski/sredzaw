def is_isogram(word:str) -> bool:
    letters = set(word)
    return len(word) == len(letters)

def is_isogrm_c(word:str) -> bool:
    return len({letter for letter in word}) == len(word)

if __name__ == '__main__':
    print(is_isogram('skrzynia'))