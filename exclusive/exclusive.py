f = open('exclusive.txt')
s = f.read()
a = []
for i in range(len(s)):
	if not(s[i] in a):
		a.append(s[i])
		a.append(s.count(s[i]))
	if len(a) == 6:
		break


mz = a[1] + a[3] + a[5] - max(a[1],a[3],a[5]) - min(a[1],a[3],a[5])

print(a[a.index(mz)-1],mz)