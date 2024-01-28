def narcissistic(value):
    sum = 0

    for digit_char in str(value):
        sum += pow(int(digit_char), len(str(value)))

    return value == sum
