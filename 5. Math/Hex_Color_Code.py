import re, sys
[print(j) for i in sys.stdin for j in re.findall('[\s:](#[a-f0-9]{6}|#[a-f0-9]{3})', i, re.I)]

#sys.stdin reads all the lines till it encounters the end of input
#re.findall finds all the occurences of the Regex in input line 
#[\s:] means that the pattern should start with either a space or colon
#[a-f0-9]{6} this is the main Regex of length 6 or 3
#re.I is used to ignore case
