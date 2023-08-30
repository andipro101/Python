#Hangman Game: Implement a text-based version of the classic hangman game. The program should choose a word randomly, and the player tries to guess the letters to complete the word.

import random

underscore = 0
strike = 0
underlist = []
wrongletters =[]
Matched_Letters = []
game_over = False

while not game_over == True: 

    #choose random word from list
    ListWords = ["monkey","Dog","Cat","ground","sow","limit","decrease","engine","comment","donor","aluminium","financial","cheque","commemorate","laser","parachute","sample","castle",'excess', 'jurisdiction', 'union', 'morsel', 'repetition', 'command', 'elbow', 'coast', 'pipe', 'pillow', 'time', 'friend', 'shock', 'corpse', 'diplomatic']
    Word = (random.choice(ListWords))
    lenght = (len(Word))


    #make as many underscores as there are letters
    while underscore < lenght:
        
        underscore = underscore + 1
        underlist.append("_")


    print ("Guess the Word:")

    #type the word letter by letter in the list
    WordLetters = (list(Word))

    #count the lenght of the letters
    length = len(WordLetters)



    while "_" in underlist:
        if strike >= 1:
            print ("this are your wrong letters" + str(wrongletters))
        print(*underlist)
        Letter = input ("Guess a letter: ")
        print ("\n")


        #find the matched letter position in the list
        for i in range(length):
            if Letter == WordLetters[i]:
                Matched_Letters.append(i)



        #replace the _ with the guessed letter
        if Letter in Word:
            for index in Matched_Letters:
                underlist[index] = Letter 
        
        Matched_Letters = []
        
        if "_" not in underlist:
            print ("you won")       


        elif Letter not in WordLetters:
            wrongletters += Letter
            strike += 1
            print ("Wrong mistake: " + str(strike))
            if strike == 8:
                print("Game Over")
                game_over = True
                break
            
    if game_over == True:
        print("The word was-",Word)
        restart = input("Type Yes to restart:")
        if restart == "Yes":
            underscore = 0
            strike = 0
            underlist = []
            wrongletters =[]
            Matched_Letters = []
            game_over = False

