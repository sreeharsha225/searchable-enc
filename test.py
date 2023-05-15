import base64

base64_ciphertext = 'w10iNHk5wQ4HIGBxPnwPU3c='
key = '23CSCZN91CSCZN91CSCZN91C'

def bxor(ba1, ba2):
    """ XOR two byte strings """
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

x = bxor(base64.b64decode(base64_ciphertext), key.encode())
print(len(key.encode()))