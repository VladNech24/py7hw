fizz = int(input())
buzz = int(input())
a = int(input())
i = []
for a in range(a):
    a=(a+1)

    if a%fizz and not a%buzz:
        i.append("B")
    elif a%buzz and not a%fizz:
        i.append("F")
    elif a%fizz!=0 and a%buzz != 0:
        i.append(a)
    elif fizz%a and buzz%a:
        i.append("FB")
print (i)
