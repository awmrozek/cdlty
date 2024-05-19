from collections import *
import sys
itr = (line for line in sys.stdin.read().split())
INP = lambda: next(itr)

# Returns next integer from STDIN
def ni(): return INP()

# Returns next line
def nl(): return [_ for _ in INP().split()]

N=int(ni())
rf = float(ni())
rm = float(ni())

# d = distance between center points
def radical_len(d, r, R):
	return ((-d+r-R)*(-d-r+R)*(-d+r+R)*(d+r+R))**0.5/d

class Cat(list):
	def __init__(self, s, x, y):
		self.append(s)
		self.append(x)
		self.append(y)
	def get_sex(self):
		return self[0]
	def get_x(self):
		return self[1]
	def get_y(self):
		return self[2]
	def __str__(self):
		return s, x, y

cats = []

for i in range(0, N):
	sex = ni()
	x = int(ni())
	y = int(ni())

	cats.append(Cat(sex, x, y))

for cat1 in cats:
	for cat2 in cats:
		if cat1.get_sex() == "M":
			r1 = rm
		else:
			r1 = rf

		if cat2.get_sex() == "M":
			r2 = rm
		else:
			r2 = rf

		d = ((cat1.get_x() - cat2.get_x())**2 + \
			(cat1.get_y() - cat2.get_y()) ** 2) ** 0.5
		if d == 0:
			continue
		
		print(f"{d} {r1} {r2} Radical len: {radical_len(d, r1, r2)}")
		radical = radical_len(d, r1, r2)
		h = radical/2

		
