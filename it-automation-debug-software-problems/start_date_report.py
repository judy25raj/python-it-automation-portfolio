#!/usr/bin/env python3
"""start_date_report.py

Google Project 7 – Debug and Solve Software Problems

Portfolio version of the Google IT Automation with Python lab:
- Reads a CSV file with employees and their start dates
- Asks the user for a minimum start date
- Prints all employees who started on or after that date

The script demonstrates:
- Fixing a type error caused by `input()` returning strings
- Improving performance by pre-processing the CSV once and reusing results
"""

import csv
import datetime
from collections import defaultdict
from typing import Dict, List, Tuple


EMPLOYEES_CSV_PATH = "employees-with-date.csv"


def get_start_date() -> datetime.datetime:
    """Interactively get the start date to query for."""
    print()
    print("Getting the first start date to query for.")
    print()
    print("The date must be greater than Jan 1st, 2018")

    # Bugfix: cast input() strings to integers
    year = int(input("Enter a value for the year: "))
    month = int(input("Enter a value for the month: "))
    day = int(input("Enter a value for the day: "))
    print()

    return datetime.datetime(year, month, day)


def load_employee_data(csv_path: str) -> List[Tuple[datetime.date, str]]:
    """Load employee data from CSV.

    Expects a CSV with headers:
      - name
      - start_date (YYYY-MM-DD)
    """
    rows: List[Tuple[datetime.date, str]] = []
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row.get("name", "").strip()
            date_str = row.get("start_date", "").strip()
            if not name or not date_str:
                continue
            try:
                y, m, d = map(int, date_str.split("-"))
                start_date = datetime.date(y, m, d)
            except ValueError:
                continue
            rows.append((start_date, name))
    return rows


def build_index(
    rows: List[Tuple[datetime.date, str]]
) -> Tuple[Dict[datetime.date, List[str]], List[datetime.date]]:
    """Build an index for fast lookup of employees by start date."""
    index: Dict[datetime.date, List[str]] = defaultdict(list)
    for start_date, name in rows:
        index[start_date].append(name)
    sorted_dates = sorted(index.keys())
    return index, sorted_dates


def get_same_or_newer(
    query_date: datetime.date,
    index: Dict[datetime.date, List[str]],
    sorted_dates: List[datetime.date],
) -> List[Tuple[datetime.date, List[str]]]:
    """Return all (date, [employees]) for dates >= query_date."""
    result: List[Tuple[datetime.date, List[str]]] = []
    for d in sorted_dates:
        if d >= query_date:
            result.append((d, index[d]))
    return result


def print_report(entries: List[Tuple[datetime.date, List[str]]]) -> None:
    """Print the report in a friendly format."""
    if not entries:
        print("No employees found for the selected start date or later.")
        return

    for date_obj, names in entries:
        formatted_date = date_obj.strftime("%b %d, %Y")
        print(f"Started on {formatted_date}: {names}")


def main():
    start_dt = get_start_date()
    query_date = start_dt.date()

    rows = load_employee_data(EMPLOYEES_CSV_PATH)
    index, sorted_dates = build_index(rows)

    newer_entries = get_same_or_newer(query_date, index, sorted_dates)
    print_report(newer_entries)


if __name__ == "__main__":
    main()
