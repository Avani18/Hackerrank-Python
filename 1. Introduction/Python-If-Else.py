import sys

number= sys.stdin.readline()
number.strip()
number= int(number)

if number%2!=0:
    print("Weird")
elif (number%2==0 and (number>=2 and number<=5)):
    print("Not Weird")
elif (number%2==0 and (number>=6 and number<=20)):
    print("Weird")
elif(number%2==0 and (number>20 and number<=100)):
    print("Not Weird")

