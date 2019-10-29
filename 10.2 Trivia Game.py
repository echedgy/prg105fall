import questions class


def main():
    q1 = questions.Question("What year did the Beatles make it big in america? ", "A. 1965", "B. 1945", "C, 1956", "D, 1964")
    q2 = questions.Question("Which famous musician from the Beatles was murdered in 1980? ", "A. Ringo Starr", "B. John Lennon", "C. George Harrison", "D. Geezer Butler")
    q3 = questions.Question("How many sides does a hexagon have?" "A. 4", "B. 6", "C. 9", "D. 7")
    q4 = questions.Question("Who wrote the Harry Potter series?" "A. J.K. Rowling", "B. Stephen King", "C. George R. R. Martin", "D. Thomas Kinkaid")

    player1 = 0
    player2 = 0

    set_1 = (q1, q2)
    set_2 = (q3, q4)

    print("Player 1: ")
    for query in set_1:
        print("\n")
        print(query.get_questions())
        print(query.get_a1())
        print(query.get_a2())
        print(query.get_a3())
        print(query.get_a4())
        guess = input("Please enter the letter of the right answer: ")
        if guess.upper() == query.get_answer():
            print("Correct!!")
            player1 += 1

    print("Player 1 has earned: " + str(player1) + " points ")

    print("Player 2: ")
    for query in set_2:
        print("\n")
        print(query.get_questions())
        print(query.get_a1())
        print(query.get_a2())
        print(query.get_a3())
        print(query.get_a4())
        guess = input("Please enter the letter of the correct answer: ")
        if guess.upper() == query.get_answer():
            print("Correct!!")
            player2 += 1

    print("Player 2 has earned: " + str(player2) + " points ")

    main()
