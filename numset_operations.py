# User inputs a list of numerical values separated by spaces for its mean, median, mode, range, and standard deviation

import statistics

def get_statistics(numbers):
    if not numbers:
        return "No data", "No data", "No data", "No data", "No data"

    mean_value = statistics.mean(numbers)
    median_value = statistics.median(numbers)
    try:
        mode_value = statistics.mode(numbers)
    except statistics.StatisticsError:
        mode_value = "No unique mode"
    range_value = max(numbers) - min(numbers)
    std_dev_value = statistics.stdev(numbers) if len(numbers) > 1 else 0

    return mean_value, median_value, mode_value, range_value, std_dev_value

def main():
    print("Welcome to the Number Set Operator.")
    user_input = input("Enter a set of numbers separated by spaces: ")

    numbers = user_input.split()
    if not numbers:
        print("Invalid input. Please enter at least one number.")
        return

    try:
        numbers = list(map(float, numbers))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    mean_value, median_value, mode_value, range_value, std_dev_value = get_statistics(numbers)

    print(f"\nMean: {mean_value:.2f}")
    print(f"Median: {median_value:.2f}")
    print(f"Mode: {mode_value:.2f}")
    print(f"Range: {range_value:.2f}")
    print(f"Standard Deviation: {std_dev_value:.2f}")

main()


