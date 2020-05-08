def minion_game(string):

    #Works for 6 test cases
    '''all_substrings = [string[x:y] for x, y in combinations(range(len(string) + 1), r = 2)]
    kevin = 0
    stuart = 0
    for i in range(len(all_substrings)):
        if (all_substrings[i].startswith(('A','E','I','O','U'))):
            kevin += 1
        else:
            stuart += 1

    if (stuart > kevin):
        print ('Stuart', str(stuart))
    elif (kevin > stuart):
        print ("Kevin", str(kevin))
    else:
        print ("Draw")'''

    #Works for all test cases
    vowels = 'AEIOU'
    kevin = 0
    stuart = 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevin += (len(string)-i)
        else:
            stuart += (len(string)-i)

    if kevin > stuart:
        print ("Kevin", kevin)
    elif (kevin < stuart):
        print ("Stuart", stuart)
    else:
        print ("Draw")

if __name__ == '__main__':

	s = input()
    minion_game(s)
