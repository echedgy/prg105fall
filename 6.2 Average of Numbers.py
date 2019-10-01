def main():
    input_file = open('numbers.txt', 'r')

    try:
        count = 1
        record = input_file.readline()
        record = record.rstrip('\n')
        record = int(record)
        total = record
        print("line count is: " + str(count))
        print("total value of records is: " + format(total, ','))
        print("Average of records is: " + format(total, ",.2f"))

        while record != '':
            record = input_file.readline()
            record = record.rstrip('\n')
            record = int(record)
            count += 1
            total += record
            average = total / count
            print("line count is: " + str(count))
            print("total value of records is: " + format(total, ','))
            print("Average of records is: " + format(total, ",.2f"))

    except ValueError:
        print("error: Something is wrong")

        input_file.close()


main()
