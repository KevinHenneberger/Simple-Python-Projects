class CaesarCipher:

    def __init__(self, text, shift):
        self.text = text
        self.shift = shift 

    def encrypt(self):

        cipher_text = ""

        for ch in self.text:
            if (ch.isalpha()):
                if (ch == ch.lower()):
                    cipher_text += chr((ord(ch) - 97 + self.shift) % 26 + 97)
                else:
                    cipher_text += chr((ord(ch) - 65 + self.shift) % 26 + 65)
            else: 
                cipher_text += ch

        return cipher_text

    def decrypt(self):

        cipher_text = ""

        for ch in self.text:
            if (ch.isalpha()):
                if (ch == ch.lower()):
                    cipher_text += chr((ord(ch) - 97 - self.shift) % 26 + 97)
                else:
                    cipher_text += chr((ord(ch) - 65 - self.shift) % 26 + 65)
            else: 
                cipher_text += ch

        return cipher_text
