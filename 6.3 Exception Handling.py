# Copy your file from the previous exercise (Average numbers) and modify it so that it handles
# the following exceptions:
# It should handle any IOError exceptions that are raised when the file is opened and data is read from it.
# It should handle any ValueError exceptions that are raised when the items that are read from the file
# are converted to a number.

def main():
    try:
        file_name = "numbers2.txt"
        numbers_file = open(file_name, 'r') # open file names numbers2.txt
        total = 0
        number_lines = 0
        line = numbers_file.readline()

        while line != "":
            number_lines += 1
            total += int(line)
            line = numbers_file.readline()
            average = total / number_lines
        numbers_file.close()
    except ValueError:
        print("There is non numeric data in the file")
    except IOError:
        print(file_name + " not found.")


main()
