def main():
    name = input("Enter in your First, Middle and last name: ")

    initials = ""
    name_list = name.split()
    print(name_list)
    for part in name_list:
        initials = initials + part[0:1].upper() + ", "

    print(initials)


main()
