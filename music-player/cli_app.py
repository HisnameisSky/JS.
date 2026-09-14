import sys
import random
from typing import TypedDict, Optional, List

class Song(TypedDict):
    id: int
    title: str
    artist: str
    duration: str
    src: str

ALL_SONGS: List[Song] = [
    {"id": 0, "title": "Hello World", "artist": "Rafael", "duration": "0:23", "src": "https://cdn.freecodecamp.org/curriculum/js-music-player/hello-world.mp3"},
    {"id": 1, "title": "In the Zone", "artist": "Rafael", "duration": "0:11", "src": "https://cdn.freecodecamp.org/curriculum/js-music-player/in-the-zone.mp3"},
    {"id": 2, "title": "Camper Cat", "artist": "Rafael", "duration": "0:21", "src": "https://cdn.freecodecamp.org/curriculum/js-music-player/camper-cat.mp3"},
    {"id": 3, "title": "Electronic", "artist": "Rafael", "duration": "0:15", "src": "https://cdn.freecodecamp.org/curriculum/js-music-player/electronic.mp3"},
    {"id": 4, "title": "Sailing Away", "artist": "Rafael", "duration": "0:22", "src": "https://cdn.freecodecamp.org/curriculum/js-music-player/sailing-away.mp3"},
]

class MockAudio:
    def __init__(self):
        self.src: str = ""
        self.title: str = ""
        self.current_time: float = 0.0
        self.is_playing: bool = False

    def play(self):
        self.is_playing = True

    def pause(self):
        self.is_playing = False


class MusicPlayer:
    def __init__(self):
        self.audio = MockAudio()
        self.user_data = {
            "songs": ALL_SONGS.copy(),
            "current_song": None,
            "song_current_time": 0.0,
        }
        # シャッフル再生の状態
        self.is_shuffled: bool = False

    def toggle_shuffle(self) -> None:
        """シャッフルモードのON/OFFを切り替える"""
        self.is_shuffled = not self.is_shuffled

    def play_song(self, song_id: int, start: bool = True) -> None:
        song = next((s for s in self.user_data["songs"] if s["id"] == song_id), None)
        if not song:
            return

        self.audio.src = song["src"]
        self.audio.title = song["title"]

        if self.user_data["current_song"] is None or start:
            self.audio.current_time = 0.0
        else:
            self.audio.current_time = self.user_data["song_current_time"]

        self.user_data["current_song"] = song
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
        """次の曲を取得（シャッフルモード有効時はランダムに選曲）"""
        songs = self.user_data["songs"]
        if not songs:
            return None

        # シャッフルモード有効時
        if self.is_shuffled:
            current = self.user_data["current_song"]
            # 現在再生中の曲以外の曲候補を作成
            remaining_songs = [s for s in songs if s != current]
            if remaining_songs:
                return random.choice(remaining_songs)
            return current

        # 通常再生時
        index = self.get_current_song_index()
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
            # 再生中でない場合、シャッフル有効ならランダムに選曲、無効なら最初の曲
            if self.is_shuffled:
                random_song = random.choice(self.user_data["songs"])
                self.play_song(random_song["id"])
            else:
                self.play_song(self.user_data["songs"][0]["id"])
            return

        next_song = self.get_next_song()
        if next_song:
            self.play_song(next_song["id"])
        else:
            self.user_data["current_song"] = None
            self.user_data["song_current_time"] = 0.0
            self.pause_song()


# --- CLI ユーザーインターフェース ---
def print_ui(player: MusicPlayer):
    current = player.user_data["current_song"]
    audio = player.audio

    print("\n" + "=" * 50)
    print("           Terminal Music Player")
    print("=" * 50)

    # 現在の再生状態とシャッフル状態を表示
    shuffle_status = "🔀 ON" if player.is_shuffled else "➡️ OFF"
    if current:
        status_icon = "▶ 再生中" if audio.is_playing else "⏸ 一時停止"
        print(f"ステータス   : {status_icon}")
        print(f"シャッフル   : {shuffle_status}")
        print(f"現在再生中   : {current['title']} - {current['artist']} [{current['duration']}]")
    else:
        print("ステータス   : 停止中 (曲が選択されていません)")
        print(f"シャッフル   : {shuffle_status}")

    print("-" * 50)
    print("【プレイリスト】")
    for song in player.user_data["songs"]:
        is_current = current and current["id"] == song["id"]
        marker = " ➔ " if is_current else "    "
        print(f"{marker}[ID: {song['id']}] {song['title']} - {song['artist']} ({song['duration']})")

    print("-" * 50)
    print("操作コマンド:")
    print("  p : 再生 / 一時停止 (Play/Pause)")
    print("  n : 次の曲 (Next)")
    print("  b : 前の曲 (Previous/Back)")
    print("  s : シャッフル切替 (Toggle Shuffle)")
    print("  0-4 : 指定したIDの曲を再生")
    print("  q : 終了")
    print("=" * 50)


def run_cli():
    player = MusicPlayer()

    while True:
        print_ui(player)
        command = input("コマンドを入力してください > ").strip().lower()

        if command == "q":
            print("\nプレーヤーを終了します。")
            sys.exit(0)

        elif command == "p":
            if player.user_data["current_song"] is None:
                player.play_song(player.user_data["songs"][0]["id"])
            elif player.audio.is_playing:
                player.pause_song()
            else:
                player.play_song(player.user_data["current_song"]["id"], start=False)

        elif command == "n":
            player.play_next_song()

        elif command == "b":
            player.play_previous_song()

        elif command == "s":
            player.toggle_shuffle()

        elif command.isdigit():
            song_id = int(command)
            target_song = next((s for s in player.user_data["songs"] if s["id"] == song_id), None)
            if target_song:
                player.play_song(song_id)
            else:
                input("\n[!] 該当するIDの曲が存在しません。Enterキーを押して続行...")

        else:
            input("\n[!] 無効なコマンドです。Enterキーを押して続行...")


if __name__ == "__main__":
    run_cli()