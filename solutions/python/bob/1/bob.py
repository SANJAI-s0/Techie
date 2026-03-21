def response(hey_bob):
    """
    Return Bob's response to a remark based on its tone:
    - Question → "Sure."
    - Yelling → "Whoa, chill out!"
    - Yelling question → "Calm down, I know what I'm doing!"
    - Silence → "Fine. Be that way!"
    - Anything else → "Whatever."
    """

    if hey_bob.strip() == "": return "Fine. Be that way!"

    is_question = hey_bob.rstrip().endswith("?")
    is_yelling = hey_bob.isupper() and any(c.isalpha() for c in hey_bob)

    if is_yelling and is_question: return "Calm down, I know what I'm doing!"
    if is_yelling: return "Whoa, chill out!"
    if is_question: return "Sure."
    
    return "Whatever."
