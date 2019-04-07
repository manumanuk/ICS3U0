#-----------------------------------------------------------------------------
# Name:        Python Assignment 1 (arcadia.py)
# Purpose:     Word and Math Based Functions and Games
#
# Author:      669571
# Created:     29-Mar-19
# Updated:     5-Apr-19
#-----------------------------------------------------------------------------

#Import sleep for use as wait function to show user their answers, and random for use in number guessing game
from time import sleep
import random

def scramble(word):
  '''
  Creates an anagram of a given word, replaces some letters with asterisks, and returns the answer.
  
  Searches through each letter of the word and replaces it with a random letter in the word. Chooses at most 5 random letters to replace with asterisks and does so.

  Parameters
  ----------
  string
    Takes in one word to jumble.
  
  Returns
  -------
  string
    Returns the scrambled string.
  '''
  #Assertions
  assert isinstance(word, str), "scramble function parameter error"

  #Put all the letters of the word into a list
  lettersInWord = list(word)

  #Initialize a variable to count how many letters have been replaced with asterisks so far
  asteriskCount = 0
  #For each letter in the word, pick a random position to move it to. Move the other letter to the open position. Randomly replace some letters with asterisks
  for counter in range (0, len(lettersInWord)):
    #Out of a 50% chance, choose whether or not to add an asterisk
    asterisk = random.randint(0, 1)
    #If the asterisk variable = 1 (which also evaluates to True), and less than letters have been replaced with asterisks so far, replace the letter with an asterisk
    if asterisk and asteriskCount<5:
      lettersInWord[counter] = "*"
      asteriskCount+=1
    #If you cannot add the asterisk:
    else:
      #Find a random letter in the word
      secondLetterIndex = random.randint(0, (len(lettersInWord)-1))
      #Set a variable to hold the current letter we are on (the for loop cycles through all letters in the word from index 0-x)
      firstLetter = lettersInWord[counter]
      #Set a variable to hold the other, random letter
      secondLetter = lettersInWord[secondLetterIndex]
      #Replace the element at the index of the second letter with the first and the first index with the second letter
      lettersInWord[counter] = secondLetter
      lettersInWord[secondLetterIndex] = firstLetter
  #Turn the list back into a string to return the function
  word = ''.join(lettersInWord)
  return word

def wordScrambler():
  '''
  Begins a word scrambling game.
  
  User is prompted to enter words whose letters are then scrambled and then partially replaced with asterisks. The user then guesses each of the words, and earns a score based on their performance.

  Parameters
  ----------
  None
  
  Returns
  -------
  Nothing
  '''
  #Print the instructions
  print('''Welcome to the word Scrambler!
  The objective of this game is to unscramble as many words as you can.
  I will ask you for a number of words, and then scramble their letters, as well as replace some with asterisks.
  Then, I will give you each of them in a random order, and you will have to unscramble them.
  Note: This game is more fun if you use words that are similar in length and letters.
  Try: "Jumping, Running, Walking, Skating"''')
  #Wait 2 seconds for user to see instructions
  sleep(2)

  #Run a continuous while loop which waits until a valid answer has been given
  while True:
    #Ask user how many words to scramble
    numberOfWords = int(input("How many words would you like to scramble? Please enter an answer between 2 and 10. "))
    #Checks if answer is valid. If not, it prints an error message. If it is, program exits the while loop
    if numberOfWords<2 or numberOfWords>10:
      print("You must scramble at least 2 words and at most 10. Please try again.")
    else:
      break
  
  #Creates a list with a number of elements equal to the number of words the user wishes to enter
  wordsToScramble = [" "] * numberOfWords
  #For each word, ask for an input
  for counter in range (0, numberOfWords):
    #Run a continous loop which only exits on valid answers
    while True:
      #Take user input.
      userWord = input("Please enter a word: ")
      if " " in userWord:
        #If input has spaces, tell the user to try again with only one word.
        print("You may not have any spaces in your word. Please try again.")
      elif len(userWord)<=2:
        #If the word is two letters or less, ask the user to enter a longer word which can be accurately scrambled.
        print("Please pick a word longer than 2 letters")
      else:
        #If input is valid, exit loop
        wordsToScramble[counter] = userWord
        break
  
  #Make a new list for scrambled words to parallel the original words
  scrambledWords = [" "]*numberOfWords
  #For each word run the scramble function and enter the scrambled word into the new list
  for index in range (0, numberOfWords):
    scrambledWords [index] = scramble(wordsToScramble[index])

  #Count points, starting at 0
  points = 0
  #For each word, ask the user what word they think it is
  for asking in range (0, numberOfWords):
    #Pick a random word from the list and print it
    randomIndex = random.randint(0, (len(scrambledWords)-1))
    print(scrambledWords.pop(randomIndex))

    #Ask the user what the word was
    ans = input("What word was this (make sure you write the capital letters correctly)? ")
    if ans == wordsToScramble[randomIndex]:
      #Check if the user's answer directly matches the original word. If it does, add a point and display a success message
      points+=1
      print("You guessed it correctly!")
    else:
      #If the word does not match the original, show the user the real word
      print("Whoops. That's not right! This word is: '" + wordsToScramble[randomIndex] + "'.")
    
    #Delete the chosen word from the list
    del wordsToScramble[randomIndex]

    #Display points. If there is only 1 point, use a different display message.
    if points == 1:
      print ("You now have 1 point.")
    else:
      print("You now have " + str(points) + " points.")
    #This for loop will continue until all original words have been asked

  #Display total points at the end of the game. If there is only 1 point, use a different display message.
  if points == 1:
    print("Good game! You earned 1 point.")
  else:
    print("Good game! You earned a total of: " + str(points) + " points.")
  return

def trivia():
  '''
  Begins a trivia game which is 10 questions long.
  
  User is asked 10 trivia questions. Their answers are evaluated against the real ones. If the user is correct, they get 1 point. If not, nothing changes. The total points are displayed at the end of each question and the end of the game.

  Parameters
  ----------
  None
  
  Returns
  -------
  Nothing
  '''
  #Questions list is a multidimensional list which includes 20 questions. Each question is a list whose 0th element contains the question, and the next 4 options contain possible answers
  questionsList = [["Who invented the telephone?", "a) Alexander Graham Bell", "b) Martin Luther King Jr.", "c) Albert Einstein", "d) Edwin Hubble"], ["How many notes are there in a musical octave?", "a) 9", "b) 12", "c) 4", "d) 8"], ["Who was the first person to step foot on the Moon?", "a) Edwin Hubble", "b) Neil Armstrong", "c) Buzz Aldrin", "d) Elon Musk"], ["When did World War I begin?", "a) 1912", "b) 1984", "c) 1914", "d) 1946"], ["What is the fourth element on the Periodic Table of Elements?", "a) Oxygen", "b) Boron", "c) Carbon", "d) Beryllium"], ["What is the capital of Australia?", "a) Sydney", "b) Canberra", "c) Melbourne", "d) Adelaide"], ["Who was one of the winners of the Nobel Prize for Physics in 2018?", "a) Donna Strickland", "b) Elon Musk", "c) Kip Thorne", "d) Stephen Hawking"], ["What is the fourth largest country in the world by land?", "a) China", "b) India", "c) Australia", "d) USA"], ["What does the roman numeral L represent?", "a) 100", "b) 500", "c) 50", "d) 1000"], ["How many valence electrons does Lithium have?", "a) 4", "b) 3", "c) 2", "d) 1"], ["How many tonnes of anthropogenic carbon dioxide are released annually?", "a) 32 megatonnes", "b) 52 gigatonnes", "c) 32 gigatonnes", "d) 52 megatonnes"], ["Where is the smallest bone in the body located?", "a) pinkie", "b) toe", "c) nose", "d) ear"], ["What is the second largest river in the world?", "a) Mackenzie River", "b) The Nile", "c) Amazon River", "d) Yangtze River"], ["What planet in our solar system is closest in size to the Earth?", "a) Mars", "b) Venus", "c) Mercury", "d) Pluto"], ["Who cut Van Gogh's ear?", "a) Van Gogh", "b) Wolfgang Amadeus Mozart", "c) Ross Hickory", "d) Elon Musk"], ["What is the name of the largest functioning rocket on Earth today?", "a) Falcon Heavy", "b) Falcon 9", "c) Delta V", "d) Space Launch System"], ["What is the second smallest country in the world?", "a) Vatican City", "b) Morocco", "c) Madagascar", "d) Rome"], ["What is the largest man-made building in the world?", "a) The CN Tower", "b) The Eiffel Tower", "c) The Burj Khalifa", "d) The Empire State Building"], ["What is the largest known star?", "a) The person reading this", "b) Elon Musk", "c) UY Scuti", "d) VY Canis Majoris"], ["Who is the CEO of Tesla Motors?", "a) Elon Musk", "b) Jeff Bezos", "c) The SEC", "d) Vincent Van Gogh"]]
  #Answers list contains integers which correspond to the index of the correct answer to the nth question from the question list, where n refers to the index of the answers list. The numbering system works such that if the answer is a, the index is 1, if b, it is 2, if c, it is 3, and if d, it is 4.
  answers = [1, 4, 2, 3, 4, 2, 1, 1, 3, 4, 3, 4, 3, 2, 1, 1, 2, 3, 3, 1]

  #Print instructions and wait 2 seconds to begin the game so that users can read
  print("Welcome to trivia! In a few seconds, you will have to answer 10 challenging questions to earn points. Let's begin!")
  sleep(2)

  #Set the initial score to 0
  score = 0
  
  #Count up to 10 questions:
  for counter in range (0, 10):
    #Find a random question. The random value is between 0 and 19 to indicate the indexes of the 20 questions. The counter variable subtracts 1 from this index range each time because an asked question is removed from the list once it has been answered.
    randomIndex = random.randint(0, 19-counter)
    #Print the question and the options for answers
    print(questionsList[randomIndex][0])
    print(questionsList[randomIndex][1])
    print(questionsList[randomIndex][2])
    print(questionsList[randomIndex][3])
    print(questionsList[randomIndex][4])

    #Run a continuous loop which checks for whether or not the user has entered an accurate response
    while True:
      #Ask the user to answer the question with a, b, c, or d
      ans = input("Select either 'a', 'b', 'c', or 'd'. ")
      #Based on what the user enters, give them a number to evaluate against the answers list
      if ans == "a":
        ans = 1
        break
      elif ans == "b":
        ans = 2
        break
      elif ans == "c":
        ans = 3
        break
      elif ans == "d":
        ans = 4
        break
      else:
        #If the user did not enter a, b, c, or d, ask them to enter a valid option
        print("Please choose a valid option. Do not include the bracket in your answer.")

    #Check the answer the user gave. If it is right, add 1 to the score and display a message. If wrong, display the correct answer.
    if ans == answers[randomIndex]:
      print("That is the right answer!")
      score+=1
    else:
      print("Uh oh. The right answer is: " + str(questionsList[randomIndex][answers[randomIndex]]))
    
    #Display the score at the end of each round
    print("Your current score is: " + str(score))

    #Delete the asked question and its corresponding answer from the list
    del questionsList[randomIndex]
    del answers[randomIndex]

    #Wait 1 second before asking the next question
    sleep(1)
  
  #Once 10 questions have been asked, display the final score
  print("Good game. Your final score is: " + str(score))

  #Return statement to exit loop
  return



def pyramidDrawer():
  '''
  Prints a pyramid (equilateral triangle) of desired length.
  
  Asks user for a valid pyramid length, prints asterisks to create a pyramid where the (length of the pyramid) = (height of pyramid)*2. Prints spaces to even out the pyramid.

  Parameters
  ----------
  None
  
  Returns
  -------
  Nothing
  '''
  #Continuously ask a question until it has been answered correctly
  while True:
    #Ask for input betweeen a reasonable size so the pyramid can be viewed
    ans = int(input("Please choose a size for your pyramid between 2 and 15 lines in height: "))
    if ans>15 or ans<2:
      #Check if answer is in valid range. If not, then ask the user to enter a valid size, and repeat the loop
      print("Please enter a valid size and try again.")
    else:
      #If the answer is valid, exit the loop
      break

  #Start a loop to print the asterisks. Each time the loop runs, it will print an individual line, until the height of the pyramid is equal to the input
  for pyramidHeight in range (0, ans):
    #The number of asterisks to be printed will follow the series (1, 3, 5...) where tn = 2n+1, and n is the value of pyramidHeight (term 0 has 1 asterisk)
    numberOfAsterisks = pyramidHeight*2+1
    #To balance the size of the triangle, a number of spaces must be printed to the left of the asterisks which is equal to the height of the pyramid - the line number.
    #The program then prints the number of asterisks as per the line number
    print(" "*(ans-pyramidHeight) + "*"*numberOfAsterisks)
  
  sleep(1)
  return

def checkLetter(givenLetter, givenWord, outputString, triesRemaining):
  '''
  Checks whether a given letter is in a given hangman string and prints a suitable message, as well as changes the score.
  
  Checks whether the guessed letter or its capital letter is in the answer. If it is, change the dashes in the hangman string to respective letters and print the newly decrypted word. If it isn't, the user loses one of their remaining tries.

  Parameters
  ----------
  givenLetter : string
    Letter guessed by the user for hangman.
  givenWord : string
    Word being decrypted by user.
  outputString : string
    Current progress of the user (includes dashes and already-guessed letters)
  triesRemaining : int
    How many of the total of 5 tries the user has already used.
  
  Returns
  -------
  list[int, string]
    Returns the number of tries remaining (out of 5) for hangman game, as well as the new state of the user's progress on guessing the hangman word (outputString).
  '''
  #Assertions
  assert isinstance (givenLetter, str), "checkLetter function parameter error"
  assert isinstance (givenWord, str), "checkLetter function parameter error"
  assert isinstance (outputString, str), "checkLetter function parameter error"
  assert isinstance (triesRemaining, int), "checkLetter function parameter error"

  #Convert the current state of the user's hangman word into a list
  outputString = list(outputString)
  
  #Lists of all capital and lowercase letters in the alphabet.
  letters = list("abcdefghijklmnopqrstuvwxyz")
  capitalLetters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

  #For each letter in the alphabet constant list, check if the guessed letter matches. This is to find the index in the alphabet of the given letter and match it with the capital letter's index
  for alphabetNumber in range (0, 26):
    if letters[alphabetNumber] == givenLetter:
      alphaIndex = alphabetNumber
  
  #letterCount variable tracks how many of the guessed letter is in the word
  letterCount = 0
  #For the length of the word, check each character to see if it matches the guess
  for wordLength in range (0, len(givenWord)):
    #If the letter in the word matches the guess, display this letter in the outputString (progress string) and add 1 to the letter count
    if givenWord[wordLength] == givenLetter:
      outputString[wordLength] = givenWord[wordLength]
      letterCount += 1
    #If the lowercase letter does not conclude any matches, check if the upper case letter in involved by using the index of the letter in the alphabet (which was found earlier) and matching it with the capital letter's index. If a match is found, change the outputString and increase the letter count
    elif givenWord[wordLength] == capitalLetters[alphaIndex]:
      outputString[wordLength] = givenWord[wordLength]
      letterCount += 1
  #Turn the outputString (progress string) back into a string from a list
  outputString = "".join(outputString)

  #If no letters were found, print this and remove 1 from the remaining tries the user has
  if letterCount == 0:
    print("Uh oh. That letter isn't in this word.")
    triesRemaining -= 1
  #If there was a letter found, print the number of letters found. If only 1 was found, print the string in a different way
  elif letterCount == 1:
      print("There is 1 letter '" + givenLetter + "'.")
  else:
    print("There are " + str(letterCount) + " letter '" + givenLetter + "'s.")

  #Return the state of the hangman string and the number of tries the user has remaining
  return [triesRemaining, outputString]


def isLetter(givenLetter):
  '''
  Checks whether a given character is a lowercase letter or not.
  
  Compares the character to every letter in the lowercase alphabet to see if it is a valid letter or not.

  Parameters
  ----------
  givenLetter : string
    Character being checked.
  
  Returns
  -------
  bool
    Returns true or false based on whether the given character is a lowercase letter or not.
  '''
  #Assertions
  assert isinstance (givenLetter, str), "isLetter function parameter error"

  #List constant of letters in the alphabet
  letters = list("abcdefghijklmnopqrstuvwxyz")

  #Sets a bool variable which will be the answer to the function's question: is the character a lowercase letter or not
  ans = False

  #For every letter in the alphabet, check if it matches the given character
  for counter in range (0, len(letters)):
    #If it matches the given character, leave the loop immediately and return the answer to the question as true
    if givenLetter == letters[counter]:
      ans = True
      break
    else:
    #Although the default case is already set as false, this else statement ensures that if the given character does not match any letters in the alphabet, the answer will be false
      ans = False

  return ans

def hangman():
  '''
  Begins a game of hangman (word guessing game).
  
  Picks a random word/phrase from a bank of words and asks user to solve it by displaying the number of characters in the word/phrase using dashes. If the user cannot solve, they have 5 tries to do so by picking letters which they think may be in the word. If the letter is in the word/phrase, those letters are revealed. If not, the user loses a try. If they guess the answer correctly or lose all their tries, the game ends.

  Parameters
  ----------
  None
  
  Returns
  -------
  Nothing
  '''
  #Bank of words and phrases to be used in the game
  phrases = ["Haphazard", "Ontario", "Mississauga", "John Fraser Secondary School", "Antidisestablishmentarianism", "Windmill", "Epic", "Dipole moment", "Haiku", "Kayak", "Music", "Ostracize", "Jealous", "Oxygen", "Encryption", "Blockchain", "Python", "Neptune", "Tesla", "Headphones", "Canada", "The United States of America", "China", "India", "Australia", "Apple", "Microsoft", "Toronto", "Waterloo", "University", "Canoe", "Camping", "Gordon Ramsey"]
  #Prints the instructions to the game and waits to display the word.
  print('''Welcome to hangman! I will pick a word from my dictionary and ask you to guess a letter in the word.
  At the end of every turn, you also have the option of solving the puzzle. If you make 5 errors, you lose! Good luck!''')
  sleep(1)

  #Chooses a random word from the phrases bank, and displays the phrase
  randomIndex = random.randint(0, (len(phrases)-1))
  randomWord = phrases[randomIndex]
  print("Here is your word:")

  #Creates a variable called stringToPrint which represents the current state of the word (including revealed letters)
  stringToPrint = ""

  #For each letter in the phrase, replace it with a dash
  for underscorePrint in range (0, len(randomWord)):
    #If there is a space in the phrase, add the space, not a dash
    if randomWord[underscorePrint] == " ":
      stringToPrint+=" "
    #If the current character is not a space, replace the letter with a dash
    else:
      stringToPrint += "-"

  #Create a list called lettersGuessed to hold previously guessed letters
  lettersGuessed = [""]
  #Create a variable to hold the number of tries remaining
  triesRemaining = 5
  #Create a variable that checks if the game has ended (if puzzle has been solved or failed)
  solvedOrFailed = False
  #As long as there are tries remaining and the puzzle has not been solved or failed, do the following:
  while triesRemaining > 0 and (not solvedOrFailed):
    #Print the current state of the guess (including guessed letters)
    print(stringToPrint)
    #Create a constant loop to look for a valid answer to the question "Would you like to solve the word now?"
    while True:
      #Ask the question
      solve = input('''Would you like to solve the word now?
      1. Yes
      0. No
      ''')
      #If the answer is yes:
      if solve == "1":
        #Ask the user to enter their answer
        ans = input("Enter your answer (make sure it is case-sensitive).")
        #If the user's answer matches the word, display the success message, reiterate the word, and exit the function entirely
        if ans == randomWord:
          print("You did it! The word was " + randomWord)
          return
        #If the user's answer was incorrect, and there is still more than 1 try remaining, remove one try and display an error message
        elif triesRemaining>1:
          triesRemaining-=1
          print("Uh oh. That isn't it.")
        #If the user answered incorrectly and there are no more tries left, subtract one from the remaining number of tries and set the failed variable to true
        else:
          triesRemaining -= 1
          solvedOrFailed = True
        #This break statement exits the while loop which checks for a valid answer to the question "Would you like to solve the word now?"
        break

      #If the user does not want to solve the puzzle yet:
      elif solve == "0":
        #Create a constant loop to check for a valid answer to the letter guess
        while True:
          #Ask the user to guess a letter in the word
          letter = input("Pick a lowercase letter from the alphabet which you think may be in this phrase.")
          #If their input is longer than 1 letter, remind the user they can only pick 1 letter
          if len(letter)>1:
            print("You may only pick one letter. Try again.")
          #Run the isLetter function to check if their entered character is a valid one or not. Display an error message if it is not
          elif not isLetter(letter):
            print("This is not a lowercase letter. You must enter a valid letter. Try again.")
          #If the letter is in the list of already guessed letters, tell the user to enter a unique answer
          elif letter in lettersGuessed:
            print("You have already guessed this letter. Please try again.")
          #If everything is valid, check if the letter is in the word
          else:
            #Add the guessed letter to the list of guessed letters
            lettersGuessed.append(letter)
            #Check if the letter is in the word by calling the function. The function will print the results and return the remaining number of tries as well as the new state of the hangman string
            checkResult = checkLetter(letter, randomWord, stringToPrint, triesRemaining)
            #Put the results from the list into their appropriate variables
            triesRemaining = checkResult[0]
            stringToPrint = checkResult[1]
            #This break statement exits the while True loop waiting for a valid answer to the letter guess
            break
        #This break statement exits the while True loop looking for a valid answer to the question "Would you like to solve the word now?"
        break

      #If the user does not pick yes or no to the question "Would you like to solve the word now?", tell them to try again
      else:
        print("Please choose a valid answer. You must enter either 1 or 0")
    
    #At the end of each round, check if all the letters in the word have been revealed
    if stringToPrint == randomWord:
      #If they have, display a success message, reiterate the word, and set the solved variable to true (to exit the game)
      print("You solved the word!")
      print(randomWord)
      solvedOrFailed = True
    #At the end of the round, check if the user has exhausted all their tries. If they have, end the game by setting the failed variable to true and displaying the correct answer
    elif triesRemaining == 0:
      print("Game over. The answer was '" + str(randomWord) + "'.")
      solvedOrFailed = True
    #At the end of the round, check how many tries are remaining and print the result. If there is only 1 try remaining, print the string differently
    elif triesRemaining == 1:
      print("You have 1 try left")
    else:
      print("You have " + str(triesRemaining) + " tries left.")

  return

def quadraticFormulaCalc():
  '''
  Determines all real roots of a quadratic equation given a, b, and c values of a parabola in the standard form equation: y=ax**2+bx+c.
  
  Asks for input values and rejects them if a is equal to 0 (this is no longer a parabola). Checks if the equation has 1, 2, or 0 roots based on discriminant, and solves for the number of solutions accordingly. Prints the answer.

  Parameters
  ----------
  None
  
  Returns
  -------
  Nothing
  '''
  #Set a loop to continuously ask for input until a valid one has been given
  while True:
    #Get inputs for a, b, and c from user
    aValue = float(input("Please type a value for a: "))
    bValue = float(input("Please type a value for b: "))
    cValue = float(input("Please type a value for c: "))

    if aValue == 0:
      #Check if the a value is valid. If not, ask the user to print a valid one.
      print("Please enter a valid a value. Quadratics require an integer a value.")
    else:
      #Exit the loop if the answer if valid
      break

  #checks if there are real solutions to the formula
  discriminant = bValue*bValue-4*aValue*cValue
  #If there are no roots, print to user
  if discriminant<0:
    print("There are no real solutions to this function")
  #If there is only one real root, print to user after calculating
  elif discriminant==0:
    ans = (-bValue)/(2*aValue)
    print("The only root of this function is " + str(ans))
  #If there are two real roots, print to user after calculating each case (positive and negative)
  else:
    ans = ((-bValue)+discriminant**0.5)/(2*aValue)
    otherAns = ((-bValue)-discriminant**0.5)/(2*aValue)
    print("The two solutions to this function are: " + str(ans) + " and " + str(otherAns))
  return

def guessNumber():
  '''
  Prompts user to think of an integer between 0 and 100 and guesses their answer.
  
  Guesses number between 0 and 100, asking user if this value is correct. If it is incorrect, user is asked whether the guess is higher or lower than the actual number, and sets this as a limit for the next guess, continuing to narrow down the guess. Once the answer is guessed, the function returns. If the number is not guessed, it means the user answered one of the "higher/lower" questions incorrectly, or did not pick a whole number. In this scenario, the function prints a string as an error message to the user, and returns.

  Parameters
  ----------
  None
  
  Returns
  -------
  Nothing
  '''
  #Prompts user to think of a random whole number between 0 and 100
  print("Think of a whole number between 0 and 100")
  #Waits 2 seconds for user to think of a number
  sleep(2)

  #Sets initial values of 3 variables: an upper limit for the guess, a lower limit, and the number of tries it takes to guess the number
  lowerLimit = 0
  upperLimit = 100
  tries = 0

  #Sets a variable which checks whether or not the number has been guessed yet. Runs a while loop until this number is guessed.
  guessing = True
  while guessing:
    #Adds 1 to number of tries
    tries +=1
    #Guesses a random integer between the upper and lower limit, which are initialized at 100 and 0 respectively.
    guess = random.randint(lowerLimit, upperLimit)

    #Sets a variable to check whether a valid answer has been given for the question "Is your number x?" and runs a while loop until this is false
    asking = True
    while asking:
      #Sets the variable to false initially to make the default case a loop exit
      asking = False
      #Asks user if the guess is accurate
      ans = int(input("Is your number " + str(guess) + '''?
      1. Yes
      0. No
      '''))
      if ans == 1:
        #If the guess is accurate, the "guessing" loop is exited by setting the while loop variable to false and printing the answer + the number of tries it took. Uses different print function if only one try has been taken. Uses ' quotations inside print function to print with " quotations.
        if tries == 1:
          print("Yay! I guessed your number. It is: '" + str(guess) + "', and I took " + str(tries) + " try.")
        else:
          print("Yay! I guessed your number. It is: '" + str(guess) + "', and I took " + str(tries) + " tries.")
        guessing = False

      elif ans == 0:
        #If the answer is no, program asks user whether the guess was higher or lower using a while loop
        while True:
          #Asks whether number was higher or lower
          answer = int(input('''Is it higher or lower?
          1. Higher
          2. Lower
          '''))
          if answer == 1:
            #If it was higher, the new limit must be at least 1 higher than the original guess. Resets the limit and exits the asking loop
            lowerLimit = guess+1
            break
          elif answer == 2:
            #If it was lower, the new limit must be at least 1 lower than the original guess. Resets the limit and exits the asking loop.
            upperLimit = guess-1
            break
          else:
            #If invalid answer was given to the higher/lower question, user is asked to input a new answer, and while loop repeats
            print("Please answer with either 1 or 2.")

      else:
        #If invalid answer was given to the "Is your number x" question, user is asked to input a new answer, and while loop variable is again set to true
        print("Please answer with either 1 or 0.")
        asking = True
    
    if upperLimit<lowerLimit:
      #If, after performing the guess, the upper limit becomes greater than the lower limit (e.g. number has already been narrowed down, but user picks no anyway), print string as error message to user and return function. 
      print("Hmm. It seems like you have tried to trick me. You do not get to play anymore. :(")
      return

  return

def slope(x1, y1, x2, y2):
  '''
  Finds the slope of a line given coordinates of two points.
  
  Enters coordinates into the slope equation and returns the value. If the y-coordinates are equal, the slope is returned as a string: "undefined", and a string "This is not a line." if x-coordinates also match.

  Parameters
  ----------
  x1 : float
    x-coordinate of the first point, A, in the line, AB.
  y1 : float
    y-coordinate of the first point, A, in the line, AB.
  x2 : float
    x-coordinate of the second point, B, in the line AB.
  y2 : float
    y-coordinate of the second point, B, in the line AB.
  
  Returns
  -------
  float, string
    If coordinates form a line of slope or a real number, the value of m is returned. If the coordinates do not form a line, the subsequent error message is returned. If the coordinates form a line with an undefined slope, the string "undefined" is returned.
  '''
  
  #Assertions
  assert isinstance (x1, float), "slope function parameter error"
  assert isinstance (y1, float), "slope function parameter error"
  assert isinstance (x2, float), "slope function parameter error"
  assert isinstance (y2, float), "slope function parameter error"
  
  
  if x2==x1 and y2==y1:
    #Checks if the points have equivalent coordinates. If they do, this is a point, not a line. Returns error message string.
    return "This is not a line."
  elif y2==y1:
    #Checks if the points have equivalent y-coordinates. If they do, the slope must be 0. Returns a value of 0 for slope.
    return 0.0
  elif x2==x1:
    #Checks if the points have equivalent x-coordinates. If they do, the slope must be undefined. Returns string: "undefined"
    return "undefined"
  else:
    #Uses slope formula m=(y2-y1)/(x2-x1) to return slope of the line
    return (y2-y1)/(x2-x1)
  return

def perpendicularSlope(originalSlope):
  '''
  Finds the slope of a line perpendicular to the given one.
  
  Finds the negative reciprocal slope and returns the value. If the slope is 0, it returns the string "undefined".  If the slope is "undefined", it returns 0.

  Parameters
  ----------
  originalSlope : float, string
    Value of given slope. If the slope is undefined, the paramater will be a string: "undefined".
  
  Returns
  -------
  float, string
    Returns the negative reciprocal of originalSlope, which is the perpendicular slope. If the original slope was "undefined", a 0 will be returned. If it was 0, the string "undefined" will be returned.
  '''
  
  #Assertions
  assert isinstance (originalSlope, (float, str)), "perpendicularSlope function parameter error"
  

  if originalSlope == 0:
    #Checks if the original slope was 0. If it was, the perpendicular slope is undefined. Returns string: "undefined".
    return "undefined"
  elif originalSlope == "undefined":
    #Checks if the original slope was undefined. If it was, the perpendicular slope is 0. Returns this value.
    return 0.0
  else:
    #Finds the perpendicular slope by returning the negative reciprocal of the original slope. Returns this value.
    return -(originalSlope**-1)
  return

def midpoint(x1, y1, x2, y2):
  '''
  Finds the coordinates of the midpoint of a line.
  
  Inserts line coordinates into midpoint equation and returns the answer.

  Parameters
  ----------
  x1 : float
    x-coordinate of the first point, A, in the line, AB.
  y1 : float
    y-coordinate of the first point, A, in the line, AB.
  x2 : float
    x-coordinate of the second point, B, in the line AB.
  y2 : float
    y-coordinate of the second point, B, in the line AB.
  
  Returns
  -------
  list[float, float]
    Returns two floats inside a list. First float corresponds to x-coordinate of midpoint, second float corresponds to y-coordinate of midpoint.
  '''
  
  #Assertions
  assert isinstance (x1, float), "midpoint function parameter error"
  assert isinstance (y1, float), "midpoint function parameter error"
  assert isinstance (x2, float), "midpoint function parameter error"
  assert isinstance (y2, float), "midpoint function parameter error"
  

  #Returns midpoint coordinates in a list based on midpoint equation.
  return [(x1+x2)/2, (y1+y2)/2]

def findB (x, y, givenSlope):
  '''
  Finds y-intercept of a line given the slope and a point on the graph.
  
  Inserts values into y=mx+b equation, solving for variable b.

  Parameters
  ----------
  x : float
    x-coordinate of given point.
  y : float
    y-coordinate of given point.
  givenSlope : float, string
    The given slope: the value of m provided for equation y=mx+b. Could be a string: "undefined" if the slope is undefined.
  
  Returns
  -------
  float, string
    Returns the value of b by applying the equation y=mx+b and solving for b.  If the slope is 0, the value of y is returned. If the slope is undefined, the line does not cross the y-axis, and thus the function returns the string "There is no y-intercept."
  '''
  
  #Assertions
  assert isinstance (x, float), "findB function parameter error"
  assert isinstance (y, float), "findB function parameter error"
  assert isinstance (givenSlope, (float, str)), "findB function parameter error"
  

  if givenSlope == "undefined":
    #Checks if given slope is undefined. If it is, there is no y-intercept. Returns this message as a string.
    return "There is no y-intercept."
  elif givenSlope == 0:
    #Checks if given slope is 0. If it is, the y-intercept is the y-coordinate of the given point. Returns this value.
    return y
  else:
    #Finds the value of b by substituting the coordinates into the equation and solving for b. Returns this value.
    return y-givenSlope*x
  return

def findIntersection(slopeA, yInterceptA, slopeB, yInterceptB, slopeC, yInterceptC):
  '''
  Finds the intersection of three lines (medians, altitudes or perpendicular bisectors of triangles) to find one of the three triangle centres.
  
  Substitutes y=y (i.e. mx+b=mx+b) for the equations of two of the lines and solves for the x-coordinate of the intersection, then plugs in the x-coordinate into one of the lines' equations. If one of the lines being used for the intersection has an undefined slope, the function will find the intersection of the other two lines.

  Parameters
  ----------
  slopeA : float, string
    Value of the slope of the first intersecting line. If the slope is undefined, the paramater will be a string: "undefined".
  yInterceptA : float, string
    Y-intercept (b) value of first line. If the slope of the line is undefined, the parameter will be a string: "There is no y-intercept."
  slopeB : float, string
    Value of the slope of the second intersecting line. If the slope is undefined, the paramater will be a string: "undefined".
  yInterceptB : float, string
    Y-intercept (b) value of second line. If the slope of the line is undefined, the parameter will be a string: "There is no y-intercept."
  slopeC : float, string
    Value of the slope of the third intersecting line. If the slope is undefined, the paramater will be a string: "undefined".
  yInterceptC : float, string
    Y-intercept (b) value of third line. If the slope of the line is undefined, the parameter will be a string: "There is no y-intercept."
  
  Returns
  -------
  string
    Returns the x-coordinate and y-coordinate of the triangle centre in a summarizing sentence.
  '''
  
  #Assertions
  assert isinstance (slopeA, (float, str)), "findIntersection function parameter error"
  assert isinstance (yInterceptA, (float, str)), "findIntersection function parameter error"
  assert isinstance (slopeB, (float, str)), "findIntersection function parameter error"
  assert isinstance (yInterceptB, (float, str)), "findIntersection function parameter error"
  assert isinstance (slopeC, (float, str)), "findIntersection function parameter error"
  assert isinstance (yInterceptC, (float, str)), "findIntersection function parameter error"
  

  if (slopeA == "undefined" and yInterceptA == "There is no y-intercept."):
    #Checks if first line's slope is undefined. If it is, use the other two lines to find the intersection.
    
    #Finds intersection x-coordinate by setting y=y on lines B and C and solving for x.
    intersectionXCo = (yInterceptB-yInterceptC)/(slopeC-slopeB)
    #Finds intersection y-coordinate by substituting the x-coordinate into equation of line B
    intersectionYCo = slopeB*intersectionXCo+yInterceptB
  elif (slopeB == "undefined" and yInterceptB == "There is no y-intercept."):
    #Checks if second line's slope is undefined. If it is, use the other two lines to find the intersection.

    #Finds intersection x-coordinate by setting y=y on lines A and C and solving for x.
    intersectionXCo = (yInterceptC-yInterceptA)/(slopeA - slopeC)
    #Finds intersection y-coordinate by substituting the x-coordinate into equation of line C
    intersectionYCo = slopeC*intersectionXCo+yInterceptC
  else:
    #Default case: lines A and B have defined slopes.
    
    #Finds intersection x-coordinate by setting y=y on lines A and C and solving for x.
    intersectionXCo = (yInterceptB-yInterceptA)/(slopeA - slopeB)
    #Finds intersection y-coordinate by substituting the x-coordinate into equation of line C
    intersectionYCo = slopeA*intersectionXCo+yInterceptA

  #Returns coordinates of the centre of the triangle in a summarizing sentence.
  return str("The triangle centre is at (" + str(intersectionXCo) + ", " + str(intersectionYCo) + ").")

def orthocentre(xA, yA, xB, yB, xC, yC):
  '''
  Finds orthocentre of a triangle given co-ordinates of three points.
  
  For the three lines on the triangle, the function finds the slope of the perpendicular line. Using these slopes and the coordinates of the opposite point (e.g. C if line is AB), it creates equations for the three lines in the form y=mx+b by substituting the point to find b. It then sets y=y using two of the lines (which possess defined slopes) to find the point of intersection.

  Parameters
  ----------
  xA : float
    x-coordinate of first point, A, on the triangle ABC.
  yA : float
    y-coordinate of first point, A, on the triangle ABC.
  xB : float
    x-coordinate of second point, B, on the triangle ABC.
  yB : float
    y-coordinate of second point, B, on the triangle ABC.
  xC : float
    x-coordinate of third point, C, on the triangle ABC.
  yC : float
    y-coordinate of third point, C, on the triangle ABC.
  
  Returns
  -------
  string
    Returns the x-coordinate and y-coordinate of the orthocentre in a summarizing sentence.
  '''
  
  #Assertions
  assert isinstance (xA, float), "orthocentre function parameter error"
  assert isinstance (yA, float), "orthocentre function parameter error"
  assert isinstance (xB, float), "orthocentre function parameter error"
  assert isinstance (yB, float), "orthocentre function parameter error"
  assert isinstance (xC, float), "orthocentre function parameter error"
  assert isinstance (yC, float), "orthocentre function parameter error"
  
  #Finds equations of altitudes AB, BC, and AC
  #Altitude of AB:
  #Finds slope of line AB
  mAtoB = slope(xA, yA, xB, yB)
  #Finds slope of altitude of AB by finding perpendicular slope
  perpSlopeAtoB = perpendicularSlope(mAtoB)
  #Finds y-intercept of the altitude of AB by plugging in point C
  yInterceptLine1 = findB(xC, yC, perpSlopeAtoB)

  #Altitude of BC:
  #Finds slope of line BC
  mBtoC = slope(xB, yB, xC, yC)
  #Finds slope of altitude of BC by finding perpendicular slope
  perpSlopeBtoC = perpendicularSlope(mBtoC)
  #Finds y-intercept of the altitude of BC by plugging in point A
  yInterceptLine2 = findB(xA, yA, perpSlopeBtoC)

  #Altitude of AC:
  #Finds slope of line AC
  mAtoC = slope(xA, yA, xC, yC)
  #Finds slope of altitude of AC by finding perpendicular slope
  perpSlopeAtoC = perpendicularSlope(mAtoC)
  #Finds y-intercept of the altitude of AC by plugging in point B
  yInterceptLine3 = findB(xB, yB, perpSlopeAtoC)

  #Finds intersection of the three lines and returns coordinates of orthocentre in a summarizing sentence
  return findIntersection(perpSlopeAtoB, yInterceptLine1, perpSlopeBtoC, yInterceptLine2, perpSlopeAtoC, yInterceptLine3)

def centroid(xA, yA, xB, yB, xC, yC):
  '''
  Finds centroid of a triangle given co-ordinates of three points.
  
  For the three lines on the triangle, the function finds the midpoints. Using these midpoints and the coordinates of the opposite point (e.g. C if line is AB), it creates equations for the three lines by finding the slope of the points, then substituting the midpoint into y=mx+b. Finally, it sets y=y using two of the lines (which possess defined slopes) to find the point of intersection.

  Parameters
  ----------
  xA : float
    x-coordinate of first point, A, on the triangle ABC.
  yA : float
    y-coordinate of first point, A, on the triangle ABC.
  xB : float
    x-coordinate of second point, B, on the triangle ABC.
  yB : float
    y-coordinate of second point, B, on the triangle ABC.
  xC : float
    x-coordinate of third point, C, on the triangle ABC.
  yC : float
    y-coordinate of third point, C, on the triangle ABC.
  
  Returns
  -------
  string
    Returns the x-coordinate and y-coordinate of the centroid in a summarizing sentence.
  '''
  
  #Assertions
  assert isinstance (xA, float), "centroid function parameter error"
  assert isinstance (yA, float), "centroid function parameter error"
  assert isinstance (xB, float), "centroid function parameter error"
  assert isinstance (yB, float), "centroid function parameter error"
  assert isinstance (xC, float), "centroid function parameter error"
  assert isinstance (yC, float), "centroid function parameter error"
  
  #Finds medians of AB, BC, and AC
  #Median of AB:
  #Finds midpoint of AB
  halfAtoB = midpoint(xA, yA, xB, yB)
  #Creates variables to hold midpoint coordinates
  midPointCoX = halfAtoB[0]
  midPointCoY = halfAtoB[1]
  #Finds slope of median by plugging in point C
  medianSlopeAB = slope(midPointCoX, midPointCoY, xC, yC)
  #Finds y-intercept of median AB using midpoint coordinates and slope
  yInterceptLine1 = findB(midPointCoX, midPointCoY, medianSlopeAB)

  #Median of BC:
  #Finds midpoint of BC
  halfBtoC = midpoint(xB, yB, xC, yC)
  #Creates variables to hold midpoint coordinates
  midPointCoX = halfBtoC[0]
  midPointCoY = halfBtoC[1]
  #Finds slope of median by plugging in point A
  medianSlopeBC = slope(midPointCoX, midPointCoY, xA, yA)
  #Finds y-intercept of median BC using midpoint coordinates and slope
  yInterceptLine2 = findB(midPointCoX, midPointCoY, medianSlopeBC)

  #Median of AC:
  #Finds midpoint of AC
  halfAtoC = midpoint(xA, yA, xC, yC)
  #Creates variables to hold midpoint coordinates
  midPointCoX = halfAtoC[0]
  midPointCoY = halfAtoC[1]
  #Finds slope of median by plugging in point B
  medianSlopeAC = slope(midPointCoX, midPointCoY, xB, yB)
  #Finds y-intercept of median AC using midpoint coordinates and slope
  yInterceptLine3 = findB(midPointCoX, midPointCoY, medianSlopeAC)

  #Finds intersection of the three lines and returns coordinates of centroid in a summarizing sentence
  return findIntersection(medianSlopeAB, yInterceptLine1, medianSlopeBC, yInterceptLine2, medianSlopeAC, yInterceptLine3)

def circumcentre(xA, yA, xB, yB, xC, yC):
  '''
  Finds circumcentre of a triangle given co-ordinates of three points.
  
  For the three lines on the triangle, the function finds the slope of the perpendicular line, and the midpoints. Using these slopes and points, it creates equations for the three lines, then sets y=y using two of the lines (which possess defined slopes) to find the point of intersection.

  Parameters
  ----------
  xA : float
    x-coordinate of first point, A, on the triangle ABC.
  yA : float
    y-coordinate of first point, A, on the triangle ABC.
  xB : float
    x-coordinate of second point, B, on the triangle ABC.
  yB : float
    y-coordinate of second point, B, on the triangle ABC.
  xC : float
    x-coordinate of third point, C, on the triangle ABC.
  yC : float
    y-coordinate of third point, C, on the triangle ABC.
  
  Returns
  -------
  string
    Returns the x-coordinate and y-coordinate of the circumcentre in a summarizing sentence.
  '''
  
  #Assertions
  assert isinstance (xA, float), "circumcentre function parameter error"
  assert isinstance (yA, float), "circumcentre function parameter error"
  assert isinstance (xB, float), "circumcentre function parameter error"
  assert isinstance (yB, float), "circumcentre function parameter error"
  assert isinstance (xC, float), "circumcentre function parameter error"
  assert isinstance (yC, float), "circumcentre function parameter error"
  
  #Finds perpendicular bisectors of AB, BC, and AC
  #Perpendicular bisector of AB:
  #Finds midpoint of AB
  halfAtoB = midpoint(xA, yA, xB, yB)
  #Creates variables to hold midpoint coordinates
  midPointCoX = halfAtoB[0]
  midPointCoY = halfAtoB[1]
  #Finds slope of AB
  mAtoB = slope(xA, yA, xB, yB)
  #Finds perpendicular slope of AB
  perpSlopeAtoB = perpendicularSlope(mAtoB)
  #Finds y-intercept of perpendicular bisector of AB using determined slope and midpoint coordinates
  yInterceptLine1 = findB(midPointCoX, midPointCoY, perpSlopeAtoB)

  #Perpendicular bisector of BC:
  #Finds midpoint of BC
  halfBtoC = midpoint(xB, yB, xC, yC)
  #Creates variables to hold midpoint coordinates
  midPointCoX = halfBtoC[0]
  midPointCoY = halfBtoC[1]
  #Finds slope of BC
  mBtoC = slope(xB, yB, xC, yC)
  #Finds perpendicular slope of BC
  perpSlopeBtoC = perpendicularSlope(mBtoC)
  #Finds y-intercept of perpendicular bisector of BC using determined slope and midpoint coordinates
  yInterceptLine2 = findB(midPointCoX, midPointCoY, perpSlopeBtoC)

  #Perpendicular bisector of AC:
  #Finds midpoint of AC
  halfAtoC = midpoint(xA, yA, xC, yC)
  #Creates variables to hold midpoint coordinates
  midPointCoX = halfAtoC[0]
  midPointCoY = halfAtoC[1]
  #Finds slope of AC
  mAtoC = slope(xA, yA, xC, yC)
  #Finds perpendicular slope of AC
  perpSlopeAtoC = perpendicularSlope(mAtoC)
  #Finds y-intercept of perpendicular bisector of AC using determined slope and midpoint coordinates
  yInterceptLine3 = findB(midPointCoX, midPointCoY, perpSlopeAtoC)

  #Finds intersection of the three lines and returns coordinates of circumcentre in a summarizing sentence
  return findIntersection(perpSlopeAtoB, yInterceptLine1, perpSlopeBtoC, yInterceptLine2, perpSlopeAtoC, yInterceptLine3)
  
def triangleCentre():
  '''
  Finds one of three separate types of triangle centres given suitable coordinates of three points.
  
  Asks user to input coordinates of 3 points, checks their validity, and then asks user which centre to find, calling the suitable function and printing the coordinates of the triangle centre. The user is then prompted on whether they wish to find another centre of the same triangle. If so, they continue picking a centre to find. If not, the function exits.

  Parameters
  ----------
  None
  
  Returns
  -------
  Nothing
  '''
  #Prompts user to input the coordinates of the triangle.
  xA = float(input("Enter the x-coordinate of point A: "))
  yA = float(input("Enter the y-coordinate of point A: "))
  xB = float(input("Enter the x-coordinate of point B: "))
  yB = float(input("Enter the y-coordinate of point B: "))
  xC = float(input("Enter the x-coordinate of point C: "))
  yC = float(input("Enter the y-coordinate of point C: "))
  
  #Finds the slopes of all three triangles
  mAtoB = slope(xA, yA, xB, yB)
  mBtoC = slope(xB, yB, xC, yC)
  mAtoC = slope(xA, yA, xC, yC)

  #Checks whether any of the slopes are equivalent (triangles cannot have parallel lines) or if any of the points have equivalent coordinates. If so, ask user to enter new coordinates that actually form a triangle.
  if mAtoB == mBtoC or mAtoB == mAtoC or mAtoC == mAtoB or mAtoB=="This is not a line." or mAtoC == "This is not a line." or mBtoC == "This is not a line." :
    print("Please enter proper coordinates for your triangle.  Triangles are 3-sided polygons, not lines!")
    return
  
  #Creates a variable to check whether the user wants to continue finding the centre of the triangle. Initializes it to true.
  findCentre = True
  #Runs a loop as long as user wishes to keep finding the centre of the triangle.
  while findCentre:
    #Asks user which triangle they would like to find.
    ans = int(input('''Which centre would you like to find?
    1. Orthocentre
    2. Centroid
    3. Circumcentre
    '''))
    if ans == 1:
      #If the user wishes to find the orthocentre, call the function and print the resulting answer.
      print (orthocentre(xA, yA, xB, yB, xC, yC))
      #Create a variable to check whether the user has selected a valid answer or not. This will be used to activate or deactivate the "Do you want to choose another centre" message.
      validSelection = True
      #Set a sleep value so the user can see their answer
      sleep(1)
    elif ans == 2:
      #If the user wishes to find the centroid, call the function and print the resulting answer.
      print (centroid(xA, yA, xB, yB, xC, yC))
      validSelection = True
      #Set a sleep value so the user can see their answer
      sleep(1)
    elif ans == 3:
      #If the user wishes to find the circumcentre, call the function and print the resulting answer.
      print (circumcentre(xA, yA, xB, yB, xC, yC))
      validSelection = True
      #Set a sleep value so the user can see their answer
      sleep(1)
    else:
      #If the user did not enter a proper answer, ask them to try again.
      validSelection = False
      ans = print("Please choose a valid option from the list. You must enter an integer between 1 and 3.")

    #Runs a loop to ask the user whether they wish to find another centre. Loop only runs if a valid answer has been chosen previously.
    while validSelection:
      #Ask if they would like to find a new centre.
      ans = int(input('''Would you like to find another centre of this triangle?
      1. Yes
      0. No
      '''))
      if ans == 1:
        #If they wish to find another centre, keep the variable which keeps the loop running true.
        findCentre = True
        #Set variable to exit while loop
        validSelection = False
      elif ans == 0:
        #If they wish to exit the loop, set the variable to false and exit the triangleCentre function.
        findCentre = False
        #Set variable to exit while loop
        validSelection = False
      else:
        #If the user did not select a valid answer, ask them to try again.
        print("Please choose a valid option from the list. You must enter either 1 or 0.")
        validSelection = True
  return


def isPrime(number):
  '''
  Checks if a given number is prime.
  
  Divides the number by all numbers preceding up to 1/2 the original value. If no remainder is yielded for any of these numbers, the given number is a prime.

  Parameters
  ----------
  number : int
    Given number to check for prime property.
  
  Returns
  -------
  bool
    Returns a true or false statement to the function's question: "Is the given number a prime?"
  '''
  #Assertions
  assert isinstance (number, int), "isPrime function parameter error"

  #Set the value of the upper limit for dividing to 1/2 the original number to speed up processing (by reducing the total number of possible factors)
  upperLimit = number//2

  #Set an initial value for the result of the operation
  prime = True

  #For every number from 2 to 1/2 the original number, check if a division yields no remainder. If it does, the number is composite and the loop can be exited immediately. If no factors are found, the prime boolean will remain "True", and this will be appropriately returned.
  for divisor in range (2, upperLimit):
    if number % divisor == 0:
      prime = False
      break
  return prime

def primeFactorization(number):
  '''
  Finds all prime factors of a given number in order from least to greatest.
  
  Divides the given number by the lowest prime possible until the final answer is no longer a composite number.

  Parameters
  ----------
  number : int
    Given number to find prime factors for.
  
  Returns
  -------
  list[int, int...]
    Returns a variably sized list of all the prime factors of the number in order from least to greatest.
  '''
  #Assertions
  assert isinstance (number, int), "primeFactorization function parameter error"

  #Initializes a list to hold the prime factors
  primeFactors = []

  #If the original number is even:
  if number % 2 == 0:
    #Create a varaible to hold this data
    even = True
    #While it is even:
    while even:
      #Continuously divide it by 2 and record this factor into the prime factors list
      number = number//2
      primeFactors.append(2)
      #If the new number is even, keep the variable true
      if number % 2 == 0:
        even = True
      #If the new number becomes odd, change the even variable to false and exit the loop
      else:
        even = False
    
    #Runs the isPrime function to check if the resulting number is a prime. If it is, add it to the list of primes and return the final result.
    if isPrime(number):
      primeFactors.append(number)
      return primeFactors
    #If it is not prime, set an upper integer limit to the highest number we need to find factors for (the largest factor of this odd number has to be less than half the original number)
    else:
      upperLimit = number//2
  #If the number was odd to begin with, the same applies
  else:
    upperLimit = number//2

  #List of primes to 100 for faster processing. List begins at 3 since divisibility by 2 has already been checked for faster processing
  primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

  #If the possible factors of the number are higher than the default list:
  if upperLimit>100:
    #Check through all numbers from 101 (first prime above 100) to the highest possible factor of the number to load a list of all the primes the number has. Skip the even numbers by using a step of 2
    for divisor in range (101, upperLimit, 2):
      #Call the isPrime function to check. If it is a prime, add the prime to the end of the primes list
      if isPrime(divisor):
        primes.append(divisor)

  #While the number still has factors, keep searching for prime factors
  while not isPrime(number):
    #Check the first prime in the list. If the number is divisible by this, add it to the list of prime factors and try again
    if number%primes[0] == 0:
      number = number//primes[0]
      primeFactors.append(primes[0])
    #If the number is no longer divisible by the prime factor, delete the prime factor
    else:
      del primes[0]

  #When the while loop exits, the final number will be a prime. Add this to the list of prime factors
  primeFactors.append(number)

  #Return the list of prime factors
  return primeFactors

def simplifyRadical():
  '''
  Simplifies a square root radical to its lowest form by removing square factors.

  Asks the user for values of the original coefficient on the radical as well as the integer inside the radical, and returns the most simplified form of the radical by determining its prime factors and removing pairs of primes.

  Parameters
  ----------
  None
  
  Returns
  -------
  Nothing
  '''
  #Explains instructions with a wait to allow user to read
  print('''Welcome. This option allows you to simplify square roots.
  Note: The original coefficient of the radical as well as the number under the radical sign must be an integer.''')
  sleep(1)

  #Continuous loop waits until accurate answer has been given to input questions
  while True:
    #Ask for original coefficient of the radical as well as the integer under the radical
    originalCoefficient = int(input("Enter the current co-efficient in front of the radical. Please enter an integer only: "))
    originalRadical = int(input("Enter the number beneath the radical sign. Please enter an integer only. This number must be between 0 and 10 000: "))
    
    #If the number under the radical sign is negative, print error message string
    if originalRadical < 0:
      print("Square roots cannot be negative! Please try again.")
    #If the number given is too large to compute quickly, display an error message string
    elif originalRadical>=10000:
      print("This number is too big! Try again.")
    #If the number under the root or the coefficient is a zero, immediately conclude that the answer is 0 (anything multiplied by 0 or root 0 is 0)
    elif originalCoefficient == 0 or originalRadical == 0:
      print("The answer is 0.")
      #Return statement exits the function
      return
    #If the radical is 1, the square root is simply 1. Print this answer
    elif originalRadical == 1:
      print("The answer is: " + str(originalCoefficient) + ".")
      #Return statement exits the function
      return
    else:
      #If there are no errors in the input, exit the continuous loop
      break

  #Check if the original radical is a prime by calling the function. If it is, tell the user that they already have the simplest form, and exit the function
  if isPrime(originalRadical):
    print("The radical is a prime number and cannot be simplified further.")
    #Return statement exits the function
    return

  #Call prime factorization function and get a list of prime factors of the original radical
  primeFactors = primeFactorization(originalRadical)
  #Calculate the largest prime by looking at the end of the prime factor list (it is in order from smallest to largest primes)
  largestPrime = primeFactors[len(primeFactors)-1]

  #Create an "index" variable to hold the current checking position of the prime factors list
  index = 0
  #Create a list of all prime factors of the radical which do not come in pairs
  radicalFactors = []
  #While the index variable is smaller than the size of the prime factors list or as long as the current number being checked is not equal to the largest prime factor of the radical:
  while index < len(primeFactors)-1 or primeFactors[index]!=largestPrime:
    #Create variables called increment and pairCounter to hold the number of prime pairs found, and to check the next element of the list
    increment = 1
    pairCounter = 1
    #Check the current factor in the prime factors list and the next. If they are equal, add 1 to the pair counter and 1 to the increment. This will make the loop check whether the next factor is also equal to the first (go through list and count how many times a prime factor is repeated)
    while primeFactors[index] == primeFactors[index+increment]:
      increment+=1
      pairCounter+=1
    
    #Multiply the original coefficient value by the value of the prime factor to the power of the number of pairs found. (If the original radical was 32, we would find that the prime factors are 2*2*2*2*2, or four pairs of 2's. Thus, since root32=root(2**4)*2, it is equivalent to 2**(4/2)root2=4root2)
    originalCoefficient*=primeFactors[index]**(pairCounter//2)

    #If the number of repeated primes was odd, place the value of this prime into a list of lone primes
    if pairCounter % 2 != 0:
      radicalFactors.append(primeFactors[index])

    #pairCounter represents the number of primes already checked in the prime factors list for repeats, while index refers to the position of the checker. Thus, to check the number or repeats for the next prime, the index must be increased by the size of pairCounter
    index += pairCounter
  
  '''Similar to the while loop, find the repeats of the largest prime factor by subtracting the size of the loop from the current check index. Integer dividing this number by 2 will give the answer to the number of paired primes. This must be done in a different way from the while loop because the loop will be unable to check for the end of the list.'''
  lastProduct = largestPrime**((len(primeFactors)-index)//2)
  #If there are no repeats of the largest prime, dividing this number by 2 will yield 0, which will cause errors when multiplying into the coefficient. So, if this is the case, add this prime to the lone primes list
  if lastProduct == 0:
    radicalFactors.append(largestPrime)
  #If this is not the case, but there is still an odd number of primes, add the number to the lone primes list, but find the result of the simplification
  elif (len(primeFactors) - index) % 2 != 0:
    radicalFactors.append(largestPrime)
    originalCoefficient = originalCoefficient**lastProduct
  #If there is no lone prime, simply find the result of simplification
  else:
    originalCoefficient = originalCoefficient**lastProduct

  #Set the initial value of the number under the radical to 1, so that you are not multiplying by 0 or an undefined number during simplification
  radicalTotal = 1
  #Take all the lone prime factors and find the product of all these primes
  for counter in range (0, len(radicalFactors)):
    radicalTotal *= radicalFactors[counter]
  #If there were no primes in the list, the radical was a perfect square. Print the result of the coefficient only.
  if radicalTotal == 1:
    print("The answer is: " + str(originalCoefficient) + ".")
  #If there were primes, print the result as simplified as possible
  else:
    print("The answer is: " + str(originalCoefficient) + " root " + str(radicalTotal) + ".")

  return






# ------------- MAIN ---------------- #

#Assertions:
#slope function
assert slope(1.0, 2.0, 3.0, 4.0) == 1, "slope function error."
assert slope(0.0, 1.0, 0.0, 1.0) == "This is not a line.", "slope function error."
assert slope(1.0, 1.0, 1.0, 4.0) == "undefined", "slope function error."
#perpendicularSlope function
assert perpendicularSlope(-2.0) == 0.5, "perpendicularSlope function error."
assert perpendicularSlope("undefined") == 0, "perpendicularSlope function error."
assert perpendicularSlope(0.0) == "undefined", "perpendicularSlope function error."
#midpoint function
assert midpoint(10.0, 5.0, 2.0, 3.0) == [6, 4], "midpoint function error."
#findB function
assert findB(4.0, 10.0, 2.0) == 2, "findB function error."
assert findB(4.0, 10.0, "undefined") == "There is no y-intercept.", "findB function error."
assert findB(4.0, 10.0, 0.0) == 10, "findB function error."
#findIntersection function
assert findIntersection (2.0, 3.0, 1.0, 4.0, -3.0, 8.0) == "The triangle centre is at (1.0, 5.0).", "findIntersection function error."
assert findIntersection ("undefined", "There is no y-intercept.", 1.0, 4.0, -3.0, 8.0) == "The triangle centre is at (1.0, 5.0).", "findIntersection function error."
assert findIntersection (2.0, 3.0, "undefined", "There is no y-intercept.", -3.0, 8.0) == "The triangle centre is at (1.0, 5.0).", "findIntersection function error."
#orthocentre function
assert orthocentre(-5.0, -5.0, -5.0, 0.0, 0.0, 5.0) == "The triangle centre is at (-15.0, 5.0).", "orthocentre function error."
#centroid function
assert centroid(-5.0, -5.0, -5.0, 0.0, 0.0, 5.0) == "The triangle centre is at (" + str(-10/3) + ", 0.0).", "centroid function error."
#circumcentre function
assert circumcentre(-5.0, -5.0, -5.0, 0.0, 0.0, 5.0) == "The triangle centre is at (" + str(5/2) + ", " + str(-5/2) + ").", "circumcentre function error."
#isLetter function
assert isLetter('b') == True, "isLetter function error"
assert isLetter('$') == False, "isLetter function error"
#checkLetter function (commented out because they include print statements)
#assert checkLetter("b", "bored", "-----", 4) == [4, "b----"], "checkLetter function error"
#assert checkLetter("s", "SpaceX", "--aceX", 2) == [2, "S-aceX"], "checkLetter function error"
#assert checkLetter("r", "SpaceX", "--aceX", 2) == [1, "--aceX"], "checkLetter function error"
#primeFactorization function
assert primeFactorization(3072) == [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3], "primeFactorization function error"
assert primeFactorization(999) == [3, 3, 3, 37], "primeFactorization function error"
#isPrime function
assert isPrime(2) == True, "isPrime function error"
assert isPrime(1) == True, "isPrime function error"
assert isPrime(999) == False, "isPrime function error"

#Set a loop to constantly print the menu until user wishes to exit
while True:
  #Print menu
  ans=int(input('''
  Welcome to Arcadia.
  Please select an option from the following:
  1. Word Scrambler
  2. Trivia
  3. Pyramid Drawer
  4. Hangman
  5. Quadratic Formula Calculator
  6. Guess my number
  7. Find the Centre of a Triangle
  8. Simplify the radical
  0. Exit
  '''))
  if ans == 1:
    #If 1st option is selected, call wordScrambler game function
    wordScrambler()
  elif ans == 2:
    #If 2nd option is selected, call trivia game function
    trivia()
  elif ans == 3:
    #If 3rd option is selected, call pyramidDrawer game function
    pyramidDrawer()
  elif ans == 4:
    #If 4th option is selected, hangman game function is called
    hangman()
  elif ans == 5:
    #If 5th option is selected, call quadraticFormulaCalc function
    quadraticFormulaCalc()
  elif ans == 6:
    #If 6th option is selected, number guessing game function is called
    guessNumber()
  elif ans == 7:
    #If the 7th option is selected, call the triangleCentre function
    triangleCentre()
  elif ans == 8:
    #If 8th option is selected, simplifyRadical function is called
    simplifyRadical()
  elif ans == 0:
    #Exit code with a break statement if user wishes to exit
    break
  else:
    #If the answer is not valid, ask user to re-enter a valid option.
    print("Please choose a valid option from the list. You must enter a number.")
  #Delay the next menu display by 1 second to ensure answer from previous function is displayed
  sleep(1)