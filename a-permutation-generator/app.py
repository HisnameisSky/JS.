def permute_string(str_val: str, prefix: str = "", result: list = None) -> list:
    if result is None:
        result = []

    if len(str_val) == 0:
        if prefix not in result:
            result.append(prefix)
        return result

    for i in range(len(str_val)):
        char = str_val[i]
        remaining = str_val[:i] + str_val[i+1:]
        permute_string(remaining, prefix + char , result)
    return result

if __name__ == "__main__":
    print(permute_string("cat"))
    print([permute_string("fcc")])