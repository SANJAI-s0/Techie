PARTS = [
    ("house", "that Jack built."),
    ("malt", "that lay in the house"),
    ("rat", "that ate the malt"),
    ("cat", "that killed the rat"),
    ("dog", "that worried the cat"),
    ("cow with the crumpled horn", "that tossed the dog"),
    ("maiden all forlorn", "that milked the cow with the crumpled horn"),
    ("man all tattered and torn", "that kissed the maiden all forlorn"),
    ("priest all shaven and shorn", "that married the man all tattered and torn"),
    ("rooster that crowed in the morn", "that woke the priest all shaven and shorn"),
    ("farmer sowing his corn", "that kept the rooster that crowed in the morn"),
    ("horse and the hound and the horn", "that belonged to the farmer sowing his corn"),
]


def recite(start_verse, end_verse):
    verses = []

    for verse in range(start_verse, end_verse + 1):
        parts = [PARTS[verse - 1][0]]

        for i in range(verse - 1, 0, -1):
            parts.append(PARTS[i][1])

        verses.append("This is the " + " ".join(parts) + " that Jack built.")

    return verses
