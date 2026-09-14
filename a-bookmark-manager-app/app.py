import json
import os

class BookmarkManager:
    def __init__(self, storage_file="bookmarks.json"):
        self.storage_file = storage_file
        self.selected_category = "News"

    # --- 1. ローカルストレージ（JSONファイル）からデータを取り出す ---
    def get_bookmarks(self) -> list:
        if not os.path.exists(self.storage_file):
            return []
        
        try:
            with open(self.storage_file, "r", encoding="utf-8") as f:
                parsed = json.load(f)
                
            if not isinstance(parsed, list):
                return []

            # 各要素が辞書型かつ必要なキー・型を持っているかバリデーション
            is_valid = all(
                isinstance(item, dict) and
                isinstance(item.get("name"), str) and
                isinstance(item.get("category"), str) and
                isinstance(item.get("url"), str)
                for item in parsed
            )
            return parsed if is_valid else []
        except Exception:
            return []

    # --- 2. ブックマークの追加 ---
    def add_bookmark(self, name: str, url: str) -> None:
        current_bookmarks = self.get_bookmarks()
        new_bookmark = {
            "name": name,
            "category": self.selected_category,
            "url": url
        }
        current_bookmarks.append(new_bookmark)

        # ファイルに書き込み保存 (localStorage.setItem 相当)
        with open(self.storage_file, "w", encoding="utf-8") as f:
            json.dump(current_bookmarks, f, ensure_ascii=False, indent=2)

    # --- 3. カテゴリごとの抽出（DOM描画の準備） ---
    def get_filtered_bookmarks((self) -> list:
        bookmarks = self.get_bookmarks()
        return [b for b in bookmarks if b.get("category") == self.selected_category]

    # --- 4. ブックマークの削除 ---
    def delete_bookmark(self, selected_bookmark_name: str) -> None:
        bookmarks = self.get_bookmarks()
        
        target_index = -1
        for i, b in enumerate(bookmarks):
            if b.get("name") == selected_bookmark_name and b.get("category") == self.selected_category:
                target_index = i
                break

        if target_index != -1:
            bookmarks.pop(target_index)
            with open(self.storage_file, "w", encoding="utf-8") as f:
                json.dump(bookmarks, f, ensure_ascii=False, indent=2)


# === 動作確認用例 ===
if __name__ == "__main__":
    manager = BookmarkManager()
    
    # 追加の試行
    manager.selected_category = "News"
    manager.add_bookmark("Google", "https://google.com")
    
    # フィルタリング取得
    print("Newsのブックマーク:", manager.get_filtered_bookmarks())
    
    # 削除の試行
    manager.delete_bookmark("Google")
    print("削除後のブックマーク:", manager.get_bookmarks())