def square_positive_numbers(numbers):
    """
    Takes a list of integers and returns a new list where each number is squared,
    excluding any negative numbers.

    Args:
        numbers: A list of integers

    Returns:
        A new list containing squared values of non-negative numbers
    """
    return [num**2 for num in numbers if num >= 0]


# Test cases
if __name__ == "__main__":
    # Test 1: Mix of positive and negative numbers
    test1 = [1, -2, 3, -4, 5]
    print(f"Input: {test1}")
    print(f"Output: {square_positive_numbers(test1)}")
    print()

    # Test 2: All positive numbers
    test2 = [1, 2, 3, 4, 5]
    print(f"Input: {test2}")
    print(f"Output: {square_positive_numbers(test2)}")
    print()

    # Test 3: All negative numbers
    test3 = [-1, -2, -3, -4]
    print(f"Input: {test3}")
    print(f"Output: {square_positive_numbers(test3)}")
    print()

    # Test 4: With zero
    test4 = [0, 1, -1, 2, -2]
    print(f"Input: {test4}")
    print(f"Output: {square_positive_numbers(test4)}")
    print()

    # Test 5: Empty list
    test5 = []
    print(f"Input: {test5}")
    print(f"Output: {square_positive_numbers(test5)}")
