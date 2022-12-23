temp = 0
i=0
j=0
k=0
l=0

print("입력\n")
a=input()
strlen = len(a)

while(j < strlen-1):
    if (a[j] == '\0'):
        break
    j+=1
    print("%d "%(ord(a[j])))

print("\n")
print("+3한수\n")

while(i < strlen-1):
    if (a[i] == '\0'):
        break
    i+=1
    print("%d "%(ord(a[i]) + 3))

print("\n")
print("소문자일경우 대문자로 변경\n")
while(k < strlen-1):
    if (a[k] == '\0'):
        break

    if (a[k] >= chr(97) and a[k] <= chr(122)):
        print("%c "%chr(ord(a[k])-32))
    else:
        print("%c "%chr(ord(a[k])))
    k+=1

print("\n")
print("나만의 암호\n")
while(l < strlen-1):
    if (a[l] == '\0'):
        break

    if (ord(a[l - 1]) == 32):

        if (a[l] >= chr(65) and a[l] <= chr(92)):

            print("%d "%(ord(a[l]) + 30))
        if (a[l] >= chr(93) and a[l] <= chr(122)):
            print("%d "%(ord(a[l]) + 30))

    if (ord(a[l + 1]) == '\0'):
        print("%d ", a[0])
    else:
        if (a[l] >= chr(65) and a[l] <= chr(92)):
            print("%d "%(ord(a[l + 1]) + 30))
        if (a[l] >= chr(93) and a[l] <= chr(122)):
            print("%d "%(ord(a[l + 1]) + 30))
    l+=1
