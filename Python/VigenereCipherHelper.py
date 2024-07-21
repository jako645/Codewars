class VigenereCipher(object):
    def __init__(self, key: str, alphabet: str):
        self.key = key
        self.alphabet = alphabet

    def encode(self, text: str) -> str:
        encoded_text = ''
        for index, letter in enumerate(text):
            if letter in self.alphabet:
                key_letter = self.key[index % len(self.key)]
                shift = self.alphabet.find(key_letter)
                encoded_text += self.alphabet[
                    (self.alphabet.find(letter) + shift) % len(self.alphabet)]
            else:
                encoded_text += letter
        return encoded_text

    def decode(self, text: str) -> str:
        decoded_text = ''
        for index, letter in enumerate(text):
            if letter in self.alphabet:
                key_letter = self.key[index % len(self.key)]
                shift = self.alphabet.find(key_letter)
                decoded_text += self.alphabet[
                    (self.alphabet.find(letter) - shift) % len(self.alphabet)]
            else:
                decoded_text += letter
        return decoded_text
