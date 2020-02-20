if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    mylist = list(arr)
    mylist.sort()
    max= mylist[n-1]
    while(mylist[n-1]==max):
        mylist.pop()
        n-=1
    print(mylist[-1])


