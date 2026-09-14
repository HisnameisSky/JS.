from dataclasses import dataclass, field
from typing import List

# 商品を表すクラス
@dataclass
class Dessert:
    id: int
    name: str
    price: float
    category: str


# カートを表すクラス
class ShoppingCart:
    def __init__(self, tax_rate: float = 8.25):
        self.items: List[Dessert] = []
        self.total: float = 0.0
        self.tax_rate: float = tax_rate

    def add_item(self, product_id: int, products_list: List[Dessert]) -> None:
        """商品IDを元に商品を検索し、カートに追加する"""
        product = next((item for item in products_list if item.id == product_id), None)
        if product:
            self.items.append(product)

    def get_counts(self) -> int:
        """カート内の合計商品数を取得"""
        return len(self.items)

    def clear_cart(self) -> None:
        """カートの中身を全削除（確認用ダイアログのロジックは呼び出し側に委ねる）"""
        if not self.items:
            print("Your shopping cart is already empty")
            return
        
        # コンソール上でクリアを再現
        self.items = []
        self.total = 0.0
        print("Cart cleared!")

    def calculate_taxes(self, amount: float) -> float:
        """消費税の計算（小数第2位でラウンド処理）"""
        return round((self.tax_rate / 100) * amount, 2)

    def calculate_total(self) -> float:
        """小計・税額・合計を計算して保持する"""
        sub_total = sum(item.price for item in self.items)
        tax = self.calculate_taxes(sub_total)
        self.total = sub_total + tax
        
        return {
            "sub_total": round(sub_total, 2),
            "tax": tax,
            "total": round(self.total, 2)
        }


# === 動作確認用実行部分 ===
if __name__ == "__main__":
    # 商品リスト（マスターデータ）
    products = [
        Dessert(1, "Vanilla Cupcakes (6 Pack)", 12.99, "Cupcake"),
        Dessert(2, "French Macaron", 3.99, "Macaron"),
        Dessert(3, "Pumpkin Cupcake", 3.99, "Cupcake"),
        Dessert(4, "Chocolate Cupcake", 5.99, "Cupcake"),
        Dessert(5, "Chocolate Pretzels (4 Pack)", 10.99, "Pretzel"),
        Dessert(6, "Strawberry Ice Cream", 2.99, "Ice Cream"),
        Dessert(7, "Chocolate Macarons (4 Pack)", 9.99, "Macaron"),
        Dessert(8, "Strawberry Pretzel", 4.99, "Pretzel"),
        Dessert(9, "Butter Pecan Ice Cream", 2.99, "Ice Cream"),
        Dessert(10, "Rocky Road Ice Cream", 2.99, "Ice Cream"),
        Dessert(11, "Vanilla Macarons (5 Pack)", 11.99, "Macaron"),
        Dessert(12, "Lemon Cupcakes (4 Pack)", 12.99, "Cupcake"),
    ]

    # カートの初期化
    cart = ShoppingCart()

    # 商品追加テスト（ID: 1 の商品を2回追加）
    cart.add_item(1, products)
    cart.add_item(1, products)

    # 状態の出力
    print(f"カート内の個数: {cart.get_counts()}個")
    totals = cart.calculate_total()
    print(f"小計: ${totals['sub_total']}, 税: ${totals['tax']}, 合計: ${totals['total']}")

    # カート消去テスト
    cart.clear_cart()