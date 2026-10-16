# Room Expense Calculator

A small beginner Python project that calculates how much each person should contribute toward shared room expenses.

## What it includes

The program asks for:

- Total rent
- Total food order cost
- Electricity bill
- Water bill
- Number of people sharing the room

It adds the four expenses and divides the total by the number of people.

## Requirements

- Python 3

## How to run

1. Save the program as `room_expenses.py`.
2. Open a terminal in the folder containing the file.
3. Run:

   ```bash
   python room_expenses.py
   ```

   On some systems, use `python3 room_expenses.py` instead.

4. Enter each amount when prompted. Enter a positive number for the number of people.

## Example

```text
Enter the total rent amount: 12000
Enter the total food order amount: 3000
Enter the electricity bill amount: 1200
Enter the water bill amount: 300
Enter the total number of people sharing the room: 3
The total amount each person has to pay is : 5500
```

The example total is 16,500, split among 3 people, so each person pays 5,500.

## Calculation

```text
(amount of rent + food + electricity + water) // number of people
```

The `//` operator performs integer division, so any remainder is discarded. For example, if the total does not divide evenly, this version reports the whole-number amount and does not show the leftover fraction.

## Note

The number of people must not be zero, because division by zero is not possible.


# Rock, Paper, Scissors

A beginner Python project that lets you play Rock, Paper, Scissors against a computer. The computer randomly chooses a move, and the program compares it with your choice to decide who wins.

## What you’ll practise

- Getting input with `input()`
- Choosing a random item with Python’s `random` module
- Using `if` and `elif` to compare choices

## Requirements

- Python 3

## How to run

1. Save the program in a file named `rock_paper_scissors.py`.
2. Open a terminal in the folder where you saved it.
3. Run:

   ```bash
   python rock_paper_scissors.py
   ```

   If your computer uses `python3`, run `python3 rock_paper_scissors.py` instead.

4. Type Rock, Paper, or Scissor when prompted.

## Rules

- Rock beats Scissors.
- Paper beats Rock.
- Scissors beats Paper.
- Matching choices make a draw.

## Important: make the choice names consistent

The current code uses different spellings and capitalization in different places. For example, the random choice list contains `"Scissor"`, while one condition checks for `"Scissors"`; it also checks for lowercase `"paper"` and `"scissors"`, even though the prompt and list use capitalized names. Because Python treats these as different strings, some results may be wrong.

Use the same spelling and capitalization everywhere. For example, choose either `"Scissors"` or `"Scissor"` and use it consistently, and make the user input match the same format before comparing it. You can also use `.strip().title()` to accept entries such as `rock`, ` ROCK `, or `Rock` in a consistent form (then make sure your list and conditions use that same form).

## Example

```text
Enter your choice (Rock, Paper, Scissor): Rock
user choice is : Rock
computer choice is : Paper
You Lose!
```

Have fun, and try adding input validation so the program asks again when someone enters something other than a valid move.
