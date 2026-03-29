"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate."""
    return record[1]


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components."""
    return tuple(coordinate)


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match."""
    
    azara_coordinate = convert_coordinate(get_coordinate(azara_record))
    rui_coordinate = rui_record[1]

    return azara_coordinate == rui_coordinate


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group."""
    
    if compare_records(azara_record, rui_record):
        treasure = azara_record[0]
        coordinate = azara_record[1]
        location = rui_record[0]
        rui_coordinate = rui_record[1]
        quadrant = rui_record[2]

        return (treasure, coordinate, location, rui_coordinate, quadrant)

    return "not a match"


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records."""

    report = ""

    for record in combined_record_group:
        treasure, _, location, coordinate, quadrant = record
        cleaned = (treasure, location, coordinate, quadrant)
        report += f"{cleaned}\n"

    return report