COLORS = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]

def color_code(color):
    """
    Return the numeric value associated with a resistor color.
    Args: color (str) - The resistor color name.
    Returns: int - The digit represented by the color.
    """
    return COLORS.index(color)

def colors():
    """
    Return all valid resistor colors in code order.
    Returns: list[str] - A list of resistor color names.
    """
    return COLORS
