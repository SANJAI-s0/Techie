def is_valid(isbn):
    # Remove hyphens
    isbn = isbn.replace("-", "")

    # Must be exactly 10 characters
    if len(isbn) != 10:
        return False

    total = 0

    for i, char in enumerate(isbn):
        if i == 9 and char == "X":
            value = 10
        elif char.isdigit():
            value = int(char)
        else:
            return False

        total += value * (10 - i)

    return total % 11 == 0
