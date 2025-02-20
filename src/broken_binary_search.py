def contains(key: float, data: list[int]) -> bool:
    """
    :param key: The key being searched for
    :param data: A sequence of keys in increasing order
    :return: True if key is in data
    """
    lo: int = 0
    hi: int = len(data)
    while lo < hi:
        mid: int = (lo + hi) // 2
        if key < data[mid]:
            hi = mid - 1
        elif key == data[mid]:
            return True
        else:
            lo = mid + 1
    return False

d = list(range(6))
for i in d:
    assert contains(i, d)
