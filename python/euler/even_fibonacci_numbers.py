dic = {}


def fib(n):
    global dic
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n in dic:
        return dic[n]
    else:
        tmp = fib(n-1) + fib(n-2)
        dic[n] = tmp
        return tmp

i = 1
s = 0
while True:
    if fib(i) >= 4000000:
        break
    else:
        if fib(i) % 2 == 0:
            s += fib(i)
    i += 1
print s
