def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list gracefully
    return sum(numbers) / len(numbers)

my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list)
print(f"The average of an empty list is: {average_empty}")

#Illustrating potential ZeroDivisionError
try:
    bad_average = calculate_average([])
    print(f"The average is: {bad_average}")
except ZeroDivisionError as e:
    print(f"Error: {e}") 