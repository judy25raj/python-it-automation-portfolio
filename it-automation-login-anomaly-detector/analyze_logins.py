
#!/usr/bin/env python3
"""
Login Anomaly Detector

A small script that analyzes user login activity and flags potentially
suspicious behavior based on how much higher today's logins are compared
to the historical average.

Usage examples:

    # Analyze a single user from the command line
    python analyze_logins.py --username ejones --current 45 --average 10 --threshold 3.0

    # Analyze multiple users from a CSV file
    python analyze_logins.py --csv sample_logins.csv --threshold 3.0
"""

import argparse
import csv
from typing import Optional


def analyze_logins(
    username: str,
    current_day_logins: int,
    average_day_logins: float,
    threshold: float = 3.0,
) -> bool:
    """
    Analyze a user's login activity and flag potential suspicious behavior.

    Args:
        username: The username being analyzed.
        current_day_logins: Number of login attempts for the current day.
        average_day_logins: Average number of daily login attempts for this user.
        threshold: Ratio above which activity is considered suspicious.
                For example, 3.0 means "3x the average".

    Returns:
        True if activity is potentially suspicious, False otherwise.
    """

    if average_day_logins <= 0:
        print(
            f"[WARN] Cannot analyze logins for {username}: "
            f"average_day_logins must be > 0 (got {average_day_logins})."
        )
        return False

    ratio = current_day_logins / average_day_logins

    print(
        f"Current day login total for {username} is {current_day_logins} "
        f"(average: {average_day_logins:.2f}, ratio: {ratio:.2f}x)"
    )

    if ratio >= threshold:
        print(
            f"[ALERT] Potential suspicious activity detected for {username}: "
            f"login attempts are {ratio:.2f}x the average (threshold={threshold})."
        )
        return True

    print(
        f"[INFO] Login activity for {username} is within normal range "
        f"(threshold={threshold}, ratio={ratio:.2f}x)."
    )
    return False


def analyze_from_csv(csv_path: str, threshold: float) -> None:
    """
    Analyze multiple users from a CSV file.

    Expected CSV header:

        username,current_day_logins,average_day_logins

    Each row will be analyzed and a simple summary printed.
    """
    print(f"\n[INFO] Analyzing login activity from: {csv_path}")
    suspicious_count = 0
    total_count = 0

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            username = row.get("username", "").strip()
            try:
                current = int(row.get("current_day_logins", "0"))
                average = float(row.get("average_day_logins", "0"))
            except ValueError:
                print(
                    f"[WARN] Skipping row with invalid numbers: {row}"
                )
                continue

            total_count += 1
            is_suspicious = analyze_logins(
                username=username,
                current_day_logins=current,
                average_day_logins=average,
                threshold=threshold,
            )
            if is_suspicious:
                suspicious_count += 1
            print("-" * 60)

    print(
        f"\n[SUMMARY] Checked {total_count} user(s). "
        f"Suspicious activity detected for {suspicious_count} user(s)."
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Analyze login activity and flag potential anomalies."
    )

    # Option 1: CSV mode
    parser.add_argument(
        "--csv",
        type=str,
        help="Path to CSV file with columns: username,current_day_logins,average_day_logins",
    )

    # Option 2: single-user mode
    parser.add_argument("--username", type=str, help="Username to analyze")
    parser.add_argument(
        "--current",
        type=int,
        help="Current day login count for the user",
    )
    parser.add_argument(
        "--average",
        type=float,
        help="Average daily login count for the user",
    )

    parser.add_argument(
        "--threshold",
        type=float,
        default=3.0,
        help="Ratio above which logins are considered suspicious (default: 3.0)",
    )

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.csv:
        # Analyze multiple users from a CSV file
        analyze_from_csv(args.csv, args.threshold)
        return

    # Single-user mode: require username, current, average
    if not (args.username and args.current is not None and args.average is not None):
        print(
            "[ERROR] You must either provide --csv PATH "
            "or all of --username, --current, and --average."
        )
        return

    analyze_logins(
        username=args.username,
        current_day_logins=args.current,
        average_day_logins=args.average,
        threshold=args.threshold,
    )


if __name__ == "__main__":
    main()
