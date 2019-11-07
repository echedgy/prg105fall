import questions
import random


def main():

    q1 = questions.Question("What year did the Beatles make it big in america? ", "A. 1965", "B. 1945", "C, 1956", "D, 1964")
    q2 = questions.Question("Which famous musician from the Beatles was murdered in 1980? ", "A. Ringo Starr", "B. John Lennon", "C. George Harrison", "D. Geezer Butler")
    q3 = questions.Question("How many sides does a hexagon have?" "A. 4", "B. 6", "C. 9", "D. 7")
    q4 = questions.Question("Who wrote the Harry Potter series?" "A. J.K. Rowling", "B. Stephen King", "C. George R. R. Martin", "D. Thomas Kinkaid")
    q5 = questions.Question("Whos the main character of the Harry Potter series?" "A. Tigger", "B. John Wayne Gacy", "C. Harry Potter", "D. Morpheus")
    q6 = questions.Question("Which band wrote the hit song: T.N.T?" "A. Led Zeppelin", "B. AC/DC", "C. The Ramones", "D. The Who")
    q7 = questions.Question("How many Queens of the Stone Age albums are there?" "A. 4", "B. 9", "C. 7", "D. 6")
    q8 = questions.Question("Who wrote the Game of Thrones books?" "A. Stephen King", "B. JK Rowling", "C. James Patterson", "D. George RR Martin")
    q9 = questions.Question("The Beatles kick started which musical explosion?" "A. The British Invasion", "B. The Grunge scene" "C. The Garage Rock Revival scene", 'D. Glam Rock')
    q10 = questions.Question("What band was did the late Lemmy Kilminster form?" "A. Metallica", "B. Motorhead", "C. Opeth", "D. Kyuss")

    all_questions = (q1, q2, q3, q4, q5, q6, q7, q8, q9, q10)
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
    for item in range(5):
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
