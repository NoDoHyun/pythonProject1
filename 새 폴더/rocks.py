import random
list=['x','x','x','x','x']
num=2
select=0
while(1):
    select1 = (int(input("1.가위,2.바위,3.보")))
    select2 = (int(input("1.가위,2.바위,3.보")))
    if(select1==1 and select2==2):
        select=2
    if(select1==1 and select2==3):
        select=1
    if(select1==select2):
        print("무승부")
        continue
    if(select1==2 and select2==1):
        select=1
    if(select1==2 and select2==3):
        select=2
    if(select1 == select2):
        print("무승부")
        continue
    if(select1==3 and select2==1):
        select=2
    if(select1==3 and select2==2):
        select=1
    if(select1 == select2):
        print("무승부")
        continue
    if(select==1 and num==4):
        print("1win")
        break
    if(select==2 and num==0):
        print("2win")
        break
    if(select==1):
        num+=1
        list[num]='o'
        list[num-1]='x'
    if(select==2):
        num-=1
        list[num]='o'
        list[num+1]='x'
    print(list)
