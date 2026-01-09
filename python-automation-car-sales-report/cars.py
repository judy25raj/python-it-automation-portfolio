#!/usr/bin/env python3
"""cars.py

Project 3 – Automatically Generate a PDF and Send it by Email.

- Loads monthly car sales data from car_sales.json
- Computes:
    * Car that generated the most revenue
    * Car with the most total sales
    * Most popular sales year across all cars
- Generates a PDF report (/tmp/cars.pdf) with a summary and table
- Emails the PDF report to the configured recipient

This implementation closely follows the Google IT Automation with Python lab.
"""

import json
import locale
import sys
import os

import reports
import emails


def load_data(filename):
    """Loads the contents of filename as a JSON file."""
    with open(filename) as f:
        data = json.load(f)
    return data


def format_car(car):
    """Given a car dictionary, returns a nicely formatted name.

    Example: {"car_make": "Acura", "car_model": "TL", "car_year": 2007}
             -> "Acura TL (2007)"
    """
    return f"{car['car_make']} {car['car_model']} ({car['car_year']})"


def process_data(data):
    """Analyzes the data, looking for maximums.

    Returns a list of summary lines:
    - The <car> generated the most revenue: $X
    - The <car> had the most sales: Y
    - The most popular year was <year> with <total sales> sales.
    """
    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

    max_revenue = {"car": None, "revenue": 0}
    max_sales = {"car": None, "total_sales": 0}
    sales_by_year = {}

    for item in data:
        price = locale.atof(item["price"].strip("$"))
        revenue = price * item["total_sales"]

        # Most revenue
        if revenue > max_revenue["revenue"]:
            max_revenue["revenue"] = revenue
            max_revenue["car"] = item["car"]

        # Most sales
        if item["total_sales"] > max_sales["total_sales"]:
            max_sales["total_sales"] = item["total_sales"]
            max_sales["car"] = item["car"]

        # Sales by year
        year = item["car"]["car_year"]
        sales_by_year[year] = sales_by_year.get(year, 0) + item["total_sales"]

    # Determine most popular year
    popular_year = None
    popular_year_sales = 0
    for year, year_sales in sales_by_year.items():
        if year_sales > popular_year_sales:
            popular_year_sales = year_sales
            popular_year = year

    summary = []
    summary.append(
        f"The {format_car(max_revenue['car'])} generated the most revenue: ${max_revenue['revenue']:.2f}"
    )
    summary.append(
        f"The {format_car(max_sales['car'])} had the most sales: {max_sales['total_sales']}"
    )
    summary.append(
        f"The most popular year was {popular_year} with {popular_year_sales} sales."
    )

    return summary


def cars_dict_to_table(data):
    """Turns the data into a list of lists suitable for a table in a PDF.

    Header: ["ID", "Car", "Price", "Total Sales"]
    Rows:   [id, formatted car, price, total_sales]
    """
    table_data = [["ID", "Car", "Price", "Total Sales"]]
    for item in data:
        car = format_car(item["car"])
        row = [item["id"], car, item["price"], item["total_sales"]]
        table_data.append(row)
    return table_data


def main(argv):
    data = load_data("car_sales.json")

    # Process data to get summary lines
    summary = process_data(data)
    # Summary as text for email
    summary_text = "\n".join(summary)
    # Summary with <br/> for PDF
    summary_html = "<br/>".join(summary)

    # Generate PDF report
    pdf_path = "/tmp/cars.pdf"
    title = "Sales summary for last month"
    table_data = cars_dict_to_table(data)
    reports.generate(pdf_path, title, summary_html, table_data)

    # Generate and send email with attachment
    sender = "automation@example.com"
    recipient = "student@example.com"  # adjust as needed
    subject = "Sales summary for last month"
    body = summary_text

    message = emails.generate(sender, recipient, subject, body, pdf_path)
    emails.send(message)


if __name__ == "__main__":
    main(sys.argv)
