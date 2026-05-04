from typing import List

def calculate_average(numbers: List[float]) -> float:
    """
    Calculate the average of a list of numbers.

    Args:
        numbers: A list of float numbers.

    Returns:
        The average of the numbers as a float.
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)