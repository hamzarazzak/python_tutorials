import random

print "\tWelcome to 'Guess My Number'!"
print "\nI'm thinking of a number between 1 and 100."
print "Try to guess it in as few attempts as possible.\n"

# set the initial values
the_number = random.randrange(100) + 1
guess = int(raw_input("Take a guess: "))
tries = 2

# guess/tries remaining loop
while (guess != the_number) and tries >0:
    if (guess > the_number):
        print "Lower..."
    else:
        print "Higher..."
            
    guess = int(raw_input("Take a guess: "))
    tries -= 1

if tries == 0:
    print "You lose, you have run out of guesses!"
else:
    print "You win, the number was", the_number
  
raw_input("\n\nPress the enter key to exit.")