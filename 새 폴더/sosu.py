def primenumber(a):
    turn = 0
    i=1
    print(a)
    while(i <= a):
        if (a % i == 0 and i != a and i != 1):
            print("%d" %i)
            turn+=1
        i+=1

    if (turn > 0):
        print("no")
    if (turn == 0):
        print("yes")

a=int(input())
primenumber(a)
