print "This program will calculate your age."

born = int(raw_input("What year where you born?\n"))
#This specifies the variable 'born', and classifies it as a interger, allowing it to be calculated in the 'age' equation.

year = int(raw_input("What's the current year?\n"))
#This specifies the variable 'year', essentially doing the same thing as the code above, just specifying a different variable.

age = year - born
#Tells the program that 'year' minus 'born' equals the variable 'age'.

print "So you where born in %r?" % born
print "And the current year is %r?" % year
print "That would mean you're %r!" % age
#Basically puts the defined variables into strings.

#Runs the variable 'age' through the if then statement, testing to see if it is greater than or equal to 18, and then running a line, and, at the same time, running another line if the requirements aren't met to run the first line.
#\/\/\/\/\/\/
if age >= 18:
    print "You're an adult, aren't you?"
else:
    print "Don't worry, you'll be 18 in %r years." % (18 - age)
    #Calculates how many years until you're 18, then inserts it into the string.