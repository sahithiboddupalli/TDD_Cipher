import unittest
import Cipher
class Test(unittest.TestCase):
    def encrypt_is_lower(self):
        cipher = Cipher()
        assert cipher.encrypt("testing", 50) == "rcqrgle"

    def encrypt_is_upper(self):
        cipher = Cipher()
        assert cipher.encrypt("TESTING", 400) == "DOCDSXQ"

    def encrypt_is_digit(self):
        cipher = Cipher()
        assert cipher.encrypt("123", 2) == "123"

    def encrypt_is_alnum(self):
        cipher = Cipher()
        assert cipher.encrypt("ab12C", 3) == "de12F"

        

