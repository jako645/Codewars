def open_or_senior(data):
    output = []

    for member in data:
        age = member[0]
        handicap = member[1]

        if age >= 55 and handicap > 7:
            output.append('Senior')
        else:
            output.append('Open')

    return output
