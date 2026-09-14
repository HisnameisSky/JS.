poll = {}


def add_option(option: str) -> str:
    if not option or option.strip() == "":
        return "Option cannot be empty."

    if option in poll:
        return f'Option "{option}" already exists.'

    poll[option] = set()
    return f'Option "{option}" added to the poll.'


def vote(option: str, voter_id: str) -> str:
    if option not in poll:
        return f'Option "{option}" does not exist.'

    voters = poll[option]

    if voter_id in voters:
        return f'Voter {voter_id} has already voted for "{option}".'

    voters.add(voter_id)
    return f'Voter {voter_id} voted for "{option}".'


def display_results() -> str:
    result = "Poll Results:"
    for option, voters in poll.items():
        result += f"\n{option}: {len(voters)} votes"
    return result


print(add_option("Turkey"))  # Option "Turkey" added to the poll.
print(add_option("Morocco"))  # Option "Morocco" added to the poll.
print(add_option("Spain"))  # Option "Spain" added to the poll.

print(vote("Turkey", "user1"))  # Voter user1 voted for "Turkey".
print(vote("Turkey", "user2"))  # Voter user2 voted for "Turkey".
print(vote("Morocco", "user3"))  # Voter user3 voted for "Morocco".

print(display_results())
