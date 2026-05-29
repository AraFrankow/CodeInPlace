"""
    Math Challenge Game - Stanford CS106A Project

    A progressive difficulty math game where players solve addition problems
    across three levels. Players have 3 lives and must reach score targets
    to advance. Features two difficulty modes: easy and normal.

    Game Flow:
    - Level 1: Numbers 1-15
    - Level 2: Numbers 20-50  
    - Level 3: Numbers 100-500

    Difficulty Settings:
    - Easy: 5/10/15 correct answers per level
    - Normal: 10/20/30 correct answers per level
"""
import random

def play_level(min_num, max_num, target_score, cont_pass, cont_death):

    while cont_death < 3:

        num1 = random.randint(min_num, max_num)
        num2 = random.randint(min_num, max_num)

        correct_answer = num1 + num2

        print(f"\nWhat is {num1} + {num2}?")

        answer_user = int(input("Your answer: "))

        if answer_user == correct_answer:
            print("Correct!")
            cont_pass += 1

            print(f"Score: {cont_pass}")

            if cont_pass == target_score:
                break

        else:
            print(f"Incorrect.")
            print(f"The expected answer is {correct_answer}")

            cont_death += 1

            print(f"Lives lost: {cont_death}/3")

            if cont_death == 3:
                break

    return cont_pass, cont_death


def main():

    print("=== WELCOME TO MY GAME ===")

    # Difficulty selection
    difficulty = input(
        "Choose difficulty (easy / normal): "
    ).lower()

    if difficulty == "easy":
        level1_goal = 5
        level2_goal = 10
        level3_goal = 15
    elif difficulty == "normal":
        level1_goal = 10
        level2_goal = 20
        level3_goal = 30
    else:
        print("This is not a difficulty")
        return

    cont_pass = 0
    cont_death = 0

    # LEVEL 1
    print("=== LEVEL 1 ===")

    cont_pass, cont_death = play_level(
        1, 15,
        level1_goal,
        cont_pass,
        cont_death
    )

    if cont_death == 3:
        print(f"\nGAME OVER")
        print(f"Final score: {cont_pass}")
        return

    print("Great job!")

    # LEVEL 2
    print("=== LEVEL 2 ===")

    cont_pass, cont_death = play_level(
        20, 50,
        level2_goal,
        cont_pass,
        cont_death
    )

    if cont_death == 3:
        print(f"\nGAME OVER")
        print(f"Final score: {cont_pass}")
        return

    print("Awesome!")

    # LEVEL 3
    print("=== LEVEL 3 ===")
    print("Final challenge!")

    cont_pass, cont_death = play_level(
        100, 500,
        level3_goal,
        cont_pass,
        cont_death
    )

    # Final result
    if cont_pass == level3_goal:
        print("CONGRATS!!! YOU WIN!")

    else:
        print("\nGAME OVER")
        print(f"Final score: {cont_pass}")


if __name__ == '__main__':
    main()