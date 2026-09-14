import unittest
# テスト対象のクラスをインポート（budget_app.pyにクラスが記述されている想定）
from budget_app import BudgetCalculator

class TestBudgetCalculator(unittest.TestCase):

    def setUp(self):
        """各テストメソッドの実行前に呼ばれるセットアップ処理"""
        self.calc = BudgetCalculator()

    # ----------------------------------------------------
    # 1. clean_input_string のテスト
    # ----------------------------------------------------
    def test_clean_input_string_removes_symbols_and_spaces(self):
        """＋, －, 空白記号が正しく除去されるか確認"""
        self.assertEqual(self.calc.clean_input_string(" +100 - "), "100")
        self.assertEqual(self.calc.clean_input_string("5 0 0"), "500")
        self.assertEqual(self.calc.clean_input_string("+ -  "), "")

    # ----------------------------------------------------
    # 2. is_invalid_input のテスト
    # ----------------------------------------------------
    def test_is_invalid_input_detects_scientific_notation(self):
        """科学的記数法 (例: 1e10) のパターンを検知できるか判定"""
        # 該当する場合はMatchオブジェクトが返るので None ではない
        self.assertIsNotNone(self.calc.is_invalid_input("1e5"))
        self.assertIsNotNone(self.calc.is_invalid_input("10E2"))
        
        # 通常の数値や文字列は None となる
        self.assertIsNone(self.calc.is_invalid_input("1000"))
        self.assertIsNone(self.calc.is_invalid_input("abc"))

    # ----------------------------------------------------
    # 3. add_entry のテスト
    # ----------------------------------------------------
    def test_add_entry_success(self):
        """指定したカテゴリに項目が正しく追加されるか確認"""
        self.calc.add_entry("food", "Lunch", "15")
        
        self.assertEqual(len(self.calc.entries["food"]), 1)
        self.assertEqual(self.calc.entries["food"][0], {"name": "Lunch", "amount": "15"})

    def test_add_entry_invalid_category_ignored(self):
        """存在しないカテゴリを指定した場合は無視されるか確認"""
        self.calc.add_entry("invalid_category", "Test", "100")
        self.assertNotIn("invalid_category", self.calc.entries)

    # ----------------------------------------------------
    # 4. get_total_from_inputs のテスト
    # ----------------------------------------------------
    def test_get_total_from_inputs_valid_list(self):
        """正常な入力文字列リストの合計値が計算できるか確認"""
        raw_list = [" 100 ", "200+", "+300-"]
        result = self.calc.get_total_from_inputs(raw_list)
        
        self.assertEqual(result, 600.0)
        self.assertFalse(self.calc.is_error)

    def test_get_total_from_inputs_scientific_notation_error(self):
        """1e10 などの科学的記数法が含まれる場合にエラーとなるか確認"""
        raw_list = ["100", "1e5"]
        result = self.calc.get_total_from_inputs(raw_list)
        
        self.assertIsNone(result)
        self.assertTrue(self.calc.is_error)

    def test_get_total_from_inputs_non_numeric_error(self):
        """数値化できない文字列が含まれる場合にエラーとなるか確認"""
        raw_list = ["100", "abc"]
        result = self.calc.get_total_from_inputs(raw_list)
        
        self.assertIsNone(result)
        self.assertTrue(self.calc.is_error)

    # ----------------------------------------------------
    # 5. calculate_budget のテスト
    # ----------------------------------------------------
    def test_calculate_budget_surplus(self):
        """黒字（余りあり）の場合の計算結果を検証"""
        self.calc.income_val = "3000"
        self.calc.rent_val = "1000"
        self.calc.add_entry("food", "Groceries", "500")
        self.calc.add_entry("utilities", "Electricity", "100")
        self.calc.add_entry("entertainment", "Movie", "50")

        # 収入 3000 / 支出 1650 / 残金 1350
        res = self.calc.calculate_budget()

        self.assertIsNotNone(res)
        self.assertEqual(res["status_class"], "surplus")
        self.assertEqual(res["net_remaining"], 1350.0)
        self.assertEqual(res["expenses"], 1650.0)

    def test_calculate_budget_deficit(self):
        """赤字（予算オーバー）の場合の計算結果を検証"""
        self.calc.income_val = "1000"
        self.calc.rent_val = "1200" # 家賃だけでオーバー

        res = self.calc.calculate_budget()

        self.assertIsNotNone(res)
        self.assertEqual(res["status_class"], "deficit")
        self.assertEqual(res["net_remaining"], -200.0)
        self.assertIn("Over Budget", res["status_text"])

    # ----------------------------------------------------
    # 6. clear_form のテスト
    # ----------------------------------------------------
    def test_clear_form_resets_state(self):
        """フォームのリセットが正しく動作するか確認"""
        self.calc.income_val = "2000"
        self.calc.add_entry("food", "Dinner", "50")
        self.calc.is_error = True

        self.calc.clear_form()

        self.assertEqual(self.calc.income_val, "0")
        self.assertEqual(len(self.calc.entries["food"]), 0)
        self.assertFalse(self.calc.is_error)


if __name__ == "__main__":
    unittest.main()