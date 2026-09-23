import tickets

def print_ticket_stats():
    total_tickets = len(tickets.Tickets)
    
    departments = {}
    priorities = {}
    total_time = 0.0

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
    print("=========================================")

if __name__ == "__main__":
    print_ticket_stats()