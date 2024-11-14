r"""
Title: dictionary
Description: A simple english dictionary
Author: CryptoPatrick <cryptopatrick@gmail.com>"
Date: 2024.11.13
"""

from difflib import get_close_matches # to compare strings for similarity.
import json
db = json.load(open("./data/database.json"))

def translate(p):
    p = p.lower()
    if p in db:
        return db[p]
    elif len(get_close_matches(p, db.keys(), cutoff=0.8)) > 0:
        closematch = get_close_matches(p, db.keys())[0]
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % closematch)
        if yn == "Y":
            return db[closematch]
        else:
            return "The word is not in the database."
    else:
        return "The word is not in the database."


print("Welcome! This is a simple english dictionary.")
quit_app = False
while quit_app == False:
    word = input("Please enter an english word to get it's meaning: ")
    res = translate(word)
    if type(res) == list:
        for r in res:
            print(r)
    else:
        print(res)

    print()
    translate_another_word = input("Do you want to translate another word? Enter Y if yes, or N if no: ")
    if translate_another_word.lower() == "n":
        print("Quitting Application.")
        quit_app = True
