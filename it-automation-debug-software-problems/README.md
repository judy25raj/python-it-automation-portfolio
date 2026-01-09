# Google Project 7 – Debug and Solve Software Problems

This project is based on the **Google IT Automation with Python** lab  
**"Debug and Solve Software Problems"**.

## 🧩 Scenario

A colleague who recently left the company wrote a Python program that reads a
CSV file with employee start dates and generates a report for people who started
on or after a given date. The script is about **90% complete**, but:

- It **crashes** with a `TypeError` when asking for the date.
- It runs **too slowly** for large datasets, because it repeatedly re-processes
  the same file.

Your job is to:
1. Debug and fix the crash.
2. Find and remove performance bottlenecks.
3. Produce a clean, maintainable version of the script.

---

## ✅ What This Project Demonstrates

- **Debugging**
  - Understanding tracebacks and root cause analysis.
  - Fixing incorrect data types (`input()` strings vs `datetime` integers).

- **Performance improvements**
  - Avoiding repeated work (no re-reading or re-parsing the CSV on each loop).
  - Pre-processing data into efficient structures:
    - Dictionary: `start_date -> [employees]`
    - Sorted list of dates.

- **Clean code & structure**
  - Small, focused functions:
    - `load_employee_data`
    - `build_index`
    - `get_same_or_newer`
    - `print_report`
  - Clear separation of I/O, processing, and reporting.

---

## 📂 Project Structure

```text
google-it-automation-debug-software-problems/
├─ start_date_report.py        # Fixed + optimized version of the lab script
├─ employees-with-date.csv     # Sample employee data for testing
└─ README.md                   # This file
```

---

## 🐞 Bug Fix – TypeError in `get_start_date()`

Original issue in the lab:

- The script used `input()` to read year, month, and day.
- `datetime.datetime(year, month, day)` requires **integers**, but `input()`
  returns **strings**.
- This caused:

  ```text
  TypeError: an integer is required (got type str)
  ```

Fix in this version:

```python
year = int(input("Enter a value for the year: "))
month = int(input("Enter a value for the month: "))
day = int(input("Enter a value for the day: "))
```

---

## 🚀 Performance Improvement – Pre-processing the CSV

Original design problem:

- The script effectively re-processed the CSV for each queried date.
- For large datasets or repeated queries, this leads to noticeable slowness.

Optimized approach (implemented here):

1. **Load data once** from `employees-with-date.csv`:

   ```python
   rows = load_employee_data(EMPLOYEES_CSV_PATH)
   ```

2. **Build an index**:

   ```python
   index, sorted_dates = build_index(rows)
   ```

   - `index`: `dict[date -> list_of_employee_names]`
   - `sorted_dates`: sorted list of all start dates found in the CSV.

3. To get all employees who started on or after a given date:

   ```python
   entries = get_same_or_newer(query_date, index, sorted_dates)
   ```

This converts repeated expensive work into a single preprocessing pass plus a
fast lookup over a sorted list.

---

## ▶️ How to Run

1. Make sure you have Python 3 installed.

2. From the project folder, run:

   ```bash
   python3 start_date_report.py
   ```

3. When prompted, enter a date, for example:

   ```text
   Enter a value for the year: 2018
   Enter a value for the month: 2
   Enter a value for the day: 3
   ```

   Example output:

   ```text
   Started on Feb 05, 2018: ['Sydnee Pickett']
   Started on Feb 07, 2018: ['Dalton Dennis']
   Started on Feb 08, 2018: ['Edward Nichols']
   Started on Feb 09, 2018: ['Bradley Workman']
   Started on Feb 10, 2018: ['Rina Mcfarland']
   ```

   Or with a later date:

   ```text
   Enter a value for the year: 2019
   Enter a value for the month: 10
   Enter a value for the day: 5
   ```

   Example output:

   ```text
   Started on Oct 06, 2019: ['Darius Goodman']
   Started on Oct 15, 2019: ['Idola Warren']
   Started on Oct 16, 2019: ['Hu Hyde', 'Lesley Fuentes']
   ```

---

## 🧠 Project Story (Portfolio Narrative)

In this lab-inspired project, I practiced both **debugging** and **performance
tuning** on an inherited Python script:

- I started with a broken program that crashed on basic user input due to a
  simple but critical type mismatch.
- After fixing the `TypeError`, I turned to performance: profiling the script
  showed it was re-processing the same CSV data multiple times.
- I redesigned the core logic to:
  - Load the CSV once.
  - Build an index keyed by start date.
  - Use a sorted list of dates to quickly answer queries.

You can summarize this project as:

> "Refactored and optimized an inherited Python reporting script:
> fixed a crashing TypeError in date handling and improved performance by
> pre-processing CSV data into indexed structures, turning repeated O(N)
> scans into fast lookups over a sorted date list."
