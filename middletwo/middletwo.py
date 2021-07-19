f = open('middletwo.txt')
s = f.read()
# Максимальное кол-во машин между Vaz2107, включая Vaz2107


a = []
d = 0
maxd = 0
crd = []

for i in range(0,len(s)):
	if s[i] == 'V' and s[i+6] == '7':#Ищем на каком по счету символу( отсчет ведется с нуля) находятся Vaz2107
		a.append(i)
print(a)

for i in range(0,len(a)-1):
	q = 0
	for k in range(int(a[i]),int(a[i+1])+1):
		if s[k] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
			q += 1
	if q >= maxd:
		maxd = q
		crd = []
		crd.append(a[i])
		crd.append(a[i+1])
print(maxd,crd)