import tickets

def print_ticket_stats():
    total_tickets = len(tickets.Tickets)

    departments = {}
    priorities = {}
    total_time = 0.0

    # Which ticket IDs have option 1 / option 2 as the correct answer
    answers = {"option_1": [], "option_2": []}
    invalid_answers = []

    for t in tickets.Tickets:
        user_info = t.get("user", "")
        if ";" in user_info:
            department = user_info.split(";")[1].strip()
        else:
            department = "Unknown"

        departments[department] = departments.get(department, 0) + 1

        prio = t.get("priority", "Unknown")
        priorities[prio] = priorities.get(prio, 0) + 1

        total_time += t.get("time_taken", 0)

        correct = t.get("correct_option")
        if correct in answers:
            answers[correct].append(t.get("id", "?"))
        else:
            invalid_answers.append(t.get("id", "?"))

    option_1_count = len(answers["option_1"])
    option_2_count = len(answers["option_2"])

    def percent(count):
        return round(count / total_tickets * 100, 1) if total_tickets else 0

    print("=========================================")
    print("           TICKET STATISTICS             ")
    print("=========================================")
    print(f"Total Tickets:            {total_tickets}")
    print(f"Total Hours Required:     {total_time} hrs")
    print(f"Average Time Per Ticket:  {round(total_time / total_tickets, 2) if total_tickets else 0} hrs")
    print("-----------------------------------------")
    print("Tickets by Department:")
    for dept, count in sorted(departments.items()):
        print(f"  - {dept}: {count}")
    print("-----------------------------------------")
    print("Tickets by Priority:")
    for prio, count in priorities.items():
        print(f"  - {prio}: {count}")
    print("-----------------------------------------")
    print("Correct Answer Balance:")
    print(f"  - Option 1 is correct: {option_1_count} ({percent(option_1_count)}%)")
    print(f"  - Option 2 is correct: {option_2_count} ({percent(option_2_count)}%)")

    swaps_needed = abs(option_1_count - option_2_count) // 2
    if swaps_needed > 0:
        heavier = "Option 1" if option_1_count > option_2_count else "Option 2"
        lighter = "Option 2" if heavier == "Option 1" else "Option 1"
        print(f"  Swap the options on {swaps_needed} {heavier} ticket(s) to make {lighter} correct")
    else:
        print("  Answers are balanced")

    print(f"  Option 1 IDs: {', '.join(answers['option_1'])}")
    print(f"  Option 2 IDs: {', '.join(answers['option_2'])}")

    if invalid_answers:
        print(f"  WARNING - invalid correct_option on IDs: {', '.join(invalid_answers)}")
    print("=========================================")

if __name__ == "__main__":
    print_ticket_stats()