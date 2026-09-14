count = 0


def card_counter(card):
    global count  

    if card in [2, 3, 4, 5, 6]:
        count += 1
    elif card in [7, 8, 9]:
        pass  
    elif card in [10, "J", "Q", "K", "A"]:
        count -= 1

    action = "Bet" if count > 0 else "Hold"

    return f"{count} {action}"