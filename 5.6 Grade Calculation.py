def calc_average(score1, score2, score3, score4, score5):
    average = (score1 + score2 + score3 + score4 + score5) / 5

    return average


def determine_grade(user_score):
    if user_score < 60:
        return "F"
    elif user_score < 70:
        return "D"
    elif user_score < 80:
        return "C"
    elif user_score < 90:
        return "B"
    elif user_score < 101:
        return "A"


def ask_for_scores():
    score1 = float(input(" Please enter your first score: "))
    score2 = float(input(" Please enter your second score: "))
    score3 = float(input(" Please enter your third score: "))
    score4 = float(input(" Please enter your fourth score: "))
    score5 = float(input(" Please enter your fifth score: "))

    return score1, score2, score3, score4, score5


def print_table_of_results(score1, score2, score3, score4, score5):
    print("Score\tLetter Grade")
    print(str(score1) + "\t\t" + determine_grade(score1), str(score2) + "\t\t" + determine_grade(score2), str(score3) + "\t\t" + determine_grade(score3), str(score4) + "\t\t" + determine_grade(score4), str(score5) + "\t\t" + determine_grade(score5), sep ="\n")


def main():
    score1, score2, score3, score4, score5 = ask_for_scores()
    print_table_of_results(score1, score2, score3, score4, score5)
    print("Your average is", calc_average(score1, score2, score3, score4, score5))

main()
