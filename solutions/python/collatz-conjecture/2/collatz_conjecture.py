def steps(number):
    """
    Calculate the number of steps required to reach 1 using the Collatz Conjecture rules.
    The Collatz rules are:
    - If the number is even, divide it by 2.
    - If the number is odd, multiply it by 3 and add 1.
    The process repeats until the number becomes 1.
    Parameters:
        number (int): A positive integer to start the sequence.
    Returns:
        int: The number of steps required to reach 1.
    Raises:
        ValueError: If the input is zero or a negative integer.
    """
    
    if number <= 0: raise ValueError("Only positive integers are allowed")
    
    count = 0
    while number != 1:
        if number % 2 == 0: number //= 2
        else: number = 3 * number + 1
        count += 1
    
    return count
