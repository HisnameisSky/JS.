def my_replace(string: str, before: str, after: str) -> str:
    # 1. beforeの先頭が大文字の場合
    if before[0].isupper():
        after = after[0].upper() + after[1:]
    else:
        after = after[0].lower() + after[1:]

    # 2. 単語の置換
    return string.replace(before, after)


# --- テスト実行 ---
print(
    my_replace("Let us go to the store", "store", "mall")
)  # -> "Let us go to the mall"
print(
    my_replace("He is Sleeping on the couch", "Sleeping", "sitting")
)  # -> "He is Sitting on the couch"
print(
    my_replace("I think we should look up there", "up", "Down")
)  # -> "I think we should look down there"
print(
    my_replace("His name is Tom", "Tom", "john")
)  # -> "His name is John"