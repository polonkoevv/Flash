f = open('easyone.txt')
s = f.read()
c = 0
k = 0
for i in range(0,len(s)-5,6):
	a = int(s[i]+s[i+1]+s[i+2]+s[i+3]+s[i+4]+s[i+5]) 
	if (a > 242795 and a <= 389459) or (a >= 550187 and a < 889151 ):
		k += 1
		c = c + a
c = c // 1000000
print(min(c,k),max(c,k))