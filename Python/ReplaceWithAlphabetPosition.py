def alphabet_position(text):
    answer = []

    for c in text.lower():
        if c.isalpha():
            answer.append(str(ord(c) - 96))

    return ' '.join(answer)
