def init_stack():
    return {
        "collection": []
    }

def push(stack, item):
    stack["collection"].append(item)

def pop(stack):
    if is_empty(stack):
        return None  # JSの undefined に該当
    return stack["collection"].pop()

def peek(stack):
    if is_empty(stack):
        return None  # JSの undefined に該当
    return stack["collection"][-1]

def is_empty(stack):
    return len(stack["collection"]) == 0

def clear(stack):
    stack["collection"] = []


# === 動作確認 ===
if __name__ == "__main__":
    my_stack = init_stack()
    print(is_empty(my_stack))  # True

    push(my_stack, 10)
    push(my_stack, 20)
    push(my_stack, 0)  # 偽値（0）のテスト

    print(peek(my_stack))      # 0 (削除されずにトップの要素を取得)
    print(is_empty(my_stack))  # False

    print(pop(my_stack))       # 0 (取り出される)
    print(pop(my_stack))       # 20
    print(pop(my_stack))       # 10
    print(pop(my_stack))       # None (空のスタックから取り出すと None)

    push(my_stack, 100)
    clear(my_stack)
    print(is_empty(my_stack))  # True