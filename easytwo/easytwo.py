f = open('easytwo.txt')
s = f.read()

m = 'SosoPavliashvili'

k = 0
m = s.find(m)
for i in range(0,m):
	if s[i] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
		k += 1
print(k//2 + 1)
