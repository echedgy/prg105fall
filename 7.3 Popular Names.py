def main():

    variable_file = open('BoyNames.txt' 'w')
    boy_names = variable_file.readlines()

    variable_file.close()

    index = 0
    while index < len(boy_names):
        boy_names[index] = boy_names[index].rstrip('\n')
        index += 1

    print(boy_names)


