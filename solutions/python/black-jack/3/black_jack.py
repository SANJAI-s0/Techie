"""Functions to help play and score a game of blackjack."""

FACE_CARDS = {"J", "Q", "K"}
TEN_CARDS = {"10", "J", "Q", "K"}
DOUBLE_DOWN_TOTALS = {9, 10, 11}


def value_of_card(card: str) -> int:
    """Return the blackjack value of a single card.

    Face cards (J, Q, K) are worth 10.
    Ace (A) is treated as 1 for this function.
    Number cards return their integer value.
    """

    if card in FACE_CARDS:
        return 10

    if card == "A":
        return 1

    return int(card)


def higher_card(card_one: str, card_two: str) -> str | tuple[str, str]:
    """Return the card with the higher blackjack value.

    If both cards have the same value, return both as a tuple.
    """

    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one > value_two:
        return card_one

    if value_two > value_one:
        return card_two

    return card_one, card_two


def value_of_ace(card_one: str, card_two: str) -> int:
    """Return the best value (1 or 11) for an upcoming Ace."""

    if "A" in {card_one, card_two}:
        return 1

    total = value_of_card(card_one) + value_of_card(card_two)

    if total + 11 <= 21:
        return 11

    return 1


def is_blackjack(card_one: str, card_two: str) -> bool:
    """Return True if the hand is a natural blackjack."""

    return (
        (card_one == "A" and card_two in TEN_CARDS)
        or (card_two == "A" and card_one in TEN_CARDS)
    )


def can_split_pairs(card_one: str, card_two: str) -> bool:
    """Return True if the hand can be split."""

    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one: str, card_two: str) -> bool:
    """Return True if the hand total allows doubling down."""

    total = value_of_card(card_one) + value_of_card(card_two)
    return total in DOUBLE_DOWN_TOTALS