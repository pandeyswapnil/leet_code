def canConstruct(self, s: str, k: int) -> bool:
    if len(s) < k:
        return False
    map_data = {}
    for char in s:
        map_data[char] = map_data.get(char, 0) + 1

    count = 0
    for var in map_data:
        if map_data[var] % 2:
            count += 1

    return count <= k