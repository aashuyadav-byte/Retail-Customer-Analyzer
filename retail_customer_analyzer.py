"""
RETAIL CUSTOMER ANALYZER
Class Project - Python 3 + Pandas

How to run:
1. Install Pandas:  pip install pandas
2. Save this file as: retail_customer_analyzer.py
3. Run:              python retail_customer_analyzer.py

If customers.csv is not present, this program creates it with the
8 sample records from the project description.
"""

import os
import pandas as pd

FILE_NAME = "customers.csv"

SAMPLE_DATA = {
    "CustomerID": ["C01", "C02", "C03", "C04", "C05", "C06", "C07", "C08"],
    "Name": [
        "Asha", "Bhavin", "Chitra", "Deepak",
        "Esha", "Farhan", "Gita", "Harit"
    ],
    "City": [
        "Raipur", "Durg", "Raipur", "Bhilai",
        "Durg", "Raipur", "Bhilai", "Durg"
    ],
    "Purchases": [5, 2, 8, 1, 4, 3, 6, 2],
    "TotalSpent": [12000, 3000, 25000, 800, 9000, 6000, 15000, 2200]
}


def create_sample_file():
    """Create customers.csv when it does not exist."""
    sample_df = pd.DataFrame(SAMPLE_DATA)
    sample_df.to_csv(FILE_NAME, index=False)
    print(f"\n'{FILE_NAME}' was not found.")
    print(f"A sample '{FILE_NAME}' file has been created.\n")


def load_customers():
    """Load and validate customer data from CSV."""
    if not os.path.exists(FILE_NAME):
        create_sample_file()

    try:
        df = pd.read_csv(FILE_NAME)
    except pd.errors.EmptyDataError:
        print("Error: customers.csv is empty.")
        return None
    except (OSError, pd.errors.ParserError) as error:
        print(f"Error while reading customers.csv: {error}")
        return None

    required_columns = [
        "CustomerID", "Name", "City", "Purchases", "TotalSpent"
    ]

    missing_columns = [
        column for column in required_columns if column not in df.columns
    ]

    if missing_columns:
        print("Error: Missing column(s):", ", ".join(missing_columns))
        return None

    if df.empty:
        print("Error: No customer records found in customers.csv.")
        return None

    # Convert numeric columns safely. Invalid values become NaN.
    df["Purchases"] = pd.to_numeric(df["Purchases"], errors="coerce")
    df["TotalSpent"] = pd.to_numeric(df["TotalSpent"], errors="coerce")

    invalid_rows = df[
        df[["Purchases", "TotalSpent"]].isna().any(axis=1)
    ]

    if not invalid_rows.empty:
        print("Warning: Rows with invalid numeric data will be ignored.")
        df = df.dropna(subset=["Purchases", "TotalSpent"])

    if df.empty:
        print("Error: No valid customer records available.")
        return None

    return df


def show_statistics(df):
    """Display mean, median, highest and lowest spending."""
    mean_spend = df["TotalSpent"].mean()
    median_spend = df["TotalSpent"].median()

    highest = df.loc[df["TotalSpent"].idxmax()]
    lowest = df.loc[df["TotalSpent"].idxmin()]

    print("\n========== CUSTOMER SPENDING STATISTICS ==========")
    print(f"Mean spend:   Rs. {mean_spend:.2f}")
    print(f"Median spend: Rs. {median_spend:.2f}")
    print(
        f"Highest: {highest['Name']} "
        f"(Rs. {highest['TotalSpent']:.2f})"
    )
    print(
        f"Lowest:  {lowest['Name']} "
        f"(Rs. {lowest['TotalSpent']:.2f})"
    )
    print("==================================================")


def show_high_value_customers(df):
    """Show customers whose spending is at least the entered limit."""
    user_input = input("\nEnter minimum spending limit (Rs.): ").strip()

    try:
        limit = float(user_input)
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    if limit < 0:
        print("Amount must be 0 or more.")
        return

    high_value = df[df["TotalSpent"] >= limit]

    print(f"\nHigh-value customers (TotalSpent >= {limit:g}): "
          f"{len(high_value)}")

    if high_value.empty:
        print("No customers found at or above this limit.")
        return

    print(
        high_value[
            ["CustomerID", "Name", "City", "TotalSpent"]
        ].to_string(index=False)
    )


def show_city_summary(df):
    """Display city-wise total and average spending."""
    city_summary = (
        df.groupby("City")["TotalSpent"]
        .agg(Total="sum", Average="mean")
        .reset_index()
    )

    print("\n========== CITY-WISE SUMMARY ==========")
    for _, row in city_summary.iterrows():
        print(
            f"{row['City']}: Total Rs. {row['Total']:.2f} | "
            f"Average Rs. {row['Average']:.2f}"
        )
    print("=======================================")


def main():
    print("======================================")
    print("       RETAIL CUSTOMER ANALYZER")
    print("======================================")

    df = load_customers()

    if df is None:
        return

    print(f"\nSuccessfully loaded {len(df)} customer record(s).")

    while True:
        print("\n--------------- MAIN MENU ---------------")
        print("1. Spending statistics")
        print("2. High-value customers")
        print("3. City-wise summary")
        print("4. Exit")
        print("-----------------------------------------")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            show_statistics(df)
        elif choice == "2":
            show_high_value_customers(df)
        elif choice == "3":
            show_city_summary(df)
        elif choice == "4":
            print("\nThank you for using Retail Customer Analyzer!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
