
# ТЗ максимальное колво подряд идущих возрастсающих по длине цепочек состоящих из восходящих символов

f = open('hardtwo.txt')
s = f.read()
s = '807FF43E0FAC965D35F2B0FB5363EC672C95D650'

a = s
d = []
kl = 1
mkl = 1
j = a[0]

for i in range(1,len(a)):
	if a[i-1] < a[i]:
		j += a[i]
	else:
		d.append([i-len(j),i-1,len(j),j])
		j = a[i]

d.append([i-len(j)+1,i,len(j)])



for i in range(len(d)-1):
	if (d[i][2] < d[(i+1)][2]) and (d[i][1] + 1 == d[(i+1)][0]):
		kl += 1
	else:
		mkl = max(mkl,kl)
		kl = 1
mkl = max(mkl,kl)
print(mkl)





