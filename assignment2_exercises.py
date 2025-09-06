# assignment2_exercises.py
# Solutions for 10 Python exercises from Assignment 2

import math
import string

# 1. Given a list of numbers, find the sum and average.
def sum_and_average(numbers):
    total = sum(numbers)
    avg = total / len(numbers) if numbers else 0
    return total, avg

# 2. Convert Celsius to Kelvin.
def celsius_to_kelvin(celsius):
    return celsius + 273.15

# 3. Check if a string is a palindrome.
def is_palindrome(s):
    cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

# 4. Reverse a string.
def reverse_string(s):
    return s[::-1]

# 5. Concatenate list of names into one string.
def concatenate_names(names):
    return ' '.join(names)

# 6. Check if a string is a pangram.
def is_pangram(s):
    s = s.lower()
    return all(ch in s for ch in string.ascii_lowercase)

# 7. Calculate area and circumference of a circle.
def circle_area_circumference(radius):
    area = math.pi * radius**2
    circumference = 2 * math.pi * radius
    return area, circumference

# 8. Convert minutes to hours and minutes.
def minutes_to_hours_minutes(minutes):
    hours = minutes // 60
    mins = minutes % 60
    return hours, mins

# 9. Count vowels in a string.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)

# 10. Check if a number is prime.
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Demo outputs for screenshots
if __name__ == "__main__":
    print("1.", sum_and_average([10, 20, 30, 40]))
    print("2.", celsius_to_kelvin(25))
    print("3.", is_palindrome("Madam"))
    print("4.", reverse_string("Python"))
    print("5.", concatenate_names(["Alice", "Bob", "Charlie"]))
    print("6.", is_pangram("The quick brown fox jumps over the lazy dog"))
    print("7.", circle_area_circumference(5))
    print("8.", minutes_to_hours_minutes(135))
    print("9.", count_vowels("This is an example string."))
    print("10.", is_prime(97))