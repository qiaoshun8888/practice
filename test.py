height = 4
width = 5

hdic = {}
vdic = {}
ldic = {}
rdic = {}
for i in range(height):
    for j in range(width):
        if i in hdic:
            hdic[i].append((i, j))
        else:
            hdic[i] = [(i, j)]

        if j in vdic:
            vdic[j].append((i, j))
        else:
            vdic[j] = [(i, j)]

        if i - j in ldic:
            ldic[i - j].append((i, j))
        else:
            ldic[i - j] = [(i, j)]

        if j + i - height in rdic:
            rdic[j + i - height].append((i, j))
        else:
            rdic[j + i - height] = [(i, j)]

result = hdic.values()
result.extend(vdic.values())
result.extend(ldic.values())
result.extend(rdic.values())
# for i in result:
#     print i


ox_list = ['x', 'x', 'x', 'x', 'o']
c = 0
result = []
head_cut = True
for i in ox_list:
    if i == 'x':
        c += 1
    elif not i:
        if c > 0:
            result.append(c)
        head_cut = False
        c = 0
    else:
        if not head_cut or c >= 4:
            result.append(c)
        c = 0
if (c > 0 and not head_cut) or c >= 4:
    result.append(c)
# print result
print result
