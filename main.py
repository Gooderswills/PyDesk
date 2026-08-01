import time
import random
import tickets

game_over = False
last_ticket = None
score = 0
money = 0
shift_time = 8

ticket_queue = []

def get_next_ticket():
    global ticket_queue
    if not ticket_queue:
        ticket_queue = list(tickets.Tickets)
        random.shuffle(ticket_queue)
    return ticket_queue.pop()

print("Hello and welcome to PyDesk, this is a text based game where you are an IT support employee, work through tickets and try and keep the company running!")
time.sleep(2)
name = input("Hi there you must be new, what is your name? ")
time.sleep(1)
print("Nice to meet you", name , "I am Will, your manager and I will help you get started on your first day")
time.sleep(2)

print("Let's not waste any time, you've already got tickets coming through!")
time.sleep(2)
print()

while game_over == False and shift_time > 0:
    ticket = get_next_ticket()
    print("---------------------------------------------------")
    print("You have ", shift_time, "hours left in your shift")
    print("---------------------------------------------------")
    print("You have a new ticket from", ticket["user"])
    print("Issue:", ticket["issue"])
    print("Priority:", ticket["priority"])
    print("Option 1:", ticket["option_1"])
    print("Option 2:", ticket["option_2"])
    choice = ""
    while choice != "1" and choice != "2":
        choice = input("Option 1 or 2?")
        if choice != "1" and choice != "2":
            print("Invalid input, try again")
    if choice == "1":
        if ticket["correct_option"] == "option_1":
            print(ticket["success_message"])
            score = score + 1
            money = money + 10
        elif ticket["correct_option"] == "option_2":
            print(ticket["fail_message"])
            money = money - 5
    elif choice == "2":
        if ticket["correct_option"] == "option_2":
            print(ticket["success_message"])
            score = score + 1
            money = money + 10
        elif ticket["correct_option"] == "option_1":
            print(ticket["fail_message"])
            money = money - 5
    else:
        print("Error, invalid input")

    shift_time = shift_time - ticket["time_taken"]
    action = ""
    print("---------------------------------------------------")
    print("You took", ticket["time_taken"], "hours to complete this ticket")
    print("You have earned £", money, "so far by completing", score, "tickets")
    load_time = random.randint(1,5)
    time.sleep(load_time)

    if shift_time <= 0:
        print("---------------------------------------------------")
        print("Shift over, you completed", score, "tickets and earned £", money,)
        print("----------------------------------------------------")
        game_over = True