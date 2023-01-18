import math
pi = math.pi
roundto = int(input('Choose Digit from 1-10: '))
if roundto in range(1,10):
	roundpi = round(pi,roundto)
	print(roundpi)