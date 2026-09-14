import random
import tkinter as tk

OPTIONS = ["Rock", "Paper", "Scissors"]

player_score = 0
computer_score = 0


def get_random_computer_result():
    """コンピュータの手をランダムに取得"""
    return random.choice(OPTIONS)


def has_player_won_the_round(player_choice, computer_choice):
    """プレイヤーの勝利判定（Booleanを返す）"""
    return (
        (player_choice == "Rock" and computer_choice == "Scissors")
        or (player_choice == "Scissors" and computer_choice == "Paper")
        or (player_choice == "Paper" and computer_choice == "Rock")
    )


def get_round_results(user_option):
    """ラウンド結果メッセージの生成とスコアの加算"""
    global player_score, computer_score
    computer_result = get_random_computer_result()

    if has_player_won_the_round(user_option, computer_result):
        player_score += 1
        return f"Player wins! {user_option} beats {computer_result}"
    elif computer_result == user_option:
        return f"It's a tie! Both chose {user_option}"
    else:
        computer_score += 1
        return f"Computer wins! {computer_result} beats {user_option}"


def show_results(user_option):
    """結果の画面表示とゲーム終了判定"""
    result_text = get_round_results(user_option)

    round_results_msg.config(text=result_text)
    computer_score_span.config(text=str(computer_score))
    player_score_span.config(text=str(player_score))

    if player_score == 3 or computer_score == 3:
        winner = "Player" if player_score == 3 else "Computer"
        winner_msg.config(text=f"{winner} has won the game!")

        reset_game_btn.pack()  
        options_container.pack_forget()  


def reset_game():
    """ゲーム状態のリセット"""
    global player_score, computer_score
    player_score = 0
    computer_score = 0

    player_score_span.config(text=str(player_score))
    computer_score_span.config(text=str(computer_score))

    reset_game_btn.pack_forget()  
    options_container.pack()  

    winner_msg.config(text="")
    round_results_msg.config(text="")


root = tk.Tk()
root.title("Rock, Paper, Scissors game")

score_frame = tk.Frame(root)
score_frame.pack(pady=10)

player_score_span = tk.Label(score_frame, text="0")
player_score_span.pack(side=tk.LEFT, px=10)

computer_score_span = tk.Label(score_frame, text="0")
computer_score_span.pack(side=tk.RIGHT, px=10)

options_container = tk.Frame(root)
options_container.pack(pady=10)

rock_btn = tk.Button(
    options_container, text="Rock", command=lambda: show_results("Rock")
)
rock_btn.pack(side=tk.LEFT)

paper_btn = tk.Button(
    options_container, text="Paper", command=lambda: show_results("Paper")
)
paper_btn.pack(side=tk.LEFT)

scissors_btn = tk.Button(
    options_container,
    text="Scissors",
    command=lambda: show_results("Scissors"),
)
scissors_btn.pack(side=tk.LEFT)

results_container = tk.Frame(root)
results_container.pack(pady=10)

round_results_msg = tk.Label(results_container, text="")
round_results_msg.pack()

winner_msg = tk.Label(results_container, text="")
winner_msg.pack()

reset_game_btn = tk.Button(results_container, text="Play again?", command=reset_game)

root.mainloop()