def mutate_string(string, position, character):
    mystr= string[:position]+character+string[position+1:]
    return mystr
