import re

class BudgetCalculator:
    def __init__(self):
        self.is_error = False
        self.entries = {
            "food": [],
            "utilities": [],
            "entertainment": []
        }
        self.income_val = "0"
        self.rent_val = "0"

    def clean_input_string(self, str_val: str) -> str:
        """＋, －, 空白記号を除去"""
        regex = r'[+-\s]'
        return re.sub(regex, '', str_val)

    def is_invalid_input(self, str_val: str):
        """科学的記数法 (例: 1e10) のパターンをチェック"""
        regex = r'\d+e\d+'
        return re.search(regex, str_val, re.IGNORECASE)

    def add_entry(self, category: str, name: str, amount_str: str):
        """支出項目を追加"""
        if category in self.entries:
            self.entries[category].append({"name": name, "amount": amount_str})

    def get_total_from_inputs(self, raw_values: list[str]) -> float | None:
        """入力文字列のリストを受け取り、無効チェックを経て合計値を計算"""
        total = 0.0
        for item in raw_values:
            curr_val = self.clean_input_string(item)
            if not curr_val:
                continue

            invalid_match = self.is_invalid_input(curr_val)

            if invalid_match:
                print(f"  [!] エラー: 無効な入力パターンが含まれています -> '{invalid_match.group(0)}'")
                self.is_error = True
                return None
            
            try:
                total += float(curr_val)
            except ValueError:
                print(f"  [!] エラー: 数値に変換できません -> '{curr_val}'")
                self.is_error = True
                return None

        return total

    def calculate_budget(self):
        """収支計算を行い結果データを返却"""
        self.is_error = False

        food_values = [item["amount"] for item in self.entries["food"]]
        utilities_values = [item["amount"] for item in self.entries["utilities"]]
        entertainment_values = [item["amount"] for item in self.entries["entertainment"]]

        rent = self.get_total_from_inputs([self.rent_val])
        food = self.get_total_from_inputs(food_values)
        utilities = self.get_total_from_inputs(utilities_values)
        entertainment = self.get_total_from_inputs(entertainment_values)
        income = self.get_total_from_inputs([self.income_val])

        if self.is_error:
            return None

        expenses = rent + food + utilities + entertainment
        net_remaining = income - expenses

        if net_remaining < 0:
            status_text = f"Over Budget by ${abs(net_remaining):.2f}"
            status_class = "deficit"
        else:
            status_text = f"${net_remaining:.2f} Remaining"
            status_class = "surplus"

        return {
            "status_class": status_class,
            "status_text": status_text,
            "income": income,
            "expenses": expenses,
            "net_remaining": net_remaining
        }

    def clear_form(self):
        """状態のクリア"""
        self.is_error = False
        self.entries = {"food": [], "utilities": [], "entertainment": []}
        self.income_val = "0"
        self.rent_val = "0"


# ==========================================
# CLI ユーザーインターフェース処理
# ==========================================
def run_cli():
    calc = BudgetCalculator()
    category_names = {
        "1": ("food", "食費 (Food)"),
        "2": ("utilities", "光熱・水道費 (Utilities)"),
        "3": ("entertainment", "娯楽費 (Entertainment)")
    }

    print("=" * 45)
    print("      家計簿・予算計算ツール (CLI版)")
    print("=" * 45)

    while True:
        print("\n--- メニュー ---")
        print("1: 基本情報の設定 (収入 / 家賃)")
        print("2: 支出項目の追加 (食費/光熱費/娯楽費)")
        print("3: 収支計算の実行")
        print("4: フォームのクリア")
        print("0: 終了")
        
        choice = input("\n操作番号を選択してください (0-4): ").strip()

        if choice == "1":
            calc.income_val = input("総収入額を入力してください (例: 3000): ").strip()
            calc.rent_val = input("家賃/住宅費を入力してください (例: 1000): ").strip()
            print(">> 基本情報を設定しました。")

        elif choice == "2":
            print("\n-- カテゴリ選択 --")
            print("1: 食費 (Food)")
            print("2: 光熱・水道費 (Utilities)")
            print("3: 娯楽費 (Entertainment)")
            cat_choice = input("カテゴリ番号を選択してください (1-3): ").strip()

            if cat_choice in category_names:
                cat_key, cat_label = category_names[cat_choice]
                name = input(f"[{cat_label}] 項目名を入力 (例: スーパー): ").strip()
                amount = input(f"[{cat_label}] 金額を入力 (例: 50): ").strip()
                calc.add_entry(cat_key, name, amount)
                print(f">> [{cat_label}] に '{name}: ${amount}' を追加しました。")
            else:
                print("[!] 無効なカテゴリ選択です。")

        elif choice == "3":
            print("\n" + "=" * 30)
            print("       計算結果")
            print("=" * 30)
            res = calc.calculate_budget()

            if res:
                print(f" 状態    : {res['status_text']}")
                print(f" ----------------------------")
                print(f" 総収入  : ${res['income']:.2f}")
                print(f" 総支出  : ${res['expenses']:.2f}")
                print("=" * 30)
            else:
                print("計算を中止しました。入力内容を確認してください。")

        elif choice == "4":
            calc.clear_form()
            print(">> すべての入力データをクリアしました。")

        elif choice == "0":
            print("プログラムを終了します。")
            break
        else:
            print("[!] 有効な番号を入力してください。")


if __name__ == "__main__":
    run_cli()