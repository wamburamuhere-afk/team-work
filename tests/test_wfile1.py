def test_add():
    add = lambda x, y: x + y
    assert add(5, 3) == 8

def test_square():
    square = lambda x: x ** 2
    assert square(4) == 16

def test_is_even():
    is_even = lambda x: x % 2 == 0
    assert is_even(10) is True
    assert is_even(7) is False

def test_celsius_to_fahrenheit():
    celsius_to_fahrenheit = lambda c: (c * 9 / 5) + 32
    assert celsius_to_fahrenheit(0) == 32.0
    assert celsius_to_fahrenheit(100) == 212.0

def test_is_palindrome():
    is_palindrome = lambda s: s == s[::-1]
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False

def test_filter_evens():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    assert evens == [2, 4, 6, 8, 10]
