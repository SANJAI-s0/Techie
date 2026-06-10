def label(colors):
    values = {
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

    first, second, multiplier = colors[:3]

    resistance = (
        (values[first] * 10 + values[second])
        * (10 ** values[multiplier])
    )

    units = [
        (10**9, "gigaohms"),
        (10**6, "megaohms"),
        (10**3, "kiloohms"),
    ]

    for factor, unit in units:
        if resistance != 0 and resistance % factor == 0:
            return f"{resistance // factor} {unit}"

    return f"{resistance} ohms"