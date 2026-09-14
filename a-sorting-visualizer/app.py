import random


# 1. 1〜100 のランダムな整数を返す
def generate_element() -> int:
    return random.randint(1, 100)


# 2. 5つのランダム整数配列を生成
def generate_array() -> list[int]:
    return [generate_element() for _ in range(5)]


# 3. 順序チェック
def is_ordered(num1: int, num2: int) -> bool:
    return num1 <= num2


# 4. 要素のスワップ (Pythonの分割代入)
def swap_elements(arr: list[int], idx: int) -> None:
    if not is_ordered(arr[idx], arr[idx + 1]):
        arr[idx], arr[idx + 1] = arr[idx + 1], arr[idx]


# 5. バブルソートのステップ実行プロセス（シミュレーション）
def simulate_bubble_sort(initial_array: list[int]):
    array = list(initial_array)
    steps = []

    # 初期表示ステップ
    steps.append({"arr": list(array), "highlight": (0, 1)})

    swapped = True
    step_count = 0

    while swapped:
        swapped = False
        for idx in range(len(array) - 1):
            if step_count != 0:
                steps.append({"arr": list(array), "highlight": (idx, idx + 1)})

            if not is_ordered(array[idx], array[idx + 1]):
                swap_elements(array, idx)
                swapped = True

            step_count += 1

    # 最終ソート済み状態
    steps.append({"arr": list(array), "highlight": None})
    return steps


# === 動作確認 ===
if __name__ == "__main__":
    start_arr = generate_array()
    print(f"初期配列: {start_arr}\n")

    history = simulate_bubble_sort(start_arr)
    for i, step in enumerate(history):
        hl = f" (ハイライト: インデックス {step['highlight']})" if step['highlight'] else " [完了]"
        print(f"Step {i+1}: {step['arr']}{hl}")