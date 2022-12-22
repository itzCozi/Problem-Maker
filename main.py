# Makes hard math problems (ik there's a bug that's the point)

# Imports
import random
import time

# Vars
operatorlist = ['-', '/', '*', '+']
int1_2 = random.randint(1, 2)
int1_3 = random.randint(1, 3)
int1_5 = random.randint(1, 5)
int1_10 = random.randint(1, 10)
int1_50 = random.randint(1, 50)
int20_100 = random.randint(20, 100)

# Fuctions
def make_A(int):
	intstage1 = int - int1_10
	intstage2 = intstage1 + int1_5
	oneORtwo = random.randint(1, 2)
	if oneORtwo == 1:
		intstage3 = intstage2 - int1_50
		return intstage3
	if oneORtwo == 2:
		intstage3 = intstage2 + int1_50
		return intstage3
	else:
		print("Code fucked up...")
		time.sleep(2)
		quit()

def make_B(int):
	intstage1 = int / int1_5
	intstage2 = intstage1 + int1_50
	oneORtwo = random.randint(1, 3)
	if oneORtwo == 1:
		intstage3 = intstage2 - int1_50
		return intstage3
	if oneORtwo == 2:
		intstage3 = intstage2 + int1_50
		return intstage3
	if oneORtwo == 3:
		intstage3 = intstage2 * int1_2
		return intstage3
	else:
		print("Code fucked up...")
		time.sleep(2)
		quit()

def make_C(int):
	intstage1 = int * int1_3
	intstage2 = intstage1 - int1_50
	oneORtwo = random.randint(1, 3)
	if oneORtwo == 1:
		intstage3 = intstage2 - int1_50
		return intstage3
	if oneORtwo == 2:
		intstage3 = intstage2 + int1_50
		return intstage3
	if oneORtwo == 3:
		intstage3 = intstage2 / int1_2
		return intstage3
	else:
		print("Code fucked up...")
		time.sleep(2)
		quit()


# Main
def main():
	randop1 = random.choice(operatorlist)
	randop2 = random.choice(operatorlist)
	randop3 = random.choice(operatorlist)
	print('A = ' + str(make_A(int20_100)))
	print('B = ' + str(make_B(int20_100)))
	print('C = ' + str(make_C(int20_100)))
	A = make_A(int20_100)
	B = make_B(int20_100)
	C = make_C(int20_100)
	x = A + B + C
	z = B * C - A
	y = C + B * A
	m = B + A - C
	print(str(x) + ' ' + randop1 + ' ' + str(y) + ' ' + randop2 + ' ' + str(z) + ' ' + randop3 + ' ' + str(m) + ' = ?')
	time.sleep(5)
	reveal_ans = input("Reveal Answer? ")
	if reveal_ans == "y":
		print('X' + " = A + B + C")
		print('Y' + " = B * C - A")
		print('Z' + " = C + B * A")
		print('M' + " = B + A - C")
		time.sleep(5)
	if reveal_ans == "n":
		time.sleep(100)
	else:
		print("Invaild")
		time.sleep(2)
		quit()

# Call to
main()

