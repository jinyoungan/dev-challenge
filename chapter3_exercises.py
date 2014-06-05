# Exercises for chapter 3:

# Name: JIN YOUNG AN

#3.1 NameError: name 'repeat_lyrics' is not defined

#3.2 SyntaxError: invalid syntax

#3.3
def right_justify(s):
	print " " * (70 - len(s)) + s
right_justify('allen')

#3.4.1
def do_twice(f):
	f()
	f()

def print_spam():
	print 'spam'

do_twice(print_spam)

#3.4.2
def do_twice(f, ham):
	f(ham)
	f(ham)

#3.4.3
def print_twice(ham):
	print ham
	print ham

#3.4.4
do_twice(print_twice, 'spam')

#3.4.5
def do_four(a, meat):
	a(meat)
	a(meat)

do_four(print_twice, 'meat')
