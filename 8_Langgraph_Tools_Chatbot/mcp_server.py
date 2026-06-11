from pathlib import Path
import os
import sys

current_dir = os.path.normcase(os.path.normpath(str(Path(__file__).resolve().parent)))
sys.path = [
    path for path in sys.path
    if os.path.normcase(os.path.normpath(str(Path(path or ".").resolve()))) != current_dir
]

from mcp.server.fastmcp import FastMCP


mcp = FastMCP("expense-server")

MONTH_ALIASES = {
    "jan": "january",
    "january": "january",
    "feb": "february",
    "february": "february",
    "mar": "march",
    "march": "march",
    "apr": "april",
    "april": "april",
    "may": "may",
    "jun": "june",
    "june": "june",
    "jul": "july",
    "july": "july",
    "aug": "august",
    "august": "august",
    "sep": "september",
    "sept": "september",
    "september": "september",
    "oct": "october",
    "october": "october",
    "nov": "november",
    "november": "november",
    "dec": "december",
    "december": "december",
}

EXPENSES = {
    "january": [
        {"day": 1, "category": "rent", "description": "Apartment rent", "amount": 1200.00},
        {"day": 4, "category": "groceries", "description": "Weekly groceries", "amount": 92.40},
        {"day": 15, "category": "utilities", "description": "Electricity bill", "amount": 118.75},
        {"day": 22, "category": "dining", "description": "Dinner with friends", "amount": 48.60},
        {"day": 29, "category": "internet", "description": "Home internet", "amount": 59.99},
    ],
    "february": [
        {"day": 1, "category": "rent", "description": "Apartment rent", "amount": 1200.00},
        {"day": 5, "category": "groceries", "description": "Weekly groceries", "amount": 88.15},
        {"day": 14, "category": "dining", "description": "Valentine dinner", "amount": 86.20},
        {"day": 20, "category": "utilities", "description": "Water bill", "amount": 37.40},
        {"day": 27, "category": "subscription", "description": "Streaming services", "amount": 24.99},
    ],
    "march": [
        {"day": 1, "category": "rent", "description": "Apartment rent", "amount": 1200.00},
        {"day": 6, "category": "groceries", "description": "Weekly groceries", "amount": 95.10},
        {"day": 11, "category": "health", "description": "Pharmacy", "amount": 31.45},
        {"day": 23, "category": "utilities", "description": "Gas bill", "amount": 52.70},
        {"day": 30, "category": "shopping", "description": "Clothing", "amount": 76.80},
    ],
    "april": [
        {"day": 1, "category": "rent", "description": "Apartment rent", "amount": 1200.00},
        {"day": 3, "category": "groceries", "description": "Weekly groceries", "amount": 90.25},
        {"day": 13, "category": "utilities", "description": "Electricity bill", "amount": 104.30},
        {"day": 21, "category": "entertainment", "description": "Movie tickets", "amount": 32.00},
        {"day": 28, "category": "internet", "description": "Home internet", "amount": 59.99},
    ],
    "may": [
        {"day": 1, "category": "rent", "description": "Apartment rent", "amount": 1200.00},
        {"day": 7, "category": "groceries", "description": "Weekly groceries", "amount": 101.35},
        {"day": 12, "category": "transport", "description": "Fuel", "amount": 47.80},
        {"day": 18, "category": "health", "description": "Doctor visit copay", "amount": 35.00},
        {"day": 31, "category": "utilities", "description": "Water bill", "amount": 39.15},
    ],
    "june": [
        {"day": 1, "category": "rent", "description": "Apartment rent", "amount": 1200.00},
        {"day": 4, "category": "groceries", "description": "Weekly groceries", "amount": 97.50},
        {"day": 15, "category": "utilities", "description": "Electricity bill", "amount": 126.40},
        {"day": 22, "category": "travel", "description": "Weekend trip", "amount": 210.00},
        {"day": 29, "category": "internet", "description": "Home internet", "amount": 59.99},
    ],
    "july": [
        {"day": 1, "category": "rent", "description": "Apartment rent", "amount": 1200.00},
        {"day": 5, "category": "groceries", "description": "Weekly groceries", "amount": 93.75},
        {"day": 10, "category": "dining", "description": "Holiday dinner", "amount": 68.40},
        {"day": 24, "category": "utilities", "description": "Electricity bill", "amount": 141.60},
        {"day": 30, "category": "subscription", "description": "Cloud storage", "amount": 9.99},
    ],
    "august": [
        {"day": 1, "category": "rent", "description": "Apartment rent", "amount": 1200.00},
        {"day": 6, "category": "groceries", "description": "Weekly groceries", "amount": 99.20},
        {"day": 12, "category": "transport", "description": "Metro pass", "amount": 64.00},
        {"day": 25, "category": "utilities", "description": "Water bill", "amount": 41.10},
        {"day": 31, "category": "internet", "description": "Home internet", "amount": 59.99},
    ],
    "september": [
        {"day": 1, "category": "rent", "description": "Apartment rent", "amount": 1200.00},
        {"day": 4, "category": "groceries", "description": "Weekly groceries", "amount": 91.85},
        {"day": 16, "category": "education", "description": "Course subscription", "amount": 79.00},
        {"day": 23, "category": "utilities", "description": "Gas bill", "amount": 49.35},
        {"day": 30, "category": "dining", "description": "Coffee and snacks", "amount": 23.70},
    ],
    "october": [
        {"day": 1, "category": "rent", "description": "Apartment rent", "amount": 1200.00},
        {"day": 5, "category": "groceries", "description": "Weekly groceries", "amount": 96.45},
        {"day": 18, "category": "utilities", "description": "Electricity bill", "amount": 112.25},
        {"day": 25, "category": "entertainment", "description": "Concert ticket", "amount": 85.00},
        {"day": 31, "category": "subscription", "description": "Streaming services", "amount": 24.99},
    ],
    "november": [
        {"day": 1, "category": "rent", "description": "Apartment rent", "amount": 1200.00},
        {"day": 3, "category": "groceries", "description": "Weekly groceries", "amount": 98.70},
        {"day": 8, "category": "transport", "description": "Metro pass", "amount": 64.00},
        {"day": 15, "category": "utilities", "description": "Electricity bill", "amount": 119.80},
        {"day": 22, "category": "dining", "description": "Dinner outing", "amount": 57.25},
        {"day": 29, "category": "shopping", "description": "Black Friday shopping", "amount": 185.40},
    ],
    "december": [
        {"day": 1, "category": "rent", "description": "Apartment rent", "amount": 1200.00},
        {"day": 6, "category": "groceries", "description": "Weekly groceries", "amount": 104.90},
        {"day": 12, "category": "transport", "description": "Fuel", "amount": 46.75},
        {"day": 18, "category": "gifts", "description": "Holiday gifts", "amount": 240.00},
        {"day": 24, "category": "dining", "description": "Holiday meal", "amount": 132.60},
        {"day": 30, "category": "internet", "description": "Home internet", "amount": 59.99},
    ],
}


def normalize_month(month: str) -> str:
    month_key = month.strip().lower()
    if month_key not in MONTH_ALIASES:
        raise ValueError(f"Unknown month: {month}")
    return MONTH_ALIASES[month_key]


def total_amount(expenses: list[dict]) -> float:
    return round(sum(expense["amount"] for expense in expenses), 2)


@mcp.tool()
def get_expenses_for_month(month: str) -> dict:
    """Get all hardcoded expenses for a month, such as Jan, February, or Nov."""
    month_name = normalize_month(month)
    expenses = EXPENSES[month_name]
    return {
        "month": month_name.title(),
        "total": total_amount(expenses),
        "expenses": expenses,
    }


@mcp.tool()
def get_expenses_between_days(month: str, start_day: int, end_day: int) -> dict:
    """Get expenses between a start day and end day within a month."""
    if start_day > end_day:
        raise ValueError("start_day must be less than or equal to end_day")

    month_name = normalize_month(month)
    expenses = [
        expense for expense in EXPENSES[month_name]
        if start_day <= expense["day"] <= end_day
    ]
    return {
        "month": month_name.title(),
        "start_day": start_day,
        "end_day": end_day,
        "total": total_amount(expenses),
        "expenses": expenses,
    }


@mcp.tool()
def get_weekly_cost_for_month(month: str) -> dict:
    """Get week-by-week expense totals for a month."""
    month_name = normalize_month(month)
    weeks = [
        {"week": 1, "start_day": 1, "end_day": 7, "total": 0.0},
        {"week": 2, "start_day": 8, "end_day": 14, "total": 0.0},
        {"week": 3, "start_day": 15, "end_day": 21, "total": 0.0},
        {"week": 4, "start_day": 22, "end_day": 28, "total": 0.0},
        {"week": 5, "start_day": 29, "end_day": 31, "total": 0.0},
    ]

    for expense in EXPENSES[month_name]:
        for week in weeks:
            if week["start_day"] <= expense["day"] <= week["end_day"]:
                week["total"] = round(week["total"] + expense["amount"], 2)
                break

    return {
        "month": month_name.title(),
        "total": total_amount(EXPENSES[month_name]),
        "weekly_costs": weeks,
    }


if __name__ == "__main__":
    mcp.run(transport="stdio")
