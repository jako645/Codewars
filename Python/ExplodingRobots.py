from collections import Counter

def will_robots_collide(x1, y1, x2, y2, commands):
    c = Counter(commands)
    dx = abs(x1 - x2)
    dy = abs(y1- y2)
    return dx <= c['R'] + c['L'] and dy <= c['U'] + c['D']
