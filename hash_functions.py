"""Provided hash functions. Do not change these functions."""


def hash_mod(key: int, table_size: int) -> int:
    return key % table_size


def hash_digit_sum(key: int, table_size: int) -> int:
    return sum(int(d) for d in str(abs(key))) % table_size
