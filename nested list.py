
dict1 = {}    
for _ in range(int(input())):
    name = input()
    score = float(input())
    dict1[name] = score
a = list(dict1.items())
a.sort()
print (a)
b = []
y  = list(dict1.values())
y = set(y)
y = list(y)
y.sort(reverse = True)
print(y)    
    
z = y.pop(-2)
print(z)
for i in range(len(a)):
    if (a[i][1] == z):
        b.append(a[i][0])
b.sort()
for i in b:
    print(i)
