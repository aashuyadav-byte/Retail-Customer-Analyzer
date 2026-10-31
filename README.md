# Retail Customer Analyzer

**Project Number:** PS No. 87  
**Project Title:** Retail Customer Analyzer  
**Language:** Python 3  
**Library:** Pandas

## 1. Project Description

Retail Customer Analyzer is a menu-driven Python application that reads customer purchase information from a CSV file and analyzes customer spending.

It displays overall spending statistics, identifies the highest- and lowest-spending customers, filters high-value customers using a spending limit entered by the user, and shows city-wise spending summaries.

## 2. Features

- Reads customer records from `customers.csv` using Pandas.
- Calculates mean and median spending.
- Finds the customers with the highest and lowest total spending.
- Filters customers whose `TotalSpent` is greater than or equal to a user-entered limit.
- Calculates city-wise total and average spending.
- Handles invalid menu choices and invalid spending limits.
- Creates a sample `customers.csv` automatically if the file is missing.

## 3. Requirements

- Python 3
- Pandas library

Install Pandas using:

```bash
pip install pandas
```

## 4. Project Files

Keep these files in the same folder:

```text
Retail-Customer-Analyzer/
├── retail_customer_analyzer.py
├── customers.csv
└── README.md
```

The program creates `customers.csv` automatically if it does not already exist. You can also create or edit the CSV file yourself.

## 5. CSV File Format

The CSV file must contain these column names:

```csv
CustomerID,Name,City,Purchases,TotalSpent
C01,Asha,Raipur,5,12000
C02,Bhavin,Durg,2,3000
C03,Chitra,Raipur,8,25000
C04,Deepak,Bhilai,1,800
C05,Esha,Durg,4,9000
C06,Farhan,Raipur,3,6000
C07,Gita,Bhilai,6,15000
C08,Harit,Durg,2,2200
```

- `CustomerID`: Unique customer identifier.
- `Name`: Customer name.
- `City`: Customer's city.
- `Purchases`: Number of purchases.
- `TotalSpent`: Total amount spent by the customer, in rupees.

## 6. How to Run

1. Save `retail_customer_analyzer.py` in a folder.
2. Open a terminal or command prompt in that folder.
3. Install Pandas if it is not already installed:

   ```bash
   pip install pandas
   ```

4. Run the program:

   ```bash
   python retail_customer_analyzer.py
   ```

5. Select an option from the menu.

## 7. Main Menu

```text
1. Spending statistics
2. High-value customers
3. City-wise summary
4. Exit
```

### Menu Options

- **Option 1 – Spending statistics:** Displays mean, median, highest spending, and lowest spending.
- **Option 2 – High-value customers:** Asks for a minimum spending limit and lists customers whose total spending is at least that amount.
- **Option 3 – City-wise summary:** Displays total and average spending for each city.
- **Option 4 – Exit:** Closes the program.

## 8. Input Validation

- If the spending limit is not a number, the program displays: `Invalid amount. Please enter a number.`
- If the spending limit is negative, the program displays: `Amount must be 0 or more.`
- If the menu choice is invalid, the program asks the user to select 1, 2, 3, or 4.
- The program checks that the required CSV columns are present and handles invalid numeric data.

## 9. Testing

| Test case | Input | Expected behavior |
|---|---|---|
| Normal statistics | Menu option 1 | Displays mean, median, highest and lowest spending |
| High-value customers | Option 2, limit 25000 | Displays Chitra from the sample data |
| Invalid amount | Option 2, limit `abc` | Displays an invalid amount message |
| Negative amount | Option 2, limit `-500` | Displays an amount validation message |
| City summary | Menu option 3 | Displays total and average spending for each city |
| Invalid menu | Enter `9` | Displays an invalid choice message |

## 10. Concepts Used

- Python functions
- Conditional statements
- Loops
- Exception handling
- CSV file handling
- Pandas DataFrames
- Filtering and grouping
- Mean, median, minimum and maximum

## 11. Conclusion

The Retail Customer Analyzer demonstrates how Python and Pandas can be used to read, organize, filter, and analyze customer purchase data. It provides useful spending statistics and city-wise summaries through a simple menu-driven interface.
