def cube_volume(h, r):
    a = r * (2**0.5)
    return round(a**3, 2) if a < h else round(h**3, 2)
