import random
a=0
c=0
i=0
j=0
k=0

num=28
students=['민영','연재','기태','명은','성일','연수','재일','도현','가미','규환','성빈','시형','의용','송화',
          '범규','보라','소윤','여름','지혜','현도','성경','영효','홍선','은희','연우','철우','민석','지혁']

while i!=2:
    b = random.randrange(1, num)
    if b!=c:
        print("분리수거", end=' : ')
        print(students[b])
        c=i
        del students[b]
        i+=1
        num-=1
    else:
        print("중복제거")
        continue
while j!=1:
    b = random.randrange(1, num)
    if b!=c:
        print("쓸기", end=' : ')
        print(students[b])
        c=j
        del students[b]
        j+=1
        num-=1
    else:
        print("중복제거")
        continue
while k!=1:
    b = random.randrange(1, num)
    if b!=c:
        print("닦기", end=' : ')
        print(students[b])
        c=k
        del students[b]
        k+=1
        num-=1
    else:
        print("중복제거")
        continue




