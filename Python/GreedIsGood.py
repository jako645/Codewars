from collections import Counter


def score(dice):
    dice_counter = Counter(dice)
    score_sum = 0
    for c in dice_counter:
        score_sum += dice_counter[c] // 3 * (1000 if c == 1 else c * 100)
        score_sum += dice_counter[c] % 3 * (100 if c == 1 else 50 if c == 5 else 0)
    return score_sum


if __name__ == "__main__":
    print(score([1, 1, 1, 3, 1]))
