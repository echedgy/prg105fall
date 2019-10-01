def main():
    list_file = open("names (2).txt", "r")

    list = list_file.readline()

    while list != "":
        print(list)
        list = list_file.readline()

    list_file.close

