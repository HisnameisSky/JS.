import re
import tkinter as tk


def get_flags():
    flags = 0
    if case_insensitive_var.get():
        flags |= re.IGNORECASE
    return flags


def test_regex():
    pattern = pattern_input.get()
    raw_text = test_string_entry.get("1.0", tk.END).strip()

    # ハイライトの全初期化
    test_string_entry.tag_remove("highlight", "1.0", tk.END)

    if not pattern:
        result_label.config(text="no match")
        return

    try:
        flags = get_flags()
        is_global = global_var.get()

        if is_global:
            matches = list(re.finditer(pattern, raw_text, flags))
        else:
            match = re.search(pattern, raw_text, flags)
            matches = [match] if match else []

        if matches:
            matched_texts = []
            for match in matches:
                start_idx = f"1.0 + {match.start()} chars"
                end_idx = f"1.0 + {match.end()} chars"
                # 一致箇所をタグでハイライト
                test_string_entry.tag_add("highlight", start_idx, end_idx)
                matched_texts.append(match.group())

            # 結果を表示（カンマとスペース区切り）
            result_label.config(text=", ".join(matched_texts))
        else:
            result_label.config(text="no match")

    except re.error:
        result_label.config(text="no match")


# --- Tkinter GUI 設定 ---
root = tk.Tk()
root.title("Regex Sandbox")
root.geometry("500x400")

# パターン入力
tk.Label(root, text="Regex Pattern:").pack(anchor="w", padx=10, pady=5)
pattern_input = tk.Entry(root, width=40)
pattern_input.pack(padx=10)

# フラグ設定
flags_frame = tk.Frame(root)
flags_frame.pack(pady=5)
case_insensitive_var = tk.BooleanVar()
global_var = tk.BooleanVar()

tk.Checkbutton(
    flags_frame, text="i (Ignore Case)", variable=case_insensitive_var
).pack(side="left")
tk.Checkbutton(flags_frame, text="g (Global)", variable=global_var).pack(
    side="left"
)

# テスト文字列
tk.Label(root, text="Test String:").pack(anchor="w", padx=10, pady=5)
test_string_entry = tk.Text(root, height=4, width=50)
test_string_entry.pack(padx=10)
test_string_entry.tag_config("highlight", background="lightgreen")

# テスト実行ボタン
test_btn = tk.Button(root, text="Test Regex", command=test_regex)
test_btn.pack(pady=10)

# 結果表示
tk.Label(root, text="Result:").pack(anchor="w", padx=10)
result_label = tk.Label(
    root, text="", bg="white", relief="sunken", anchor="w", height=2
)
result_label.pack(fill="x", padx=10, pady=5)

root.mainloop()