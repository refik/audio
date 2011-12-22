import string
import random

def random_string(size=3):
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for x in range(size))
