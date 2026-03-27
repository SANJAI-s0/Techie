"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""


def exchange_money(budget, exchange_rate):
    """
    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    Example:
    >>> exchange_money(127.5, 1.2)
    106.25
    """
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """
    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    Example:
    >>> get_change(127.5, 120)
    7.5
    """
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """
    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    Example:
    >>> get_value_of_bills(5, 128)
    640
    """
    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """
    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    Example:
    >>> get_number_of_bills(127.5, 5)
    25
    """
    return int(amount // denomination)


def get_leftover_of_bills(amount, denomination):
    """
    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    Example:
    >>> get_leftover_of_bills(127.5, 20)
    7.5
    """
    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    Examples:
    >>> exchangeable_value(127.25, 1.20, 10, 20)
    80
    >>> exchangeable_value(127.25, 1.20, 10, 5)
    95
    """
    # increase exchange rate by spread percentage (spread is given as integer percent)
    adjusted_rate = exchange_rate * (1 + spread / 100.0)
    # foreign currency amount after applying fee
    foreign_amount = budget / adjusted_rate
    # number of whole bills we can get
    number_of_whole_bills = int(foreign_amount // denomination)
    # total exchangeable value in whole bills (int)
    return number_of_whole_bills * denomination