def main():
    """
    Nimm is an ancient game of strategy that is named after the old German word for "take." 
    It is also called Tiouk Tiouk in West Africa and Tsynshidzi in China. Players alternate taking stones until there are zero left. 
    The game of Nimm goes as follows:
        1)The game starts with a pile of 20 stones between the players
        2)The two players alternate turns
        3)On a given turn, a player may take either 1 or 2 stone from the center pile
        4)The two players continue until the center pile has run out of stones.
    The last player to take a stone loses.
    """
    stones = 20
    while stones > 0:
        # Player 1
        stones = play_turn("Player 1", stones)
        if stones == 0:
            print("Player 2 wins!")
            break

        # Player 2
        stones = play_turn("Player 2", stones)
        if stones == 0:
            print("Player 1 wins!")
            break

def play_turn(player, stones):
    print(f"There are {stones} stones left.")
    user_input = input(f"{player} would you like to remove 1 or 2 stones? ")
    print("")
    while input_is_invalid(user_input):
        user_input = input("Please enter 1 or 2: ")
    user_input = int(user_input)
    stones -= user_input
    return stones

def input_is_invalid(user_input):
    return user_input not in ["1", "2"]

if __name__ == '__main__':
    main()