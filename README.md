# Family Restaurant Billing System

A command-line interface (CLI) Python application for managing a restaurant menu, accepting customer orders, calculating tiered discounts, applying 5% GST, and generating a final bill.

## Project Overview

The application demonstrates fundamental Python programming concepts including lists, loops, conditional statements, user input, validation, arithmetic calculations, and formatted console output.

## Prerequisites

- Python 3.x
- A terminal or command prompt

Check your Python installation with:

```bash
python --version
```

## Setup

1. Clone the repository:

```bash
git clone https://github.com/sumit26bce10082-sudo/Restaurant_Billing_System.git
```

2. Navigate into the project directory:

```bash
cd Restaurant_Billing_System
```

3. No third-party packages are required. The project uses only Python's standard functionality.

## Run the Project

Execute the application from the terminal:

```bash
python My_project.py
```

If your system uses `python3` as the Python command, run:

```bash
python3 My_project.py
```

## How to Use

1. Enter the customer's name.
2. Review the displayed restaurant menu and item numbers.
3. Enter an item number to add it to the order.
4. Enter the quantity for the selected item.
5. Continue adding items as required.
6. Enter `0` when the order is complete.
7. The program displays the final bill with subtotal, discount, GST, and total payable amount.

## Menu

| Item No. | Food | Price (Rs.) |
|---:|---|---:|
| 101 | Paneer Butter Masala | 220 |
| 102 | Dal Tadka | 150 |
| 103 | Butter Naan | 40 |
| 104 | Jeera Rice | 120 |
| 105 | Veg Biryani | 180 |

## Discount Rules

- Subtotal Rs. 2000 or more: 15% discount
- Subtotal Rs. 1000 to Rs. 1999: 10% discount
- Subtotal Rs. 500 to Rs. 999: 5% discount
- Subtotal below Rs. 500: no discount

After the discount, 5% GST is calculated on the discounted amount.

## Project Structure

```text
Restaurant_Billing_System/
├── My_project.py
└── README.md
```

## Example Calculation

For an order with a subtotal of Rs. 2000:

- Discount = Rs. 300 (15%)
- Amount after discount = Rs. 1700
- GST = Rs. 85 (5%)
- Total payable = Rs. 1785

## Validation

The program checks item-number input and quantity input before adding an order. Invalid menu numbers, non-positive and invalid characters quantities are rejected with a message so the user can enter the value again.