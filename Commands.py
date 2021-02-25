import string
from string import ascii_lowercase


def createHall(line_split, hall_list, halls_dict):
    print("")
    hall_name = line_split[1]
    line_split[2] = line_split[2].rstrip('\n')
    hall_size = line_split[2].split("x")
    # print(hall_size)
    if hall_name in hall_list:
        print("Warning: Cannot create the hall for the second time. The cinema has already " + hall_name)
    else:
        hall_list.append(hall_name)

        row_num = int(hall_size[0])
        col_num = int(hall_size[1])

        hall_array = [["X" for x in range(row_num)] for x in range(col_num)]
        # print(hall_array)
        '''
        for i in range(len(hall_array)):
            for j in range(len(hall_array[i])):
                print(hall_array[i][j], end=" ")
            print("\n")
        '''
        halls_dict[hall_name] = hall_array

        print("The hall " + hall_name + " having  " + str(row_num * col_num) + " seats has been created")


def sellTicket(line_split, hall_list, halls_dict, customer_list):
    print("")

    customer_name = line_split[1]
    customer_type = line_split[2]
    hall_name = line_split[3]

    # print("customer type = ", customer_type)
    customer_letter = ""
    if customer_type == "full":
        customer_letter = "F"
    elif customer_type == "student":
        customer_letter = "S"

    if customer_name in customer_list:
        print("unique id problem")
    elif hall_name not in hall_list:
        print("unknown hall")
    elif customer_type != "full" and customer_type != "student":
        print("unknown type of customer")
    else:
        space_split = []
        for i in range(4, len(line_split)):
            space_split.append(line_split[i])
        # print(space_split)

        for i in space_split:
            row_num = int(letterToNumerics(i[0]))
            if '-' in i:
                seat_line = i[1:]
                seat_line_split = seat_line.split("-")

                col_num_start = int(seat_line_split[0])
                col_num_finish = int(seat_line_split[1])

                if col_num_finish > len(halls_dict[hall_name]):
                    print("Error: The hall '" + hall_name + "' has less column than the specified index " + i.rstrip(
                        "\n") + "!")
                    continue
                full = False
                for j in range(col_num_start, col_num_finish):
                    if halls_dict[hall_name][row_num][j] == 'X':
                        continue
                    else:
                        full = True
                        print("Warning: The seats " + i.rstrip(
                            '\n') + " cannot be sold to " + customer_name + " due some of them have already been sold")

                if not full:
                    print("Success: " + customer_name + " has bought " + i.rstrip('\n') + " at " + hall_name)
                    customer_list.append(customer_name)
                    for k in range(col_num_start, col_num_finish):
                        halls_dict[hall_name][row_num][k] = customer_letter

            else:
                # print(i)
                col_num = int(i[1])
                if col_num > len(halls_dict[hall_name]):
                    print("Error: The hall '" + hall_name + "' has less column than the specified index " + i.rstrip(
                        "\n") + "!")
                    continue
                if halls_dict[hall_name][row_num][col_num] == 'X':
                    halls_dict[hall_name][row_num][col_num] = customer_letter
                    print("Success: " + customer_name + " has bought " + i.rstrip('\n') + " at " + hall_name)
                    customer_list.append(customer_name)
                else:
                    print("Warning: The seats " + i.rstrip(
                        '\n') + "cannot be sold to " + customer_name + "due some of them have already been sold")

        # print(halls_dict[hall_name])


def cancelTicket(line_split, hall_list, halls_dict, customer_list):
    print("")

    hall_name = line_split[1].rstrip("\n")

    if hall_name not in hall_list:
        print("unknown hall")
    else:
        space_split = []
        for i in range(2, len(line_split)):
            space_split.append(line_split[i])
        # print(space_split)

        for i in space_split:
            row_num = int(letterToNumerics(i[0]))
            if '-' in i:
                seat_line = i[1:]
                seat_line_split = seat_line.split("-")

                col_num_start = int(seat_line_split[0])
                col_num_finish = int(seat_line_split[1])

                if col_num_finish > len(halls_dict[hall_name]):
                    print("Error: The hall '" + hall_name + "' has less column than the specified index " + i.rstrip(
                        "\n") + "!")
                    continue
                full = True
                for j in range(col_num_start, col_num_finish):
                    if halls_dict[hall_name][row_num][j] == 'X':
                        continue
                    else:
                        full = False
                        print("Error: The seat " + i.rstrip(
                            "\n") + " at " + hall_name + " has already been free! Nothing to cancel")

                if full:
                    print("Success: The seat " + i.rstrip(
                        "\n") + " at " + hall_name + " has been canceled and now ready to be sold again")
                    for k in range(col_num_start, col_num_finish):
                        halls_dict[hall_name][row_num][k] = "X"

            else:
                # print(i)
                col_str =""
                if len(i)>3:
                    for j in range(1, len(i)):
                        col_str += i[j]
                    col_num = int(col_str)
                else:
                    col_num = int(i[1])

                if col_num > len(halls_dict[hall_name]):
                    print("Error: The hall '" + hall_name + "' has less column than the specified index " + i.rstrip(
                        "\n") + "!")
                    continue
                if halls_dict[hall_name][row_num][col_num] == 'X':
                    print("Error: The seat " + i.rstrip(
                        "\n") + " at " + hall_name + " has already been free! Nothing to cancel")
                else:
                    halls_dict[hall_name][row_num][col_num] = "X"
                    print("Success: The seat " + i.rstrip(
                        "\n") + " at " + hall_name + " has been canceled and now ready to be sold again")

        # print(halls_dict[hall_name])


def showhall(hall_name, halls_dict):
    print("")
    print("Printing hall layout of " + hall_name)
    for i in reversed(range(len(halls_dict[hall_name]))):
        d = dict(enumerate(string.ascii_uppercase, 0))

        print(d[i], end="  ")
        for j in range(len(halls_dict[hall_name][i])):
            print(halls_dict[hall_name][i][j], end=" ")
            print(" ", end=" ")
        print()

    print(" ", end=" ")
    for i in range(len(halls_dict[hall_name])):
        print(i, end=" ")
        print(" ", end=" ")


def balance(hall_name, halls_dict):
    print("")
    print("Hall report of '" + hall_name + "'")
    print("-------------------------")
    sum_stu = 0
    sum_full = 0
    for i in reversed(range(len(halls_dict[hall_name]))):
        for j in range(len(halls_dict[hall_name][i])):
            if halls_dict[hall_name][i][j] == "S":
                sum_stu += 1
            elif halls_dict[hall_name][i][j] == "F":
                sum_full += 1

    print(
        "Sum of students = " + str(sum_stu * 5) + ", Sum of full fares = " + str(sum_full * 10) + ", Overall = " + str(
            sum_stu * 5 + sum_full * 10))


def letterToNumerics(text):
    LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=0)}

    text = text.lower()

    numbers = [LETTERS[character] for character in text if character in LETTERS]

    return ' '.join(numbers)
