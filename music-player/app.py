from typing import TypedDict, Optional, List

# 曲オブジェクトのデータ型定義
class Song(TypedDict):
    id: int
    title: str
    artist: str
    duration: str
    src: str

# 初期楽曲リスト（JSの allSongs 配列に相当）
ALL_SONGS: List[Song] = [
    {
        "id": 0,
        "title": "Hello World",
        "artist": "Rafael",
        "duration": "0:23",
        "src": "https://cdn.freecodecamp.org/curriculum/js-music-player/hello-world.mp3",
    },
    {
        "id": 1,
        "title": "In the Zone",
        "artist": "Rafael",
        "duration": "0:11",
        "src": "https://cdn.freecodecamp.org/curriculum/js-music-player/in-the-zone.mp3",
    },
    {
        "id": 2,
        "title": "Camper Cat",
        "artist": "Rafael",
        "duration": "0:21",
        "src": "https://cdn.freecodecamp.org/curriculum/js-music-player/camper-cat.mp3",
    },
    {
        "id": 3,
        "title": "Electronic",
        "artist": "Rafael",
        "duration": "0:15",
        "src": "https://cdn.freecodecamp.org/curriculum/js-music-player/electronic.mp3",
    },
    {
        "id": 4,
        "title": "Sailing Away",
        "artist": "Rafael",
        "duration": "0:22",
        "src": "https://cdn.freecodecamp.org/curriculum/js-music-player/sailing-away.mp3",
    },
]

# Audioオブジェクトの挙動を再現する疑似クラス
class MockAudio:
    def __init__(self):
        self.src: str = ""
        self.title: str = ""
        self.current_time: float = 0.0
        self.is_playing: bool = False

    def play(self):
        self.is_playing = True
        print(f"[Audio] 再生中: {self.title} ({self.src})")

    def pause(self):
        self.is_playing = False
        print(f"[Audio] 一時停止 (再生位置: {self.current_time}秒)")


class MusicPlayer:
    def __init__(self):
        self.audio = MockAudio()
        # JSの userData オブジェクトに相当
        self.user_data = {
            "songs": ALL_SONGS.copy(),
            "current_song": None,  # Optional[Song]
            "song_current_time": 0.0,
        }

    # IDから対象曲の曲ID「荷物」を検索して再生を開始する
    def play_song(self, song_id: int, start: bool = True) -> None:
        # IDに一致する曲を検索 (JSの Array.prototype.find に相当)
        song = next((s for s in self.user_data["songs"] if s["id"] == song_id), None)
        if not song:
            return

        self.audio.src = song["src"]
        self.audio.title = song["title"]

        if self.user_data["current_song"] is None or start:
            self.audio.current_time = 0.0
        else:
            self.audio.current_time = self.user_data["song_current_time"]

        # 「荷物（状態）」の更新
        self.user_data["current_song"] = song
        self.set_player_display()
        self.highlight_current_song()
        self.set_play_button_accessible_text()
        self.audio.play()

    def pause_song(self) -> None:
        self.user_data["song_current_time"] = self.audio.current_time
        self.audio.pause()

    def get_current_song_index(self) -> int:
        current = self.user_data["current_song"]
        if current is None:
            return -1
        try:
            return self.user_data["songs"].index(current)
        except ValueError:
            return -1

    def get_next_song(self) -> Optional[Song]:
        index = self.get_current_song_index()
        songs = self.user_data["songs"]
        if 0 <= index < len(songs) - 1:
            return songs[index + 1]
        return None

    def get_previous_song(self) -> Optional[Song]:
        index = self.get_current_song_index()
        songs = self.user_data["songs"]
        if index > 0:
            return songs[index - 1]
        return None

    def play_previous_song(self) -> None:
        if self.user_data["current_song"] is None:
            return
        prev_song = self.get_previous_song()
        if prev_song:
            self.play_song(prev_song["id"])
        else:
            self.play_song(self.user_data["songs"][0]["id"])

    def play_next_song(self) -> None:
        if self.user_data["current_song"] is None:
            self.play_song(self.user_data["songs"][0]["id"])
            return

        next_song = self.get_next_song()
        if next_song:
            self.play_song(next_song["id"])
        else:
            self.user_data["current_song"] = None
            self.user_data["song_current_time"] = 0.0
            self.set_player_display()
            self.highlight_current_song()
            self.set_play_button_accessible_text()
            self.pause_song()

    # --- UI更新用処理（Terminalログ出力で代用） ---
    def set_player_display(self) -> None:
        song = self.user_data["current_song"]
        title = song["title"] if song else ""
        artist = song["artist"] if song else ""
        print(f"[UI更新] タイトル: '{title}', アーティスト: '{artist}'")

    def highlight_current_song(self) -> None:
        song = self.user_data["current_song"]
        song_id = song["id"] if song else None
        print(f"[UI更新] ハイライト曲ID: {song_id}")

    def set_play_button_accessible_text(self) -> None:
        song = self.user_data["current_song"]
        label = f"Play {song['title']}" if song else "Play"
        print(f"[UI更新] ボタンアクセシビリティ: '{label}'")