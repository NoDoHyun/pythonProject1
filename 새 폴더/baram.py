a = int(input())
b = 0
c = 1
d = a
e=a
while a >= 0:
        while b < e:
                while c < e:
                        while d > 0:
                                print(" "*b+"*"*a+" "*d+"*"*c)
                                a -= 1
                                b += 1
                                c += 1
                                d -= 1
        a = e
        b = 0
        c = 1
        d = e
        while a+2 >= 0:
                while b < e:
                        while c < e:
                                while d > 0:
                                        print("*"*a+" "*b+"*"*c+" "*d)
                                        a -= 1
                                        b += 1
                                        c += 1
                                        d -= 1