import os
import time
import random
import tickets
import json
import subprocess

game_over = False
score = 0
money = 0
day = 1

HOURS_PER_DAY = 8

ticket_queue = []

def get_next_ticket():
    global ticket_queue
    if not ticket_queue:
        ticket_queue = list(tickets.Tickets)
        random.shuffle(ticket_queue)
    return ticket_queue.pop()

def save_game(name, score, money, day):
    save_data = {
        "name": name,
        "score": score,
        "money": money,
        "day": day
    }
    with open("savegame.json", "w") as file:
        json.dump(save_data, file, indent=4)

def load_game():
    try:
        with open("savegame.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return None

def clear_terminal():
    try:
        subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
    except Exception:
        print("\n" * 40)

save_data = load_game()

if save_data:
    name = save_data["name"]
    score = save_data["score"]
    money = save_data["money"]
    day = save_data.get("day", 1)

    print("Welcome back to PyDesk,", name, "you have completed", score, "tickets and earned £", money, "and you got to", day, "days")
    time.sleep(2)
else:
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
    shift_time = HOURS_PER_DAY
    day_tickets = 0
    day_score = 0
    day_money = 0

    while shift_time > 0:
        clear_terminal()
        ticket = get_next_ticket()
        print("---------------------------------------------------")
        print("Day", day)
        print("You have ", shift_time, "hours left in your shift")
        print("---------------------------------------------------")
        print("ID", ticket["id"])
        print("User", ticket["user"])
        print("Issue:", ticket["issue"])
        print("Priority:", ticket["priority"])
        print()
        print("Option 1:", ticket["option_1"])
        print("Option 2:", ticket["option_2"])
        print()
        choice = ""
        while choice != "1" and choice != "2":
            choice = input("Option 1 or 2? ")
            if choice != "1" and choice != "2":
                print("Invalid input, try again")

        correct = False
        if choice == "1":
            correct = ticket["correct_option"] == "option_1"
        elif choice == "2":
            correct = ticket["correct_option"] == "option_2"

        if correct:
            print(ticket["success_message"])
            score = score + 1
            money = money + 10
            day_score = day_score + 1
            day_money = day_money + 10
        else:
            print(ticket["fail_message"])
            money = money - 5
            day_money = day_money - 5

        day_tickets = day_tickets + 1
        shift_time = shift_time - ticket["time_taken"]

        print()
        print()
        print("---------------------------------------------------")
        print("You took", ticket["time_taken"], "hours to complete this ticket")
        print("You have earned £", money, "so far by completing", score, "tickets")
        save_game(name, score, money, day)
        print("---------------------------------------------------")
        print("Game Saved")
        time.sleep(5)

    clear_terminal()
    print("=====================================================")
    print("End of Day", day)
    print("=====================================================")
    print("Tickets completed today:", day_tickets)
    print("Tickets solved correctly today:", day_score)
    print("Money earned/lost today: £", day_money)
    print("-----------------------------------------------------")
    print("Total tickets completed:", score)
    print("Total money: £", money)
    print("=====================================================")
    save_game(name, score, money, day)
    print("Game Saved")
    time.sleep(4)

    choice = ""
    while choice != "1" and choice != "2":
        choice = input("Continue to Day " + str(day + 1) + " (1) or End shift here (2)? ")
        if choice != "1" and choice != "2":
            print("Invalid input, try again")

    if choice == "1":
        day = day + 1
        save_game(name, score, money, day)
    else:
        print("---------------------------------------------------")
        print("You finished on Day", day, "having completed", score, "tickets and earned £", money)
        print("----------------------------------------------------")
        time.sleep(5)
        print("Thanks for playing, hope to see you again soon!")
        time.sleep(2)
        game_over = True