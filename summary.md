# Retail Customer Analyzer -- Development Summary

> This file is intended to complement `README.md`, not repeat it. The
> README contains the project description, features, requirements, CSV
> format, installation and run instructions, menu options, validation
> rules, tests, concepts, and conclusion. This summary focuses on the
> program's execution flow and development challenges.

## 1. Execution Flow: What Happens When the Program Runs

### Step 1 -- Python starts the file

Python executes the import statements: - `os` is used to check whether
the CSV file exists. - `pandas` is used to work with customer data.

The constant `FILE_NAME` stores the name `customers.csv`, and
`SAMPLE_DATA` contains the sample records that can be written to the
file.

### Step 2 -- The main function is called

At the bottom of the file, this condition checks whether the file is
being run directly:

``` python
if __name__ == "__main__":
    main()
```

If it is, Python calls `main()`.

### Step 3 -- Customer data is loaded

`main()` calls `load_customers()`.

-   `os.path.exists(FILE_NAME)` checks whether `customers.csv` exists.
-   If the file is missing, `create_sample_file()` builds a Pandas
    DataFrame from `SAMPLE_DATA` and saves it as a CSV file.
-   `pd.read_csv(FILE_NAME)` reads the file into a DataFrame.

### Step 4 -- The data is checked and cleaned

Before analysis, `load_customers()`: 1. Handles an empty file or
file-reading error. 2. Checks that all required columns are present. 3.
Checks that the DataFrame contains records. 4. Converts `Purchases` and
`TotalSpent` into numeric values. 5. Removes rows where either of those
numeric values is invalid.

If no usable records remain, the function returns `None` and the program
stops. Otherwise, it returns the cleaned DataFrame to `main()`.

### Step 5 -- The menu loop begins

`main()` displays the menu inside a `while True` loop and asks the user
to enter a choice. The same cleaned DataFrame is passed to the selected
analysis function.

### Step 6 -- The selected analysis runs

-   **Choice 1:** `show_statistics(df)` calculates the mean and median.
    It uses `idxmax()` and `idxmin()` to locate the records with the
    highest and lowest spending.
-   **Choice 2:** `show_high_value_customers(df)` reads a spending
    limit, checks the input, and filters rows using
    `df["TotalSpent"] >= limit`.
-   **Choice 3:** `show_city_summary(df)` groups records by `City` and
    calculates the sum and average of `TotalSpent`.
-   **Choice 4:** The program prints a closing message and uses `break`
    to leave the loop.

### Step 7 -- The program repeats or ends

After choices 1, 2, or 3, control returns to the menu. An invalid choice
displays a message and the menu appears again. The program ends when the
user selects choice 4, or earlier if valid customer data cannot be
loaded.

## 2. Execution Flow Diagram

``` text
Run Python file
      |
      v
Call main()
      |
      v
Call load_customers()
      |
      v
Check customers.csv
   /       \
Missing    Exists
  |          |
Create CSV   |
   \        /
      v
Read CSV into DataFrame
      |
      v
Validate and clean data
      |
      v
Is usable data available?
   /       \
  No       Yes
  |          |
Stop     Display menu
             |
             v
       Read user choice
             |
     +-------+-------+-------+
     |       |       |       |
     1       2       3       4
     |       |       |       |
 Statistics Filter  City    Exit
             |     summary
     +-------+-------+
             |
       Show menu again
```

## 3. Development Difficulties and How They Were Addressed

The following challenges are based on the code structure. They are good
points to discuss in a presentation, but describe them as personal
experiences only if you actually faced them.

### Challenge 1 -- Understanding how Pandas stores data

**Why it can be difficult:** A CSV file is plain tabular data, while the
program analyses it through a Pandas DataFrame.

**How the code addresses it:** `pd.read_csv()` loads the CSV into a
DataFrame, which can then be filtered, grouped, and analysed.

### Challenge 2 -- Making the program work when the CSV is missing

**Why it can be difficult:** Reading a file that does not exist would
cause a file error.

**How the code addresses it:** The program checks with
`os.path.exists()` and creates sample data through
`create_sample_file()` when needed.

### Challenge 3 -- Handling damaged or incomplete input data

**Why it can be difficult:** The CSV may be empty, may not contain the
required headings, or may contain text where a number is expected.

**How the code addresses it:** The program checks file-reading errors,
required columns, empty records, and numeric values before continuing.

### Challenge 4 -- Avoiding calculation errors

**Why it can be difficult:** Statistical calculations require usable
numeric values.

**How the code addresses it:** `pd.to_numeric(..., errors="coerce")`
converts invalid numeric entries to missing values, and `dropna()`
removes rows that cannot be used for these calculations.

### Challenge 5 -- Validating the spending limit entered by the user

**Why it can be difficult:** The user might type letters or a negative
amount instead of a valid limit.

**How the code addresses it:** `try/except` handles values that cannot
be converted to a number, and an `if` statement rejects negative limits.

### Challenge 6 -- Writing the analysis operations

**Why it can be difficult:** Each operation needs a different way to
select or summarize records.

**How the code addresses it:** The project uses Pandas methods such as
`mean()`, `median()`, `idxmax()`, `idxmin()`, Boolean filtering,
`groupby()`, and `agg()`.

### Challenge 7 -- Controlling the menu

**Why it can be difficult:** The program should keep accepting choices
without restarting, but it must also provide a way to exit.

**How the code addresses it:** A `while True` loop repeats the menu,
`if/elif/else` selects an operation, and `break` exits the loop.

## 4. Short First-Person Presentation Answer

You can adapt this answer for your viva if it matches your actual
experience:

"During the development of my Retail Customer Analyzer project, some
challenging parts were understanding Pandas DataFrames, reading CSV
files, validating customer data, and handling incorrect user input. I
addressed these problems by using Pandas functions, file checks,
conditional statements, and exception handling. I also had to understand
how to calculate customer statistics, filter high-value customers, group
spending by city, and repeat the menu until the user chooses Exit."

## 5. What This Project Helped Me Practise

-   Following the execution of a Python program from its entry point.
-   Dividing a program into functions with separate responsibilities.
-   Passing a DataFrame from one function to another.
-   Checking and cleaning data before analysing it.
-   Using loops and conditions to control a menu.
-   Using Pandas operations for statistics, filtering, and grouping.
-   Handling expected file and input errors.
