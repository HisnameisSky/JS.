def init_queue():
    return {
        "collection": []
    }

def print_queue(queue):
    print(queue["collection"])

def enqueue(queue, element):
    queue["collection"].append(element)

def dequeue(queue):
    if is_empty(queue):
        return None  # JSの undefined に該当
    return queue["collection"].pop(0)  # 先頭（インデックス0）を取り出す

def front(queue):
    if is_empty(queue):
        return None  # JSの undefined に該当
    return queue["collection"][0]

def size(queue):
    return len(queue["collection"])

def is_empty(queue):
    return len(queue["collection"]) == 0


# === 動作確認 ===
if __name__ == "__main__":
    my_queue = init_queue()
    print(is_empty(my_queue))  # True

    enqueue(my_queue, "A")
    enqueue(my_queue, "B")
    enqueue(my_queue, "C")

    print_queue(my_queue)      # ['A', 'B', 'C']
    print(front(my_queue))     # 'A' (先頭を参照)
    print(size(my_queue))      # 3

    print(dequeue(my_queue))    # 'A' (最初に入れた 'A' が取り出される)
    print(dequeue(my_queue))    # 'B'
    print(size(my_queue))      # 1
    print(is_empty(my_queue))  # False

    dequeue(my_queue)           # 'C' を取り出して空にする
    print(dequeue(my_queue))    # None (空のキューから取り出すと None)
    print(is_empty(my_queue))  # True