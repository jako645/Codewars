from collections import Counter


def count_feelings(letters, feelings):
    counter = Counter(letters)
    result = 0
    for feeling in feelings:
        result += not (Counter(feeling) - counter)
    return "{} feeling{}.".format(result, "s" if result != 1 else "")
