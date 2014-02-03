
res = 0
for i in range(3, 1000, 3):
    res += i

for i in range(5, 1000, 5):
    if i % 3 > 0:
        res += i

print res
