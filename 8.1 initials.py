def main():
    my_string = input("Enter in your First, Middle and last name: ")
    word_list = my_string.split()

    for ch in word_list:
print(ch[0] + ".")

main()

