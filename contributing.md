# Contributing

## How to help
1. Fork the repo 
2. Clone your fork locally
3. Create a branch for your contributions (e.g. `add-more-tickets` )
4. Edit the code
5. Test your changes thoroughly
6. Commit your changes with a clear message on what you have done
7. Push to github
8. Open a Pull Request (Ensure the game runs in the terminal without crashing, changes are unique and worthwhile and no unnecesary files are in the PR.)
9. Wait for me to merge it, if it has been a day or 2 and I haven't seen it then email me on `wgdev.uk@gmail.com`, I'll get back to you when I can.

## What can you add
*More tickets, the game needs more to make it better so feel free to add as many as you want to just make sure it follows the format below.
*New features/improvements, if you feel the game could have more features then feel free to add it.
*Any other fixes or typos you can find that you think the game could use

## Adding tickets

All tickets in the game are inside `tickets.py` please add them in here and make sure all tickets follow the format below:

{"id": "unique 4 digit number (Higher than the last ID)",
"user": "Name; Department",
"priority": "Low,Medium,High,Critical", 
"issue": "Problem, error message: 'error",
"option_1": "First choice",
"option_2": "Second choice",
"correct_option": "correct option (e.g. option_1)",
"success_message": "Go in more depth about what the option does",
"fail_message": "Say why it failed",
"time_taken": 1 (just an estimate)
},

**Make sure it is indented and under any previous tickets.**

Try to balance it so it is not always option 1 or 2 etc and vary priority/time etc

If you look at previous tickets in the file it might be easier to understand

## What you get

If you contribute your name will go onto the [itch.io](https://gooderswills.itch.io/pydesk) page and onto the github readme