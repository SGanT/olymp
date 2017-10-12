import re

def pointer(string):
    string = str(string)[::-1]
    splitted = re.split("(\d\d\d)",  string)
    final = [x for x in splitted if x is not '']
    return ".".join(final)[::-1]

print pointer( raw_input("Your number ->") )
