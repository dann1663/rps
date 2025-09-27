"""
Rock-Paper-Scissors game implemented in Python.

This script allows a human player to play against a bot. 
The bot's choice is generated randomly, while the human player 
provides input that is validated and converted into one of the 
valid options.

The game then compares both choices and prints the result: 
win, lose, or draw.

"""
Rock-Paper-Scissors game implemented in Python.

This script allows a human player to play against a bot. 
The bot's choice is generated randomly, while the human player 
provides input that is validated and converted into one of the 
valid options.

The game then compares both choices and prints the result: 
win, lose, or draw.

Modules:
    - random (for generating the bot's choice)
"""
import random

def bot_choice():
    """
    Picking a element randomly from array
    
    RETURN:
    a random "choice"
    """
    options = ["Rock", "Paper", "Scissor"]
    return random.choice(options)

def human_choice(n: int | str | None = None) -> str:
    """
    Handles the player's choice in Rock-Paper-Scissors.

    This function accepts a player's choice,
    validates it, and returns one of the valid options: 
    "Rock", "Scissor", or "Paper".

    If the input cannot be recognized, it returns 
    "forkert input, prøv igen" (Danish for "wrong input, try again").

    Args:
        n (int | str | None, optional): 
            - Can be an integer (1, 2, or 3)
            - A string ("rock", "paper", "scissor", or their numeric equivalents)
            - None

    Returns:
        str: 
            - "Rock", "Scissor", or "Paper" if the input is valid
            - "forkert input, prøv igen" if the input is invalid
    """
    
    if n  is None or n == "":
        n = input("Vælg:\n 1 = rock\n 2 = scissor\n 3 = paper\n\n")
    elif isinstance(n, str):
        n = n.strip().lower()    
    
    match n:
        case 1 | "1" | "rock":
            return "Rock"
        case 2 | "2" | "scissor":
            return "Scissor"
        case 3 | "3" | "paper":
            return "Paper"
        case _:
            return "forkert input, prøv igen"

def decision(p1:str, p2:str) -> str:
    """
    Compares the players choice against bot's choice'
    and return the result as a string

    Args:
        p1(str): player's choice(Rock, paper, scissor or an error)
        p2(st): bot's choice (rock, paper, scissor)
    
    Returns:
        str: A message describing the result
            - If the player wins -> "du vandt"
            - If the player lose -> "du tabte"
            - If draw -> "uafgjort"

    """
    if p1 == "forkert input, prøv igen":
        return p1
    if p1 == p2:
        return "Uafgjort"

    rules = {
        ("Rock", "Scissor"): "Du vandt",
        ("Scissor", "Paper"): "Du vandt",
        ("Paper", "Rock"): "Du vandt",

        ("Scissor", "Rock"): "Du tabte",
        ("Paper", "Scissor"): "Du tabte",
        ("Rock", "Paper"): "Du tabte",

    }
    return rules[(p1, p2)]

def main():
    """
    Prompts the player's and bot's for a choice,
    and prints both choices with the result.
    """
    print("Velkommen til sten, saks og papir")
    h = human_choice()
    b = bot_choice()
    print(f"Du: {h} | Bot: {b}")
    print(decision(h,b))

if __name__ == "__main__":
    main()

Modules:
    - random (for generating the bot's choice)
"""
import random

def bot_choice():
    """
    Picking a element randomly from array
    
    RETURN:
    a random "choice"
    """
    options = ["Rock", "Paper", "Scissor"]
    return random.choice(options)

def human_choice(n: int | str | None = None) -> str:
    """
    Handles the player's choice in Rock-Paper-Scissors.

    This function accepts a player's choice,
    validates it, and returns one of the valid options: 
    "Rock", "Scissor", or "Paper".

    If the input cannot be recognized, it returns 
    "forkert input, prøv igen" (Danish for "wrong input, try again").

    Args:
        n (int | str | None, optional): 
            - Can be an integer (1, 2, or 3)
            - A string ("rock", "paper", "scissor", or their numeric equivalents)
            - None

    Returns:
        str: 
            - "Rock", "Scissor", or "Paper" if the input is valid
            - "forkert input, prøv igen" if the input is invalid
    """
    
    if n  is None or n == "":
        n = input("Vælg:\n 1 = rock\n 2 = scissor\n 3 = paper\n\n")
    elif isinstance(n, str):
        n = n.strip().lower()    
    
    match n:
        case 1 | "1" | "rock":
            return "Rock"
        case 2 | "2" | "scissor":
            return "Scissor"
        case 3 | "3" | "paper":
            return "Paper"
        case _:
            return "forkert input, prøv igen"

def decision(p1:str, p2:str) -> str:
    """
    Compares the players choice against bot's choice'
    and return the result as a string

    Args:
        p1(str): player's choice(Rock, paper, scissor or an error)
        p2(st): bot's choice (rock, paper, scissor)
    
    Returns:
        str: A message describing the result
            - If the player wins -> "du vandt"
            - If the player lose -> "du tabte"
            - If draw -> "uafgjort"

    """
    if p1 == "forkert input, prøv igen":
        return p1
    if p1 == p2:
        return "Uafgjort"

    rules = {
        ("Rock", "Scissor"): "Du vandt",
        ("Scissor", "Paper"): "Du vandt",
        ("Paper", "Rock"): "Du vandt",

        ("Scissor", "Rock"): "Du tabte",
        ("Paper", "Scissor"): "Du tabte",
        ("Rock", "Paper"): "Du tabte",

    }
    return rules[(p1, p2)]

def main():
    """
    Prompts the player's and bot's for a choice,
    and prints both choices with the result.
    """
    print("Velkommen til sten, saks og papir")
    h = human_choice()
    b = bot_choice()
    print(f"Du: {h} | Bot: {b}")
    print(decision(h,b))

if __name__ == "__main__":
    main()

