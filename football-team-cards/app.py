import tkinter as tk
from tkinter import ttk

football_team = {
    "team": "Argentina",
    "year": 1986,
    "headCoach": "Carlos Bilardo",
    "players": [
        {"name": "Sergio Batista", "position": "midfielder", "isCaptain": False},
        {"name": "Diego Maradona", "position": "midfielder", "isCaptain": True},
        {"name": "Jorge Valdano", "position": "forward", "isCaptain": False},
        {"name": "José Luis Brown", "position": "defender", "isCaptain": False},
        {"name": "Nery Pumpido", "position": "goalkeeper", "isCaptain": False},
    ],
}


def set_player_cards(arr):
    """配列（リスト）を受け取り、カード表示エリアをクリアして再描画する"""
    # 既存のカードをすべてクリア
    for widget in player_cards_container.winfo_children():
        widget.destroy()

    # リスト内の各プレイヤーオブジェクトからカードを作成
    for player in arr:
        card = tk.Frame(
            player_cards_container, relief=tk.RAISED, bd=2, padx=10, pady=10
        )
        card.pack(fill=tk.X, pady=5)

        title = (
            f"(Captain) {player['name']}"
            if player["isCaptain"]
            else player["name"]
        )
        title_label = tk.Label(
            card, text=title, font=("Helvetica", 12, "bold")
        )
        title_label.pack(anchor="w")

        pos_label = tk.Label(card, text=f"Position: {player['position']}")
        pos_label.pack(anchor="w")


def on_filter_change(event):
    """ドロップダウンの変更イベントハンドラ"""
    selected_value = players_dropdown.get()

    if selected_value == "all":
        set_player_cards(football_team["players"])
    else:
        filtered_players = [
            p
            for p in football_team["players"]
            if p["position"] == selected_value
        ]
        set_player_cards(filtered_players)


root = tk.Tk()
root.title("Team stats")

team_span = tk.Label(root, text=f"Team: {football_team['team']}")
team_span.pack()

year_span = tk.Label(root, text=f"Year: {football_team['year']}")
year_span.pack()

head_coach_span = tk.Label(
    root, text=f"Head coach: {football_team['headCoach']}"
)
head_coach_span.pack()

dropdown_label = tk.Label(root, text="Filter Teammates:")
dropdown_label.pack(pady=(10, 0))

players_dropdown = ttk.Combobox(
    root,
    values=["all", "forward", "midfielder", "defender", "goalkeeper"],
    state="readonly",
)
players_dropdown.set("all")
players_dropdown.pack()
players_dropdown.bind("<<ComboboxSelected>>", on_filter_change)

player_cards_container = tk.Frame(root)
player_cards_container.pack(pady=10, fill=tk.BOTH, expand=True)

set_player_cards(football_team["players"])

root.mainloop()