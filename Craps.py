import random

class Die(object):
	def __init__(self,num_sides = 6):
		self.num_sides = num_sides
		self.face_up = random.randint(1,self.num_sides)

	def roll(self):
		self.face_up = random.randint(1,self.num_sides)
		return self.face_up

	def __str__(self):
		return str(self.face_up)


class Craps (object):
	def __init__(self):
		self.d1 = Die()
		self.d2 = Die()

	def play(self):
		winner = True
		v1 = self.d1.roll()
		v2 = self.d2.roll()
		sum_die1 = v1 + v2


		if (sum_die1 in [7,11]):
			winner = True
			print(str(v1) + '+' + str(v2) + '=' + str(sum_die1))
		elif (sum_die1 in [2,3,12]):
			winner =  False
			print(str(v1) + '+' + str(v2) + '=' + str(sum_die1))
		else:
			print(str(v1) + '+' + str(v2) + '=' + str(sum_die1))
			sum_die2 = 0
			play_on = True
			while play_on:
				v1 = self.d1.roll()
				v2 = self.d2.roll()
				sum_die2 = v1 + v2
				print(str(v1) + '+' + str(v2) + '=' + str(sum_die2))

				if sum_die1 == sum_die2:
					winner = True
					break
				elif(sum_die2 == 7):
					play_on = False
					winner = False
					break
				else:
					play_on =True
					

		return winner



def main():

	num_players = int(input("Please enter the number of players:"))

	game = 	Craps()

	for i in range (0,num_players):
		if game.play():
			print ('Player',str(i+1),"wins")
		else:
			print('Player',str(i+1),"loses")

main()