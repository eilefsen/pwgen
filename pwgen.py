#!/usr/bin/env python3
import string
import secrets
import argparse

#import request
from urllib.request import urlopen

def fetch_words():
    word_list = [""]
    try:
        with open("words.txt", "r") as file:
            for line in file:
                word_list.append(line.rstrip())
    except FileNotFoundError:
        url = "https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt"
        with urlopen(url) as file:
            for line in file:
                line_parse = line.split()
                word_list.append(line_parse[1].decode('utf-8'))
    return word_list

def generate(word_list):
    lowercase   = ''.join(secrets.choice(string.ascii_lowercase)    for i in range(64))
    uppercase   = ''.join(secrets.choice(string.ascii_uppercase)    for i in range(64))
    digits      = ''.join(secrets.choice(string.digits)             for i in range(64))
    symbols     = ''.join(secrets.choice('/=!@#$%&*()')        for i in range(64))
    combined_sequence = ""
    words = [""]

    if args.words:
        words = [secrets.choice(word_list) for x in range(words_amount)]
    if args.uppercase:
        combined_sequence += uppercase
        words = [i.capitalize() for i in words]
    if args.digits:
        combined_sequence += digits
        words.insert(0, digits[0:2])
    if args.symbols:
        combined_sequence += symbols
        words.append(symbols[0:2])
    if args.words:
        password = '-'.join(words)
    else:
        combined_sequence += lowercase
        password = ''.join(secrets.choice(combined_sequence) for i in range(args.length))

    return password

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
                        prog='pwgen',
                        description='Generates strong, secure passwords.')
    parser.add_argument('-u', '--uppercase', action='store_true', help='use uppercase letters in the password')     # Uppercase
    parser.add_argument('-d', '--digits', action='store_true', help='use digits (numbers 0 to 9) in the password')  # Digits
    parser.add_argument('-s', '--symbols', action='store_true', help='use special symbols in the password')         # symbols 
    parser.add_argument('-w', '--words', action='store_true', help='use english words in the password')             # dictionary words
    parser.add_argument('-l', '--length', type=int, default=16, metavar='x', help="set the length of the password")                        # length
    args = parser.parse_args()

    words_amount = 4
    word_list = [""]
    if args.words:
        word_list = fetch_words()
        if args.length != 16:
            words_amount = int(args.length)

for i in range(25):
    print(generate(word_list))
