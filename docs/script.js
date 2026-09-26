const output = document.getElementById("output");
const input = document.getElementById("terminal-input");
const inputLine = document.getElementById("input-line");
const terminal = document.getElementById("terminal");
 
const ticketText =
`---------------------------------------------------
You have new ticket from Michael, Finance
Issue: Unable to access company bank account, error message: 'Cannot connect to bank'
Priority: High
---------------------------------------------------
Option 1: Check if finance switch is down, restart if needed
Option 2: Remote into user's computer, update their OS and BIOS
 
Option 1 or 2? `;
 
const correctOption = "1";
const successMessage = "Correct! The finance switch had gone down - a quick restart got the connection back online.\n\nYou completed the ticket.";
const failMessage = "That didn't fix it. Remoting in and updating the OS/BIOS had nothing to do with the network issue - the switch was still down.\n\nTicket failed.";
 
let answered = false;
 
function print(text, className) {
    const span = document.createElement("span");
    if (className) span.className = className;
    span.textContent = text;
    output.appendChild(span);
}
 
function startTicket() {
    print(ticketText, "prompt");
}
 
function handleAnswer(choice) {
    print(choice + "\n\n");
    if (choice === "1" || choice === "2") {
        answered = true;
        if (choice === correctOption) {
            print(successMessage + "\n", "success");
        } else {
            print(failMessage + "\n", "fail");
        }
        print("\n(refresh the page to try again)", "prompt");
        inputLine.classList.add("hidden");
    } else {
        print("Invalid input, try again\n\n");
        print("Option 1 or 2? ", "prompt");
    }
}
 
input.addEventListener("keydown", (e) => {
    if (answered) return;
    if (e.key === "Enter") {
        const val = input.value.trim();
        if (val.length > 0) {
            handleAnswer(val);
            input.value = "";
        }
    }
});
 
terminal.addEventListener("click", () => {
    if (!answered) input.focus();
});
 
startTicket();
input.focus();