<h1 align="center">Debug and Solve Software Problems</h1>

<p align="center">
  Python • Debugging • Performance Optimization • Data Processing
</p>

<hr/>

This project is based on the Google IT Automation with Python lab
"Debug and Solve Software Problems".

## 🧩 Scenario
A Python program reads a CSV file with employee start dates and generates a report for people who started on or after a given date. The original script was incomplete and unstable:

- Crashed with a TypeError when reading date input  
- Performed slowly on large datasets due to repeated CSV processing  

The objective is to debug the crash, remove performance bottlenecks, and produce a clean, maintainable script.

## ✅ What This Project Demonstrates

### Debugging
- Understanding tracebacks and root cause analysis  
- Fixing incorrect data types (input strings vs datetime integers)

### Performance Improvements
- Avoiding repeated CSV reads and parsing  
- Pre-processing data into efficient structures:
  - Dictionary: start_date → [employees]
  - Sorted list of dates

### Clean Code & Structure
Small, focused functions:
- load_employee_data  
- build_index  
- get_same_or_newer  
- print_report  

Clear separation of I/O, processing, and reporting.

## 📂 Project Structure
```
google-it-automation-debug-software-problems/
├─ start_date_report.py
├─ employees-with-date.csv
└─ README.md
```

## 🐞 Bug Fix – TypeError in get_start_date()
Original issue:
input() returns strings, but datetime requires integers.

**Fix:**
```
year = int(input("Enter a value for the year: "))
month = int(input("Enter a value for the month: "))
day = int(input("Enter a value for the day: "))
```

## 🚀 Performance Improvement – Pre-processing the CSV
Optimized approach:
- Load CSV once
- Build an index: date → employees
- Maintain sorted list of dates
- Query via fast lookups instead of repeated scans

## ▶️ How to Run
```
python3 start_date_report.py
```

Enter a date when prompted.

## 🧠 Portfolio Summary
Refactored and optimized an inherited Python reporting script by fixing a crashing TypeError in date handling and improving performance through indexed, pre-processed CSV data structures.
