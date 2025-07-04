from preloaded import MORSE_CODE


def decode_morse(morse_code):
    return ' '.join([''.join([MORSE_CODE[ml] for ml in mw.split(' ')])
                     for mw in morse_code.strip().split('   ')])
