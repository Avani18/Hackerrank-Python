import re

def validRegexCheck(regex):
    try:
        re.compile(regex)
    except re.error:
        return False
    return True

for _ in range(int(input())):
    print (validRegexCheck(input()))
