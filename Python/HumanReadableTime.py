def make_readable(seconds):
    hours = seconds // 3600
    minutes = seconds // 60 % 60
    seconds = seconds % 60
    return ':'.join([f'{hours:02}', f'{minutes:02}', f'{seconds:02}'])
