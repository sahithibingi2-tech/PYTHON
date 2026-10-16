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
