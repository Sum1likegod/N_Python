import random
import string


def encod(inp_str):
    if len(inp_str) > 3:
        inp_str = inp_str[1:] + inp_str[0]
        return random_string() + inp_str + random_string()
    else:
        return "".join(reversed(inp_str))


def decod(inp_str):
    if len(inp_str) > 3:
        return inp_str[-4] + inp_str[3:-4]
    else:
        return "".join(reversed(inp_str))


def random_string():
    letters = string.ascii_letters
    rand_combo = ''
    for i in range(3):
        rand_combo += random.choice(letters)
    return rand_combo


aski = int(input("press 1 for encoding and 2 for decoding: "))

if aski == 1:
    sent_str = input("Enter the string to encode: ")
    for words in sent_str.split(" "):
        print(encod(words), end=" ")


elif aski == 2:
    sent_str = input("Enter the string to decode: ")
    for words in sent_str.split(" "):
        print(decod(words), end=" ")
