import questions
import random


def main():
    q1 = questions.question("What year did the Beatles make it big in america? ", "A. 1965", "B. 1945", "C, 1956",
                            "D, 1964")
    q2 = questions.question("Which famous musician from the Beatles was murdered in 1980? ", "A. Ringo Starr",
                            "B. John Lennon", "C. George Harrison", "D. Geezer Butler")
    q3 = questions.question("How many sides does a hexagon have?" "A. 4", "B. 6", "C. 9", "D. 7")
    q4 = questions.question("Who wrote the Harry Potter series?" "A. J.K. Rowling", "B. Stephen King",
                            "C. George R. R. Martin", "D. Thomas Kinkaid")

    all_questions = (q1, q2, q3, q4)
    print("*   Player 1   *")
    player1 = ask(all_questions)
    print("*   Player 1   *")
    player2 = ask(all_questions)

    if player1 == player2:
        print("You two are now tied!")
    elif player1 > player2:
        print("Player 1 is winner of this quiz!")
    else:
        print("Player 2 is the winner of this quiz!")


def ask(all_the_questions):
    correct = 0
    for item in range(2):
        player_questions = random.choice(all_the_questions)
        print(player_questions.get_question())
        print("A. " + player_questions.get_answer1())
        print("B. " + player_questions.get_answer2())
        print("C. " + player_questions.get_answer3())
        print("D. " + player_questions.get_answer4())
        player_response = input("Please enter the letter of your answer: ")

        if player_response.upper() == player_questions.get_correct_answer():
            print("\nNice Job! Correct!\n\n")
        else:
            print("\nSo sad. Hopefully you do better next time.\n\n")

        return correct


main()
