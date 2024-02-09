def count_characters(my_string: str) -> str:
    return len(my_string)

def token_count(tokens: int) -> int:
    tokens_leftover = tokens % 4
    return  tokens // 4 + 1 if tokens_leftover > 0 else tokens // 4