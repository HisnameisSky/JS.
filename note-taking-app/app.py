import tkinter as tk

# 1. 状態を保持する変数（JavaScriptの currentContent に相当）
current_content = ""


def on_focus_in(event):
    """focus イベント処理: 入力開始時にステータスをクリア"""
    status_el.config(text="")


def on_focus_out(event):
    """blur イベント処理: フォーカスが外れた時に変更を検知して保存"""
    global current_content

    # テキストエリアの内容を取得（末尾の改行を除外）
    new_content = note_el.get("1.0", tk.END).strip()

    # 内容が変わっていなければ処理を中断
    if current_content == new_content:
        return

    # 内容が更新されていれば保存処理を実行
    current_content = new_content
    print(f"Saved content: {current_content}")

    # ステータス表示の更新
    status_el.config(text="Note saved successfully!")


# --- GUI (画面) の初期化 ---
root = tk.Tk()
root.title("Auto Save Note")
root.geometry("300x200")

# 2. 要素（DOM）の取得に相当するUIコンポーネントの作成
note_el = tk.Text(root, height=8, width=30)
note_el.pack(pady=10)

status_el = tk.Label(root, text="", fg="green")
status_el.pack()

# 3. イベントリスナーの設定
# <FocusIn> は focus, <FocusOut> は blur に対応
note_el.bind("<FocusIn>", on_focus_in)
note_el.bind("<FocusOut>", on_focus_out)

# 4. DOMContentLoaded に相当する初期化処理（初期テキストの保持）
current_content = note_el.get("1.0", tk.END).strip()

root.mainloop()