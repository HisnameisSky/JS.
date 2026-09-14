import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QComboBox,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

# ---------------------------------------------------------
# 1. ロジック層 (データ管理)
# ---------------------------------------------------------
poll: dict[str, set] = {}


def add_option(option: str) -> str:
    option = option.strip()
    if not option:
        raise ValueError("Option cannot be empty.")
    if option in poll:
        raise ValueError(f'Option "{option}" already exists.')

    poll[option] = set()
    return f'Option "{option}" added to the poll.'


def vote(option: str, voter_id: str) -> str:
    voter_id = voter_id.strip()
    if not option or option not in poll:
        raise ValueError(f'Option "{option}" does not exist.')
    if not voter_id:
        raise ValueError("Voter ID cannot be empty.")

    voters = poll[option]
    if voter_id in voters:
        raise ValueError(f'Voter {voter_id} has already voted for "{option}".')

    voters.add(voter_id)
    return f'Voter {voter_id} voted for "{option}".'


# ---------------------------------------------------------
# 2. GUI層 (PyQt6 ウィンドウ)
# ---------------------------------------------------------
class PollApp(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("PyQt6 投票システム")
        self.setFixedSize(500, 550)

        # 全体レイアウト
        main_layout = QVBoxLayout()

        # === 1. オプション追加エリア ===
        group_add = QGroupBox("1. 新しい選択肢の追加")
        layout_add = QHBoxLayout()

        self.input_option = QLineEdit()
        self.input_option.setPlaceholderText("例: Turkey, Morocco...")
        btn_add = QPushButton("追加")
        btn_add.clicked.connect(self.handle_add_option)

        layout_add.addWidget(self.input_option)
        layout_add.addWidget(btn_add)
        group_add.setLayout(layout_add)
        main_layout.addWidget(group_add)

        # === 2. 投票エリア ===
        group_vote = QGroupBox("2. 投票フォーム")
        layout_vote = QVBoxLayout()

        # 選択肢ドロップダウン
        layout_combo = QHBoxLayout()
        layout_combo.addWidget(QLabel("選択肢:"))
        self.combo_options = QComboBox()
        layout_combo.addWidget(self.combo_options)
        layout_vote.addLayout(layout_combo)

        # 有権者ID入力
        layout_voter = QHBoxLayout()
        layout_voter.addWidget(QLabel("有権者ID:"))
        self.input_voter = QLineEdit()
        self.input_voter.setPlaceholderText("例: user1, traveler1...")
        layout_voter.addWidget(self.input_voter)
        layout_vote.addLayout(layout_voter)

        # 投票ボタン
        btn_vote = QPushButton("投票する")
        btn_vote.clicked.connect(self.handle_vote)
        layout_vote.addWidget(btn_vote)

        group_vote.setLayout(layout_vote)
        main_layout.addWidget(group_vote)

        # === 3. リアルタイム結果表示エリア ===
        group_results = QGroupBox("3. 投票結果 (リアルタイム表示)")
        layout_results = QVBoxLayout()

        self.list_results = QListWidget()
        layout_results.addWidget(self.list_results)

        group_results.setLayout(layout_results)
        main_layout.addWidget(group_results)

        self.setLayout(main_layout)

        # 初期データのセットアップ (テスト用)
        self.setup_initial_data()

    def setup_initial_data(self):
        """初期選択肢をいくつか登録"""
        for opt in ["Turkey", "Morocco", "Spain"]:
            add_option(opt)
        self.update_ui_state()

    # ---------------------------------------------------------
    # イベントハンドラ & 描画更新
    # ---------------------------------------------------------
    def handle_add_option(self):
        """「追加」ボタン押下時"""
        opt_text = self.input_option.text()
        try:
            msg = add_option(opt_text)
            self.input_option.clear()
            self.update_ui_state()
            QMessageBox.information(self, "成功", msg)
        except ValueError as e:
            QMessageBox.warning(self, "エラー", str(e))

    def handle_vote(self):
        """「投票する」ボタン押下時"""
        selected_option = self.combo_options.currentText()
        voter_id = self.input_voter.text()

        try:
            msg = vote(selected_option, voter_id)
            self.input_voter.clear()
            self.update_ui_state()
            QMessageBox.information(self, "投票完了", msg)
        except ValueError as e:
            QMessageBox.warning(self, "エラー", str(e))

    def update_ui_state(self):
        """データ(poll)の現在状態に合わせてドロップダウンと結果リストを更新"""
        # ドロップダウン選択状態の保持
        current_selection = self.combo_options.currentText()
        self.combo_options.clear()
        self.list_results.clear()

        # 辞書からリストとドロップダウンを再構築
        for option, voters in poll.items():
            self.combo_options.addItem(option)

            # 結果リストアイテム生成
            item_text = f"{option}: {len(voters)} 票 (投票者: {', '.join(voters) if voters else 'なし'})"
            self.list_results.addItem(QListWidgetItem(item_text))

        # 以前選択していた項目を復元
        index = self.combo_options.findText(current_selection)
        if index >= 0:
            self.combo_options.setCurrentIndex(index)


# ---------------------------------------------------------
# 実行エントリーポイント
# ---------------------------------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PollApp()
    window.show()
    sys.exit(app.exec())