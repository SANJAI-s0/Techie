def rotate(text, key):
    result = []

    for char in text:
        if 'a' <= char <= 'z':
            shifted = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            result.append(shifted)
        elif 'A' <= char <= 'Z':
            shifted = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
            result.append(shifted)
        else:
            result.append(char)

    return ''.join(result)
