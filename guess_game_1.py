(input('Pick a number between 0 and 100, ready?')) #press enter to begin
e = 1 #epsilon
num_guess = 0 #guess counter
low = 0
high = 100
guess = int(round((high + low)/2)) #guesses are rounded to nearest whole number, take the half of the low to hind bounds
a = 0 #check that will break while loop
while a != 1:
    h = input('Is your number ' + str(guess) + '? (y/n): ')
    if h == 'n': #wanted to include or 'N' in case they put a capital n
        b = 0 
        while b != 1:
            r = input('Is it less than or more than ' + str(guess) + '? (l/m): ')
            if r == 'l':
                high = guess
                b = 1
            elif r == 'm':
                low = guess
                b = 1 #breaks while loop
            else:
                print('Invalid input, try again.') #I want this statement to go back to line 11, not line 9 
    elif h == 'y':
        a = 1 #ends the while loop, wanted to use break, but then I wouldn't have a statement to use while loop continuously, help?
    else:
        print('Invalid input, try again.')
        num_guess -= 1 #reduces guess count so that invalid inputs don't count
    num_guess += 1
    guess = round((high + low)/2)
if num_guess == 1:
    t = "try" #grammar
else:
    t = "tries"
print("Hurray! I guessed your number was " + str(guess) + " in " + str(num_guess) + " " + str(t) + "!")