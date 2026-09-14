import math
import time
import threading

# 1. アニメーション用のデータ定義（辞書のリスト）
animation_data = [
    {
        "input_val": 5,
        "add_el_delay": 1.0,
        "msg": 'decimalToBinary(5) returns "10" + 1 (5 % 2). Then it pops off the stack.',
        "show_msg_delay": 15.0,
        "remove_el_delay": 20.0,
    },
    {
        "input_val": 2,
        "add_el_delay": 1.5,
        "msg": 'decimalToBinary(2) returns "1" + 0 (2 % 2) and gives that value to the stack below. Then it pops off the stack.',
        "show_msg_delay": 10.0,
        "remove_el_delay": 15.0,
    },
    {
        "input_val": 1,
        "add_el_delay": 2.0,
        "msg": "decimalToBinary(1) returns '1' (base case) and gives that value to the stack below. Then it pops off the stack.",
        "show_msg_delay": 5.0,
        "remove_el_delay": 10.0,
    }
]


# 2. 10進数から2進数へ変換する再帰関数
def decimal_to_binary(input_val: int) -> str:
    if input_val == 0 or input_val == 1:
        return str(input_val)
    else:
        # Math.floor(input / 2) は Python では input_val // 2
        return decimal_to_binary(input_val // 2) + str(input_val % 2)


# 3. アニメーションをシミュレートする関数
def show_animation() -> None:
    print("\n--- Call Stack Animation ---")

    def schedule_task(delay: float, action):
        time.sleep(delay)
        action()

    # 各アニメーションステップを別スレッドで並行実行（JSの setTimeout を再現）
    threads = []
    for obj in animation_data:
        # 要素の追加
        t1 = threading.Thread(
            target=schedule_task,
            args=(obj["add_el_delay"], lambda o=obj: print(f"[Stack Added]: decimalToBinary({o['input_val']})"))
        )
        # メッセージの更新
        t2 = threading.Thread(
            target=schedule_task,
            args=(obj["show_msg_delay"], lambda o=obj: print(f"[Stack Msg]: {o['msg']}"))
        )
        # 要素の削除
        t3 = threading.Thread(
            target=schedule_task,
            args=(obj["remove_el_delay"], lambda o=obj: print(f"[Stack Removed]: decimalToBinary({o['input_val']})"))
        )
        threads.extend([t1, t2, t3])

    # 最終結果表示用のタイマー（20秒後）
    t_final = threading.Thread(
        target=schedule_task,
        args=(20.0, lambda: print(f"\n[Result]: {decimal_to_binary(5)}"))
    )
    threads.append(t_final)

    for t in threads:
        t.start()


# 4. ユーザー入力をチェックして処理する関数
def check_user_input(user_input: str) -> None:
    try:
        input_int = int(user_input)
        if input_int < 0:
            print("Please provide a decimal number greater than or equal to 0")
            return
    except ValueError:
        print("Please provide a decimal number greater than or equal to 0")
        return

    # 入力が 5 の場合はアニメーションを実行
    if input_int == 5:
        show_animation()
        return

    # それ以外は即座に結果を表示
    result = decimal_to_binary(input_int)
    print(f"Result: {result}")


# === 動作確認部分 ===
if __name__ == "__main__":
    # 例1: 通常の数値入力 (例: 10)
    print("--- 10を変換する場合 ---")
    check_user_input("10")

    # 例2: 5を入力してアニメーションを起動する場合
    # print("\n--- 5を変換する場合（アニメーション実行） ---")
    # check_user_input("5")