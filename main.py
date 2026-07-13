import time
import random
import tickets

game_over = False
last_ticket = None
score = 0
money = 0


print("Hello and welcome to PyDesk, this is a text based game where you are an IT support employee, work through tickets and try and keep the company running!")
time.sleep(2)
name = input("Hi there you must be new, what is your name? ")
time.sleep(1)
print("Nice to meet you", name , "I am Will, your manager and I will help you get started on your first day")
time.sleep(2)

print("Let's not waste any time, you've already got tickets coming through!")
time.sleep(2)
print()

while game_over == False:
    ticket = random.choice(tickets.Tickets)
    if len(tickets.Tickets) > 1:
        while ticket == last_ticket:
            ticket = random.choice(tickets.Tickets)
    last_ticket = ticket
    print("---------------------------------------------------")
    print("You have a new ticket from", ticket["user"])
    print("Issue:", ticket["issue"])
    print("Priority:", ticket["priority"])
    print()
    print("Option 1:", ticket["option_1"])
    print("Option 2:", ticket["option_2"])
    print()
    choice = input("Option 1 or 2?")
    if choice == "1":
        if ticket["correct_option"] == "option_1":
            print(ticket["success_message"])
            score = score + 1
            money = money + 10
        elif ticket["correct_option"] == "option_2":
            print(ticket["fail_message"])
    elif choice == "2":
        if ticket["correct_option"] == "option_2":
            print(ticket["success_message"])
            score = score + 1
            money = money + 10
        elif ticket["correct_option"] == "option_1":
            print(ticket["fail_message"])
    else:
        print("Error, invalid input")

    action = input("Continue or End shift?(C/E)").upper()

    if action == "E":
        print("Shift over, you completed", score, "tickets and earned £", money,)
        game_over = True