import random

lst = []
slots = int(input("Enter number of slots : "))
while slots < 2:
    print("minimum number of slots is 2")
    slots = int(input("Enter number of slots : "))

for i in range(0, slots):
    print("Option", i, ": ")
    option = input()
    while option == "":
        print("Your option is invalid")
        option = input()
    lst.append(option)  # add the option to the list

print("list:", lst)
agreed = input("Is this the list you want : ")
agreed_upper = agreed.upper()

if agreed_upper == "YES" or agreed_upper == "YUP":
    picked_choice = random.choice(lst)  # picking a random element from the list

else:
    number = int(input("How many words are wrong : "))
    for i in range(number):
        old = input("Which word is wrong : ")
        # corrected = input("Write your new option : ")
        lst.remove(old)
        new = input("Write the new option : ")
        lst.append(new)
    print("Modified list : ", lst)
    picked_choice = random.choice(lst)

print(picked_choice)
