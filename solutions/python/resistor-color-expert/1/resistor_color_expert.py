def resistor_label(colors):
    digit_values = {
        "black": 0,
        "brown": 1,
        "red": 2,
        "orange": 3,
        "yellow": 4,
        "green": 5,
        "blue": 6,
        "violet": 7,
        "grey": 8,
        "white": 9,
    }

    tolerance_values = {
        "grey": "0.05",
        "violet": "0.1",
        "blue": "0.25",
        "green": "0.5",
        "brown": "1",
        "red": "2",
        "gold": "5",
        "silver": "10",
    }

    if len(colors) == 1:
        return "0 ohms"

    if len(colors) == 4:
        value = (
            (digit_values[colors[0]] * 10 + digit_values[colors[1]])
            * (10 ** digit_values[colors[2]])
        )
        tolerance = tolerance_values[colors[3]]

    else:  # 5 bands
        value = (
            (
                digit_values[colors[0]] * 100
                + digit_values[colors[1]] * 10
                + digit_values[colors[2]]
            )
            * (10 ** digit_values[colors[3]])
        )
        tolerance = tolerance_values[colors[4]]

    units = ["ohms", "kiloohms", "megaohms", "gigaohms"]
    unit_index = 0

    while value >= 1000 and unit_index < len(units) - 1:
        value /= 1000
        unit_index += 1

    if value == int(value):
        value_str = str(int(value))
    else:
        value_str = f"{value:.2f}".rstrip("0").rstrip(".")

    return f"{value_str} {units[unit_index]} ±{tolerance}%"
