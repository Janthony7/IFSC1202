#Example 1
a = [1, 2, 3, 4]
b = [5, 6]
c = [7, 8, 9]
d = []
d.append(a)
d.append(b)
d.append(c)
print (d)
print(d[0])
print(d[1])
print(d[2])
print(d[0][0])
print(d[0][1])
print(d[0][2])
print(d[0][3])
print(d[1][0])
print(d[1][1])
print(d[2][0])
print(d[2][1])
print(d[2][2])
d[0][0] = 10
d[0][1] = 11
d[0][2] = 12
d[0][3] = 13
print(d[0][0])
print(d[0][1])
print(d[0][2])
print(d)