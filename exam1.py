### This program is a simple examp program which asks users certain questions and 
### base on the replies , marks are alloted.
from sys import argv
import random

#script report = argv

def random_number(number):
	number = random.randint(1, number)
	return number

def test1():
	points_earned = 0
	upperbound = 1000
	n1 = random.randint(1, 1000)
	s1 = "%d is a Even or Odd Number(Type \'even\' | \'odd\'): ?" %n1
	print s1
	answer = raw_input("> ")
	result = even_odd_number(n1)
	if result == answer:
		points_earned = points_earned + 1
	else:
		points_earned = points_earned - 1
		
	report = s1 + answer 
	return report, points_earned

	


def even_odd_number(number):
	if number % 2 == 0:
		return 'even'
	else:
		return 'odd'

	
print """
This is a simple test, where you will be asked simple
questions regarding mathematics.
"""

check = raw_input("Ready to take: (y/n)")
if check == 'y':
	output = test1()
	print output
else:
	print "Thanks"

