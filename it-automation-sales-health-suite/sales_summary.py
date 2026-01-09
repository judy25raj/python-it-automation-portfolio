
#!/usr/bin/env python3
"""sales_summary.py

Reads a sales CSV file and summarizes sales by category:
- Total quantity sold per category
- Total revenue per category

Outputs a formatted text summary that can be used in a PDF or email.
"""

import csv
from collections import defaultdict
from typing import Dict, Tuple


def process_sales_data(csv_path: str) -> str:
    """Process the sales CSV and return a formatted summary string.

    Args:
        csv_path: Path to the sales CSV file.

    Returns:
        A multi-line string summarizing sales by category.
    """
    stats: Dict[str, Tuple[int, float]] = defaultdict(lambda: (0, 0.0))

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            category = row.get("category", "Unknown")
            try:
                quantity = int(row.get("quantity", 0))
                price = float(row.get("price", 0.0))
            except ValueError:
                continue

            total_qty, total_rev = stats[category]
            total_qty += quantity
            total_rev += quantity * price
            stats[category] = (total_qty, total_rev)

    lines = []
    lines.append("Sales Summary by Category\n")
    for category, (qty, rev) in sorted(stats.items()):
        lines.append(f"Category: {category}")
        lines.append(f"  Total Quantity: {qty}")
        lines.append(f"  Total Revenue: ${rev:,.2f}")
        lines.append("")
    return "\n".join(lines)


if __name__ == "__main__":
    summary = process_sales_data("sales.csv")
    print(summary)
