##******************
## Elements Quiz
## Developed by: Ian Johnson
## Version 1.8
##
## Purpose:
## To choose an element at random from a table and ask the user for the opposite sign
##******************

import random   ##allows us to randomly choose items later on in the code

##creates the variables that will be used later on
score = 0
q = 0
run = 0
x = 0
att = 0
scores = []

##Welcomes user to the program and explains the basic instructions on how to use the software
print "Welcome to the Elements Study Help!\nThis is a tool designed to help you study the Periodic Table of Elements.\nThe program will choose either a symbol or an elements name and you must provide the matching symbol or name.\nGood luck!\n(When your done, type 'done' for your answer and the your score will appear.)\n"

##creates a loop to generate the questions
while (run != 1):

    ##Creates a table that will store all the possible element symbol/name pairs
    elemtab = ['H', 'Hydrogen',
               'He', 'Helium',
               'Li', 'Lithium',
               'Be', 'Beryllium',
               'B', 'Boron',
               'C', 'Carbon',
               'N', 'Nitrogen',
               'O', 'Oxygen',
               'F', 'Flourine',
               'Ne', 'Neon',
               'Na', 'Sodium',
               'Mg', 'Magnesium',
               'Al', 'Aluminum',
               'Si', 'Silicon',
               'P', 'Phosphorus',
               'S', 'Sulfur',
               'Cl', 'Chlorine',
               'Ar', 'Argon',
               'K', 'Potassium',
               'Ca', 'Calcium',
               'Cr', 'Chromium',
               'Mo', 'Molybdenum',
               'W', 'Tungsten',
               'Mn','Maganese',
               'Rb', 'Rubidium', 
               'Sr', 'Strongtium',
               'Cs', 'Cesium',
               'Ba', 'Barium',
               'Fr', 'Francium',
               'Ra', 'Radium',
               'Fe', 'Iron',
               'Co', 'Cobalt',
               'Ni', 'Nickel',
               'Cu', 'Copper',
               'Zn', 'Zinc',
               'Ag', 'Silver',
               'Au', 'Gold',
               'Cd', 'Cadium',
               'Hg', 'Mercury',
               'Ga', 'Gallium',
               'Ge', 'Germanium',
               'As', 'Arsenic',
               'Se', 'Selenium',
               'Br', 'Bromine',
               'Kr','Kryton',
               'I', 'Iodine',
               'Xe', 'Xenon',
               'Rn', 'Radon',
               'Pb', 'Lead',
               'Sn', 'Tin',
               'Sb', 'Antimony',
               'Te', 'Tellurium',
               'At', 'Astatine',
               'U', 'Uranium',
               'Bi', 'Bismuth']

    ##This is the block of code that ends the quiz
    if q == 50:   ##checks question number, and if the question is #5, it runs this code
        att = att + 1   ##adds 1 to the number of attempts
        fscore = score, 'out of', q   ##creates a new variable for the final score
        atempt = 'Atempt', att   ##creates a new variable for the number of attempts
        scores.append(atempt)   ##adds the new attempts variable to a table
        
        scores.append(fscore)   ##adds the new final score variable to the same table
        for s in scores:
            print s   ##lists every entery in the scores table
        print ""   ##adds blank line before startin code again
        q = 0   ##resets the question number to 0
        score = 0   ##resets score to 0

    q = q + 1 ##adds 1 to the question number
    
    x = random.randint(0,109) ##randomly chooses an entery from the table of element names/symbols
 
    print 'Question', q   ##tells the user what question they are on
    
    ans = raw_input (elemtab[x])   ##shows the user the entry from the table and saves their input

    if ans == 'done':   ##if user enters 'done' for answer, this code will run
        print score, 'out of', q - 1   ##shows the user their final score
 ##       print score/100
        run = 1   ##sets run to 1, which kills the while loop

    elif x == 0:   ##if the program chose the first entry from the table, this code runs
        if ans == 'Hydrogen':   ##checks the users answer
            print 'Correct\n'   ## and prints 'correct' if the answers match

            score = score + 1   ##adds 1 to the score

    elif x % 2 == 0:   ##if the value the computer chose is even, this code runs         

        correctelem = elemtab[x + 1]   ##determines which entery matches the entery chosen earlier
        
        if ans == correctelem:   ##compares the correct entery with the user's input
            print 'Correct\n'   ##prints 'correct' if the answers match

            score = score + 1   ##adds 1 to the score

        else:   ##this code runs if the user got the answer wrong
            print 'Wrong'   ##tells the user that their answer was wrong
            print 'You said:', ans   ##tells the user what they put
            print 'Correct answer:', correctelem, '\n'   ##tells the user the correct answer so that they learn for next time

    else:
    
        correctelem = elemtab[x - 1]
    
        if ans == correctelem:
            print 'Correct\n'

            score = score + 1

        else:
            print 'Wrong\n'
            print 'You said:', ans
            print 'Correct answer:', correctelem, '\n'
