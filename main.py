
import sys

from Commands import createHall, sellTicket, cancelTicket, showhall, balance

# run with pyhton main.py input.txt

input_file = open(sys.argv[1], "r")

halls_list = []
halls_dict = {}
customer_list = []

for line in input_file:
    line_split = line.split(" ")
    # print(line_split)
    if line_split[0] == "CREATEHALL":
        if len(line_split) > 3:
            print("Error: Too much parameters for creating a hall!")
        elif len(line_split) < 3:
            print("Error: Not enough parameters for creating a hall!")
        else:
            createHall(line_split, halls_list, halls_dict)

        # print(halls_dict)
    elif line_split[0] == "SELLTICKET":
        sellTicket(line_split, halls_list, halls_dict, customer_list)
    elif line_split[0] == "CANCELTICKET":
        cancelTicket(line_split, halls_list, halls_dict, customer_list)
    elif line_split[0] == "SHOWHALL":
        showhall(line_split[1].rstrip("\n"), halls_dict)
        print()
    elif line_split[0] == "BALANCE":
        balance(line_split[1].rstrip("\n"), halls_dict)
    else:
        print("unknown commands")




input_file.close()
