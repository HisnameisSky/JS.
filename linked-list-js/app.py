import json


# 1. リストの初期化
def init_list():
    return {
        "head": None,
        "length": 0
    }


# 2. 空かどうかを判定
def is_empty(lst):
    return lst["length"] == 0


# 3. ノードの追加
def add(lst, element):
    node = {
        "element": element,
        "next": None
    }

    if is_empty(lst):
        lst["head"] = node
    else:
        current = lst["head"]
        while current["next"] is not None:
            current = current["next"]
        current["next"] = node

    lst["length"] += 1


# 4. ノードの削除
def remove(lst, element):
    previous = None
    current = lst["head"]

    # 削除対象の要素を検索
    while current is not None and current["element"] != element:
        previous = current
        current = current["next"]

    # 該当要素が存在しない場合
    if current is None:
        return

    # ポインタ（参照）の繋ぎ替え処理
    if previous is not None:
        previous["next"] = current["next"]
    else:
        lst["head"] = current["next"]

    lst["length"] -= 1


# === 実行部分 ===
my_list = init_list()
print(is_empty(my_list))  # True

add(my_list, 42)
add(my_list, 43)
add(my_list, 44)

print(my_list)
print(is_empty(my_list))  # False

remove(my_list, 43)

# JSの JSON.stringify(myList, null, 2) を再現
print(json.dumps(my_list, indent=2))