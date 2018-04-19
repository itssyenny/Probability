import random

def randomize( nrand ):
	n_inside = 0
	min = -1
	max = 1

	for nloops in range(1, nrand):
		xrand = random.randint(min, max)*2 - 1
		yrand = random.randint(min, max)*2 - 1

		#find its distance from origin
		rrand = math.sqrt(math.pow(2,xrand) + math.pow(2,yrand))
		
		#it falls inside the circle
		if rrand <= 1:
			n_inside += 1
		#end
	#end
	phi = (4 * n_inside)/nrand
	print phi
	return

#Call the random function
nrand = 4
randomize(nrand)
