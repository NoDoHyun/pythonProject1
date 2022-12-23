i=j=k=num=0
a=(input())
b=list(a)
c=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
d=[' ']
for i in b:
    for j in c:
        if i==j:
            for k in d:
                if(k==j):
                    num=1
            if(num==0):
                print(i, end=' : ')
                print("인덱스",b.index(i), end=' ')
                print("카운트",b.count(i))
                d+=i
            else:
                num=0
                continue


