def gcd(a, b):
	if a%b==0:
		return b
	return findGcd(b, a%b)

def exEuclid(a, b):
	if gcd(a, b) != 1:
		print('inverse doesnt exist')
	else:
		