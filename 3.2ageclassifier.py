user_age = int(input("How old are you?"))
if user_age <= 1:
    print(" you are an infant")
    if user_age < 13:
        print(" you are a child")
        if user_age < 20:
            print("You must be a teen")
        else:
            print("You are an adult")
