def solution(s):
    answer = []

    if len(s) % 2:
        s += '_'

    for i in range(0, len(s), 2):
        answer.append(s[i:i+2])

    return answer
