"""
Please write you name here:
"""
from typing import Tuple


def process_shifts(path_to_csv: str) -> dict:
    """
    Args:
        path_to_csv(str): The path to the work_shift.csv

    Returns:
        A dictionary with time as key (str) with format %H:%M
        (e.g. "18:00") and cost as value (Number)

    For example, it should be something like:

        {
            "17:00": 50,
            "22:00: 40,
        }

    In other words, for the hour beginning at 17:00, labour cost was
    50 pounds

    """
    return NotImplemented


def process_sales(path_to_csv: str) -> dict:
    """
    Args:
        path_to_csv (str): The path to the transactions.csv

    Returns:
        A dictionary with time (string) with format %H:%M as key and
        sales as value (string),
        and corresponding value with format %H:%M (e.g. "18:00"),
        and type float)

    For example, it should be something like:

        {
            "17:00": 250,
            "22:00": 0,
        }

    This means, for the hour beginning at 17:00, the sales were 250 dollars
    and for the hour beginning at 22:00, the sales were 0.

    """
    return NotImplemented


def compute_percentage(shifts: dict, sales: dict) -> dict:
    """
    Args:
        shifts (dict):
        sales (dict):

    Returns:
        A dictionary with time as key (string) with format %H:%M and
        percentage of labour cost per sales as value (float),
        If the sales are null, then return -cost instead of percentage

    For example, it should be something like:

        {
            "17:00": 20,
            "22:00": -40,
        }

    """
    return NotImplemented


def best_and_worst_hour(percentages: dict) -> Tuple[str, str]:
    """
    Args:
        percentages (dict): output of compute_percentage
    Returns:
        A list or tuple of strings, the first element should be the best hour,
        the second (and last) element should be the worst hour. Hour are
        represented by string with format %H:%M
        e.g. "18:00", "20:00"

    """
    return NotImplemented


def main(path_to_shifts, path_to_sales) -> Tuple[str, str]:
    """
    Do not touch this function, but you can look at it, to have an idea of
    how your data should interact with each other
    """

    shifts_processed = process_shifts(path_to_shifts)
    sales_processed = process_sales(path_to_sales)
    percentages = compute_percentage(shifts_processed, sales_processed)
    best_hour, worst_hour = best_and_worst_hour(percentages)
    return best_hour, worst_hour


if __name__ == "__main__":
    # You can change this to test your code, it will not be used
    your_path_to_sales = ""
    your_path_to_shifts = ""
    best, worst = main(your_path_to_shifts, your_path_to_sales)
