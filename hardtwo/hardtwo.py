f = open('hardtwo.txt')

d = ['I','V','X','L','C','D','M']
dd = [1,5,10,50,100,500,1000]

cp = [] # Будут указываться римские числа строки
cpd = [] # Будут указываться десятичные значения римских чисел строки
gcp = '' # Будут обозначаться максимальные римские числа строк


for s in f:
	s = s[:-1]
	for i in range(0,len(s)-1):
		if s[i]+s[i+1] not in ['LL','VV','DD']:
			cp.append(s[i]+s[i+1])

		if dd[d.index(s[i])] < dd[d.index(s[i+1])]:
			cpd.append(dd[d.index(s[i+1])]-dd[d.index(s[i])])
		else:
			cpd.append(dd[d.index(s[i+1])]+dd[d.index(s[i])])
	m = max(cpd)
	gcp += (cp[cpd.index(m)])
	cp,cpd = [],[]

print(gcp)
