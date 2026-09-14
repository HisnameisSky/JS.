import sys
from PyQt6.QtCore import Qt, QUrl
from PyQt6.QtMultimedia import QAudioOutput, QMediaPlayer
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

# ドラムパッドのデータ定義 (JavaScriptの drumPads と同じ構造)
DRUM_PADS = [
    {
        "key": "Q",
        "id": "Heater 1",
        "src": "https://cdn.freecodecamp.org/curriculum/drum/Heater-1.mp3",
    },
    {
        "key": "W",
        "id": "Heater 2",
        "src": "https://cdn.freecodecamp.org/curriculum/drum/Heater-2.mp3",
    },
    {
        "key": "E",
        "id": "Heater 3",
        "src": "https://cdn.freecodecamp.org/curriculum/drum/Heater-3.mp3",
    },
    {
        "key": "A",
        "id": "Heater 4",
        "src": "https://cdn.freecodecamp.org/curriculum/drum/Heater-4_1.mp3",
    },
    {
        "key": "S",
        "id": "Clap",
        "src": "https://cdn.freecodecamp.org/curriculum/drum/Heater-6.mp3",
    },
    {
        "key": "D",
        "id": "Open-HH",
        "src": "https://cdn.freecodecamp.org/curriculum/drum/Dsc_Oh.mp3",
    },
    {
        "key": "Z",
        "id": "Kick-n'-Hat",
        "src": "https://cdn.freecodecamp.org/curriculum/drum/Kick_n_Hat.mp3",
    },
    {
        "key": "X",
        "id": "Kick",
        "src": "https://cdn.freecodecamp.org/curriculum/drum/RP4_KICK_1.mp3",
    },
    {
        "key": "C",
        "id": "Closed-HH",
        "src": "https://cdn.freecodecamp.org/curriculum/drum/Cev_H2.mp3",
    },
]


class DrumMachine(QWidget):

    def __init__(self):
        super().__init__()
        self.players = {}
        self.audio_outputs = {}
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Drum Machine")
        self.setStyleSheet("background-color: #1e293b; color: white;")

        # メインレイアウト (#drum-machine に相当)
        main_layout = QVBoxLayout()

        # タイトル
        title = QLabel("DRUM MACHINE")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet(
            "font-size: 20px; font-weight: bold; color: #cbd5e1; margin-bottom: 10px;"
        )
        main_layout.addWidget(title)

        # ディスプレイ要素 (#display に相当)
        self.display = QLabel("Drum Machine")
        self.display.setObjectName("display")
        self.display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.display.setStyleSheet(
            "background-color: #0f172a; border: 1px solid #334155; "
            "color: #22d3ee; font-size: 18px; font-weight: bold; padding: 15px; border-radius: 8px;"
        )
        main_layout.addWidget(self.display)

        # パッドのグリッド (#pad-bank に相当)
        grid_layout = QGridLayout()

        for index, pad in enumerate(DRUM_PADS):
            # ボタンの生成
            btn = QPushButton(pad["key"])
            btn.setStyleSheet(
                "background-color: #334155; color: white; font-size: 20px; font-weight: bold; "
                "padding: 20px; border-radius: 8px; border: 1px solid #475569;"
            )

            # 音声プレーヤーの初期化 (<audio> タグに相当)
            player = QMediaPlayer()
            audio_output = QAudioOutput()
            player.setAudioOutput(audio_output)
            player.setSource(QUrl(pad["src"]))

            self.players[pad["key"]] = player
            self.audio_outputs[pad["key"]] = audio_output

            # クリックイベントの接続
            btn.clicked.connect(
                lambda checked, k=pad["key"], sound_id=pad["id"]: self.play_sound(
                    k, sound_id
                )
            )

            # 3x3 のグリッドに配置
            row = index // 3
            col = index % 3
            grid_layout.addWidget(btn, row, col)

        main_layout.addLayout(grid_layout)
        self.setLayout(main_layout)

    # サウンド再生と表示更新関数 (JavaScriptの playSound に相当)
    def play_sound(self, key, sound_id):
        if key in self.players:
            player = self.players[key]
            player.setPosition(0)  # 頭出し (audio.currentTime = 0)
            player.play()  # 再生 (audio.play())
            self.display.setText(sound_id)  # ディスプレイ更新 (setDisplayText)

    # キーボードイベントハンドラ (JavaScriptの handleKeyDown に相当)
    def keyPressEvent(self, event):
        key_text = event.text().upper()
        # 押されたキーに該当するパッドを検索
        target_pad = next(
            (pad for pad in DRUM_PADS if pad["key"] == key_text), None
        )
        if target_pad:
            self.play_sound(target_pad["key"], target_pad["id"])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DrumMachine()
    window.show()
    sys.exit(app.exec())