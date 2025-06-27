import random
import string


def text_generator(pswd=False):
    chars = string.ascii_letters + string.digits
    if pswd == True:
        chars += "!@#$%^&*()_+-="
    password = ''.join(random.choices(chars, k=5))
    return password
