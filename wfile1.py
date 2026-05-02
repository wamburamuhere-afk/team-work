# 1. Add two numbers
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

# 2. Square a number
square = lambda x: x ** 2
print(square(4))  # Output: 16

# 3. Check if number is even
is_even = lambda x: x % 2 == 0
print(is_even(10))  # Output: True

# 4. Convert temperature Celsius to Fahrenheit
celsius_to_fahrenheit = lambda c: (c * 9/5) + 32
print(celsius_to_fahrenheit(0))  # Output: 32.0

# 5. Get length of a string
get_length = lambda s: len(s)
print(get_length("Python"))  # Output: 6

# 6. Multiply three numbers
multiply_three = lambda x, y, z: x * y * z
print(multiply_three(2, 3, 4))  # Output: 24

# 7. Get maximum of two numbers
max_num = lambda x, y: x if x > y else y
print(max_num(10, 20))  # Output: 20

# 8. Check if string is palindrome
is_palindrome = lambda s: s == s[::-1]
print(is_palindrome("racecar"))  # Output: True

# 9. Filter even numbers from list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # Output: [2, 4, 6, 8, 10]

# 10. Map and square numbers
squared = list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))
print(squared)  # Output: [1, 4, 9, 16, 25]

# 11. Sort list of tuples by second element
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)  # Output: [('Charlie', 78), ('Alice', 85), ('Bob', 92)]

# 12. Convert list of strings to integers
strings = ["1", "2", "3", "4", "5"]
integers = list(map(lambda x: int(x), strings))
print(integers)  # Output: [1, 2, 3, 4, 5]