def print_formatted(number):
    length= len(bin(number))-2
    for i in range(1,number+1):
        print (str(i).rjust(length), end=' ')
        print (str(oct(i)).lstrip('0o').rjust(length), end=' ')
        print (str(hex(i)).lstrip('0x').upper().rjust(length), end=' ')
        print (str(bin(i)).lstrip('0b').rjust(length), end=' ')
        print ('')
