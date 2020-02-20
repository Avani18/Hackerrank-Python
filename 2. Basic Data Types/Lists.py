if __name__ == '__main__':
    N = int(input())
    mylist=[]
    for i in range(0,N):
        str= input().split()
        if(str[0]=='insert'):
            mylist.insert(int(str[1]),int(str[2]))
        if(str[0] == "print"):
            print(mylist)
        if (str[0]=='append'):
            mylist.append(int(str[1]))
        if(str[0]=='remove'):
            mylist.remove(int(str[1]))
        if(str[0]=='sort'):
            mylist.sort()
        if(str[0]=='pop'):
            if len(mylist)!=0:
                mylist.pop()
        if(str[0]=='reverse'):
            mylist.reverse()



