import tkinter as tk

# 1. データ定義 (JS の themes 配列に相当)
themes = [
    {
        "name": "light",
        "message": "Light theme activated!",
        "bg": "#ffffff",
        "fg": "#000000",
    },
    {
        "name": "dark",
        "message": "Dark theme activated!",
        "bg": "#222222",
        "fg": "#ffffff",
    },
]

# ドロップダウンの表示状態を管理するフラグ
is_menu_visible = False


def toggle_dropdown():
    """ドロップダウンメニューの表示/非表示切り替え (JS の click イベントハンドラ)"""
    global is_menu_visible
    if is_menu_visible:
        dropdown_frame.pack_forget()
        is_menu_visible = False
    else:
        dropdown_frame.pack(after=switcher_btn)
        is_menu_visible = True


def apply_theme(theme):
    """テーマ適用処理 (JS の body.classList.add & message 表示に相当)"""
    global is_menu_visible
    # 背景色と文字色の変更
    root.config(bg=theme["bg"])
    status_label.config(text=theme["message"], bg=theme["bg"], fg=theme["fg"])

    # メニューを閉じる
    dropdown_frame.pack_forget()
    is_menu_visible = False


# --- GUI (画面) の初期化 ---
root = tk.Tk()
root.title("Theme Switcher")
root.geometry("300x200")

# メインボタン
switcher_btn = tk.Button(
    root, text="Switch Theme", command=toggle_dropdown, padx=10, pady=5
)
switcher_btn.pack(pady=10)

# ドロップダウンメニュー用フレーム（初期状態は非表示）
dropdown_frame = tk.Frame(root, bd=1, relief=tk.SOLID)

# li 要素に相当するボタンの生成
for theme in themes:
    btn = tk.Button(
        dropdown_frame,
        text=theme["name"],
        command=lambda t=theme: apply_theme(t),
        width=15,
    )
    btn.pack()

# ステータスメッセージ表示エリア (aria-live="polite" に相当)
status_label = tk.Label(root, text="", font=("Arial", 10, "bold"))
status_label.pack(pady=20)

root.mainloop()