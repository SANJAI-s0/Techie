def is_armstrong_number(number):
    # Convert number to string to easily iterate over digits
    digits = str(number)
    power = len(digits)
    
    # Calculate sum of digits raised to the power of number of digits
    total = sum(int(digit) ** power for digit in digits)
    
    # Check if it equals the original number
    return total == number
