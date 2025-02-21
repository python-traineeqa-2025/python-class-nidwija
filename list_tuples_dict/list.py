#ordered, mutable
a=[1,2,3,4,1,1,1,1]
print(a[1])
print(len(a))
a.append(10)
print(a)
a.insert(1,9)
print(a)
a.insert(3,'ram')
print(a)
print(a.count(1))
print(a.reverse())

#sort
#sorted
# a.sort()
# d=sorted(a)

a=[1,4,5,6,7]
a[2]='ram'
print(a)