#-------------REPLACE TEXT CONTENT IN STORY.TXT WITH STORYSTATIC.TXT IF CHANGED-----------#
#-----------------------------------------------------------------------------
# Name:        Python Assignment 2 (assignment2.py)
# Purpose:     Demonstrating Understanding of Lists, Dictionaries,
#              Exceptions, and Logging
#
# Author:      669571
# Created:     30-May-19
# Updated:     6-Jun-19
#-----------------------------------------------------------------------------
#Import dictionaries for logging, sleep and random functions
import random, logging
from time import sleep

#logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename='log.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.info("Program started")

def readUserData():
  '''
  Simple function that reads usernames and passwords from users.txt and returns them in a dictionary.
  
  Reads information from users.txt and sets every 1st line as a username and every 2nd line as the corresponding password.

  Parameters
  ----------
  None
  
  Returns
  -------
  dict['usernames':'passwords']
    Returns a dictionary containing the usernames and passwords of all users in users.txt.
  '''
  logging.debug("readUserData called")
  #Open user data file
  users = open('users.txt', 'r')
  #Hold file data in a variable
  userData = users.readlines()
  #Create a dictionary to hold usernames:passwords
  userInformation = {}
  #Lines 1, 3, 5... correspond to usernames, while the proceeding lines correspond to passwords
  #Read usernames in a for loop
  for user in range (0, len(userData), 2):
    username = userData[user]
    #Read password (follows username on next line)
    password = userData[user+1]
    #If the username or password includes a newline character, remove it
    if username.endswith('\n'):
      username = username[:-1]
    if password.endswith('\n'):
      password = password[:-1]
    #Create a new key and value in the dictionary which corresponds to username and password found in data file 
    userInformation[username] = password
  #Print dictionary to ensure newlines have been removed
  logging.info("Usernames and passwords: ")
  logging.info(userInformation)
  #Close file for reading
  users.close()

  return userInformation

def checkAccountStatus(userAuthentication):
  '''
  Logs user into account or creates a new one.
  
  Asks user whether they have an account or not, and calls loginFlow to verify user input.

  Parameters
  ----------
  userAuthentication : dict
    Dictionary containing usernames of all users in data file and the corresponding passwords.
  
  Returns
  -------
  None

  Raises (this section is only applicable if your function raises an exception)
  ------
  ValueError
    If the user does not enter an appropriate answer to question: "Do you have an account?". Raised if entered value is not an int or if is not 0 or 1
  '''
  logging.debug("checkAccountStatus called")

  while True:
    #Ask user if they have an account, try to convert to int
    print("Do you have an account?".center(screenSize))
    hasAccount = input("1. Yes\n0. No\n")
    #If user did not enter an int, raise exception
    if not hasAccount.isdecimal():
      raise ValueError("An error occurred: Please enter an integer value.".center(screenSize))
    hasAccount = int(hasAccount)
    #If user did not answer 0 or 1, raise exception
    if(hasAccount!=0 and hasAccount!=1):
      raise ValueError("An error occurred: Please enter either 1 or 0.".center(screenSize))
    #If no error occured, continue with program
    else:
      #Send user's answer and dictionary of accounts to a function
      userAuthentication = loginFlow(hasAccount, userAuthentication)
      #If no errors occur, exit the login flow loop
      break
  #Open the user text file as write
  users = open('users.txt', 'w')
  #Write each username and password in succession from the dictionary to the file
  for keys in userAuthentication.keys():
    #For each username, write the key from the dictionary, add a newline, then print each password
    #Log to ensure file write is happening appropriately
    logging.info("Writing to file: " + str(keys)+ '\n' + str(userAuthentication[keys]) + '\n')
    users.write(str(keys)+ '\n' + str(userAuthentication[keys]) + '\n')
  #Close file
  users.close()
  return

def loginFlow(accountStatus, userData):
  '''
  Logs the user into their existing account or creates a new one and logs in.
  
  If user has an account, asks for input and checks if username and password match on database. If user does not have account, asks them to create a username and password of ample length.

  Parameters
  ----------
  accountStatus : int
    Holds data about whether or not the user has an account (will either be a 1 or 0)
  userData : dict
    Dictionary of {usernames:passwords, ...}
  
  Returns
  -------
  dict
    Returns the original dictionary with any amendments made to the user information.
  
  Raises
  ------
  TypeError
    If accountStatus is not an integer, an exception will be raised
  ValueError
    If accountStatus is not a 1 or 0, a ValueError exception will be raised
  TypeError
    If userData is not a dictionary, an exception will be raised
  KeyError
    If userData does not include the username being searched for, raise an exception (user does not have an account)
  ValueError
    If the username given for the key is incorrect, raise an exception.
  Exception
    Raised if user is trying to create a new account, but chooses a username that already exists
  ValueError
    Raised if user is trying to create a new account, but chooses a username that is too short.
  ValueError
    Raised if user is trying to create a password for a new account, but chooses one that is too short.
  '''
  logging.debug("loginFlow called")

  #Ensuring accountStatus is an integer between 1 and 0
  if not isinstance(accountStatus, int):
    raise TypeError("An unexpected error occured: accountStatus is not an int")
  if accountStatus!=0 and accountStatus!=1:
    raise ValueError("An unexpected error occured: I'm not sure if you have an account or not!")
  #Ensuring userData is a dictionary
  if not isinstance(userData, dict):
    raise TypeError("An unexpected error occured: userData is not a dictionary!")
  #If the user does have an account, ask them for their username
  if accountStatus:
    username = input("Please enter your username: ")
    #If the username is not in the dictionary, raise an exception
    if username not in userData.keys():
      raise KeyError("Uh oh. Looks like that username doesn't exist.".center(screenSize))
    #If the username is in the dictionary, ask for the corresponding password. If input is incorrect, raise an exception.
    else:
      password = input("Please enter your password: ")
      if password not in userData.values():
        raise ValueError("That isn't the right password. Please try again.".center(screenSize))
  #If the user does not have an account, ask user to enter a new username
  elif accountStatus == False:
    print("You must create an account to enter.".center(screenSize))
    newUsername = input("Please enter a new username: ")
    #If the username already exists, raise an exception
    if newUsername in userData.keys():
      raise Exception("That username already exists! Try a different one.".center(screenSize))
    #If the username is too short, raise an exception
    elif len(newUsername)<3:
      raise ValueError("Please make your username longer.".center(screenSize))
    #Ask user to create a password
    newPassword = input("Please create a password: ")
    #If the password is too short, raise an exception
    if len(newPassword)<3:
      raise ValueError("Please make your password longer.")
    #If all information is entered properly, put the new user data into the dictionary
    userData[newUsername] = newPassword
  else:
    #If accountStatus is still somehow not a 1 or 0, raise an exception
    raise ValueError("An unexpected error occured. I don't know if you have an account or not!")
  #Return the updated dictionary of usernames and passwords
  return userData

def addToDictionary(textFile):
  '''
  Takes in a list of strings and adds legible words to a dictionary.
  
  Takes list of strings, splits into individual words, checks words for non-alpha characters and removes these words as "illegible". When done this filtering process, adds list of words to the dictionary and exits the function.

  Parameters
  ----------
  textFile : list[strings]
    textFile is a list of strings containing English words to be added to the dictionary.
  
  Returns
  -------
  Nothing

  Raises (this section is only applicable if your function raises an exception)
  ------
  TypeError
    If textFile is not a list, raise an exception. 
  IndexError
    If textFile input is an empty list, raise an exception.
  TypeError
    If even a single character in the list is not a string, raise an exception.
  '''
  logging.debug("addToDictionary called")

  #Exceptions checking whether given input is a list of strings or not, and whether input is empty
  if not isinstance(textFile, list):
    raise TypeError("The entered input is not in a list")
  elif not textFile:
    raise IndexError("The entered input is empty!")
  else:
    for item in textFile:
      if not isinstance(item, str):
        raise TypeError("There are some non-string values in the entered list.")
  #Make a list to hold all the words
  textFileWords = []
  #Split the lines into words
  for line in textFile:
    #Delete any newline characters by slicing to -1
    if line.endswith('\n'):
      line = line[:-1]
    #Split the current line into a list of words
    words = line.split(' ')
    #For each word in the list, add it to macbethWords
    textFileWords.extend(words)
  #logging.info("List of words in text: " + str(textFileWords))
  #Make a variable to hold the index of the word we are on
  word = len(textFileWords)-1
  #While the size of the index is smaller than the size of the list, loop through and look for "legible" words
  while word>=0:
    #Subtract 1 from the index
    word-=1
    #If the size of the word in the list is less than one character (i.e. ''), delete it (used to be a newline)
    #Continue statement restarts the loop so that index will remain in range of the length of the list
    if len(textFileWords[word])<1:
      del(textFileWords[word])
      continue
    #If the word ends in a non-alpha character, the character must be a punctuation. Delete this, and add the word
    elif not textFileWords[word][-1].isalpha():
      textFileWords[word] = textFileWords[word][:-1]
    
    #If, after deleting all the non-alpha characters, the string becomes: '', delete it from the list
    if len(textFileWords[word])<1:
      logging.info("Deleting " + str(textFileWords[word] + " since it is empty"))
      del(textFileWords[word])
      continue
    #If, after deleting all the non-alpha characters, the word is just one letter (but not "I" or "a"), then delete the word
    elif len(textFileWords[word])<2 and textFileWords[word].lower()!='i' and textFileWords[word]!='a':
      logging.info("Deleting " + str(textFileWords[word] + " since it is too short"))
      del(textFileWords[word])
      continue
    #Now check if any other non-alpha characters remain in the word. If they do, delete the word from the list
    for character in textFileWords[word]:
      if not character.isalpha():
        logging.info("Deleting " + str(textFileWords[word] + " since it is illegible"))
        del textFileWords[word]
        break

  #Change all words in the textfile to lowercase
  for index in range(len(textFileWords)):
    textFileWords[index] = textFileWords[index].lower()

  #Convert the list to a set, then back to a list (sets include unique values only, thus this gets rid of any multiples)
  textFileWords = list(set(textFileWords))

  # logging.info("Here's a list of legible words in the text file:")
  # logging.info(textFileWords)

  #Open the current dictionary and read the lines
  englishDictionary = open('dictionary.txt', 'r')
  englishWords = englishDictionary.readlines()
  englishDictionary.close()

  #Open the dictionary as write
  englishDictionary = open('dictionary.txt', 'w')
  #Delete all newline characters in the lines read from dictionary.txt
  for index, word in enumerate(englishWords):
    if word.endswith('\n'):
      englishWords[index] = word[:-1]
  #Add all new words to the end of the textfile
  englishWords.extend(textFileWords)
  #Convert to a set to get rid of any duplicate words.
  englishWords = list(set(englishWords))
  #Write the words to the dictionary and add newline characters
  for word in englishWords:
    englishDictionary.write(str(word) + '\n')
  englishDictionary.close()
  return

def checkEnglish(userInput):
  '''
  Checks whether a given phrase is in English or not.
  
  Looks for all given words inside the dictionary.txt file. Looks for variations of the word (such as plural forms, words with punctuation at the end, etc)

  Parameters
  ----------
  userInput : str
    User entered string which is being evaluated as being in English or not.
  
  Returns
  -------
  bool
    Returns True if the given word is in English, otherwise returns False.

  Raises (this section is only applicable if your function raises an exception)
  ------
  TypeError
    If given input is somehow not a string, raises an exception.
  ValueError
    If the given string is empty, or, after stripping all spaces away, is empty, ask user to enter an appropriate input that is at least one word
  '''
  logging.debug("checkEnglish called")

  #Check if input is a string
  if not isinstance(userInput, str):
    logging.critical("userInput paramter in checkEnglish function is not a string!")
    raise TypeError ("An unexpected error occurred.")
  #Did user enter an empty string?
  if userInput == '':
    raise ValueError ("Please enter at least one word.")
  #Remove any excess spaces entered before or after the phrase
  userWords = userInput.strip(' ')
  #Did user enter only spaces?
  if userWords == '':
    raise ValueError ("Please enter at least one word.")
  
  #Open the dictionary and get a list of the lines inside
  dictionary = open('dictionary.txt', 'r')
  dictionaryWords = dictionary.readlines()
  dictionary.close()
  #Remove all newline characters from the dictionary.
  for index in range (len(dictionaryWords)):
    if dictionaryWords[index].endswith('\n'):
      dictionaryWords[index] = dictionaryWords[index][:-1]

  #Get a list of words in the user input by splitting the stripped string
  userWords = userWords.split(' ')

  #Set a default case variable for the return value to True (upcoming loop will check for if the word is not in English)
  isEnglish = True
  logging.debug("List of words in user input: " + str(userWords))

  #Check each word in the user input
  for word in userWords:
    #Convert the word to lowercase characters to compare word to dictionary words
    word = word.lower()
    #If the word ends in a character which is not an alpha character, this may be a punctuation. Remove it.
    if not word[-1].isalpha():
      word = word[:-1]
    #If the word still includes any non-alpha characters, the data is not legible (since the dictionary file excludes words with special characters like apostrophes in the middle)
    if not word.isalpha():
      isEnglish = False
    #Set a variable which represents the plural of the user-inputted word by adding an 's', as is often done to English words. Even if the word is already plural, checking for this additional "s" will not affect final result.
    pluralWord = word + 's'
    #If the word is not in the dictionary:
    if (word not in dictionaryWords):
      #Check if the is in plural form by determining if it ends with an s. If it does, double-check to make sure the second-last letter is not an 's'. If all this is true, check if the word without the 's' is found in the dictionary. This filter is not perfect, but helps weed out many possibilities.
      if(word.endswith('s') and word[-2]!='s' and word[:-1] in dictionaryWords):
        #Do not change the value of isEnglish
        pass
      #If the above if statement is not true, the word may be singular. Check if the plural form of the word is in the dictionary.
      elif(pluralWord in dictionaryWords):
        #Do not change the value of isEnglish
        pass
      else:
        #If all of these filters fail, the word is not in the dictionary, and the phrase is not in English.
        isEnglish = False
        logging.info(str(word) + " was entered but is not in dictionary.txt")
  #Return whether the sentence/phrase is in English or not.
  return isEnglish

def checkGuess(letterGuessed, answer, stateOfGuess):
  '''
  Checks if a given letter is in a word and updates the hangman string accordingly.
  
  If the guessed letter is in the word, prints the number of instances found. If not, prints "no instances found". Replaces asterisks in the hangman string with the letters found and returns this.

  Parameters
  ----------
  letterGuessed : str
    Letter being searched for inside of word.
  answer : str
    Hangman answer word.
  stateOfGuess : str
    State of the hangman guess (asterisks and letters)
  
  Returns
  -------
  str
    State of the hangman guess after letter has been searched for (asterisks and letters)

  Raises (this section is only applicable if your function raises an exception)
  ------
  TypeError
    If any of the parameters are not strings as they should be, return an error message.
  ValueError
    If the letter guessed is not an alpha character (letter), or is more than 1 letter long, raise an exception
  '''
  logging.debug("checkGuess called")

  #If any of the inputs are not strings, raise an exception and log a critical error
  if not isinstance (letterGuessed, str):
    raise TypeError("An unexpected error occurred.")
    logging.critical("Parameter letterGuessed is not a string in function isGuessCorrect")
  if not isinstance (answer, str):
    raise TypeError("An unexpected error occurred.")
    logging.critical("Parameter answer is not a string in function isGuessCorrect")
  if not isinstance (stateOfGuess, str):
    raise TypeError("An unexpected error occurred.")
    logging.critical("Parameter stateOfGuess is not a string in function isGuessCorrect")
  #If the letter guess input is not a letter, or is longer than 1 letter, raise an exception
  if not letterGuessed.isalpha():
    raise ValueError("Please enter a valid letter as your guess.")
  if len(letterGuessed)>1:
    raise ValueError("Please enter only one letter.")

  #Set a variable to count the instances of the letter
  letterCount = 0
  #For each letter in the word, check if the letter guess matches
  for index,letter in enumerate(answer):
    if letterGuessed==letter:
      logging.info("Found one " + str(letterGuessed) + " in " + str(answer))
      #If a matching letter is found, add one to the letter count
      letterCount+=1
      #Create a temporary list which holds the individual characters of the hangman guess (asterisks and letters)
      tempList = list(stateOfGuess)
      #Replace the asterisk at the given character location in the string with the guessed letter
      tempList[index] = letterGuessed
      logging.info(tempList)
      #Join the list of characters into a string and set the new guess state to this string
      stateOfGuess = ''.join(tempList)

  #If no letters were found, print the new state of the guess and a subsequent message. Return the new state of the guess.
  if letterCount == 0:
    print("There are no letter " + str(letterGuessed) + "'s.")
    print(str(stateOfGuess))
    return stateOfGuess
  #If only one letter was found, print the new state of the guess and a subsequent message. Return the new state of the guess.
  elif letterCount == 1:
    print("There is one letter " + str(letterGuessed) + ".")
    print(str(stateOfGuess))
    return stateOfGuess
  #If multiple letters were found, print the new state of the guess and a subsequent message. Return the new state of the guess.
  else:
    print("There are " + str(letterCount) + " letter " + str(letterGuessed) + "'s.")
    print (str(stateOfGuess))
    return stateOfGuess

def displayHangman(triesRemaining):
  '''
  Prints a picture of a hangman depending on the number of tries remaining.
  
  Uses rjust, and other string manipulation techniques to print text-art of a hangman.

  Parameters
  ----------
  triesRemaining : int
    A number between 0 and 6 representing the number of remaining tries in the hangman game.
  
  Returns
  -------
  None

  Raises (this section is only applicable if your function raises an exception)
  ------
  ExceptionType
    Describe why/how this exception gets raised
  '''
  logging.debug("displayHangman called")

  if not isinstance (triesRemaining, int):
    logging.critical("triesRemaining parameter in displayHangman function is not an int!")
    raise TypeError("An unexpected error occurred.")
  #Variably sized display variable that can be changed to accomodate different terminal sizes
  displaySize = 30
  #If there are 6 tries remaining, print a simple hanging bar
  if triesRemaining == 6:
    #Prints top of bar
    print("_"*displaySize)
    #For half the size of displaySize:
    for i in range (displaySize//2):
      #Prints bars on either side of the screen, one for the hanging bar and the other for the structural bar.
      if i<3:
        #rjust allows bar to be printed right beneath top, underscore bar
        print("|" + "|".rjust(displaySize, ' '))
      #Once 3 hanging bar extensions have been printed, continue printing the structural bar
      else:
        print("|")
    #Print base of hanging structure
    print("_"*(displaySize//3))

  #If 5 tries are remaining, print a head as well
  elif triesRemaining==5:
    print("_"*displaySize)
    for i in range (displaySize//2):
      if i<3:
        print("|" + "|".rjust(displaySize, ' '))
      #Prints a head on the next line after the hanging bar
      elif i==3:
        print("|" + "O".rjust(displaySize, ' '))
      else:
        print("|")
    print("_"*(displaySize//3))

  #If 4 tries are remaining, print a body as well
  elif triesRemaining==4:
    print("_"*displaySize)
    for i in range (displaySize//2):
      #i==4 added to create a new | character that will compose the body of the hangman
      if i<3 or i==4:
        print("|" + "|".rjust(displaySize, ' '))
      elif i==3:
        print("|" + "O".rjust(displaySize, ' '))
      else:
        print("|")
    print("_"*(displaySize//3))

  #If 3 tries are remaining, print one hand for the hangman
  elif triesRemaining==3:
    print("_"*displaySize)
    for i in range (displaySize//2):
      #i==5 prints another | character on the next line to continue the body shape
      if i<3 or i==5:
        print("|" + "|".rjust(displaySize, ' '))
      elif i==3:
        print("|" + "O".rjust(displaySize, ' '))
      #Print a slash representing the hangman's hand
      elif i==4:
        print("|" + "\|".rjust(displaySize, ' '))
      else:
        print("|")
    print("_"*(displaySize//3))

  #If two tries are remaining, print both arms.
  elif triesRemaining==2:
    print("_"*displaySize)
    for i in range (displaySize//2):
      if i<3 or i==5:
        print("|" + "|".rjust(displaySize, ' '))
      elif i==3:
        print("|" + "O".rjust(displaySize, ' '))
      elif i==4:
        #Two slashes represent arms of hangman. displaySize+1 required for rjust , since it will align based on "/", therefore to centre "|", character must be moved one right
        print("|" + "\|/".rjust(displaySize+1, ' '))
      else:
        print("|")
    print("_"*(displaySize//3))

  #If one try remains, print one leg for the hangman
  elif triesRemaining==1:
    print("_"*displaySize)
    for i in range (displaySize//2):
      if i<3 or i==5:
        print("|" + "|".rjust(displaySize, ' '))
      elif i==3:
        print("|" + "O".rjust(displaySize, ' '))
      elif i==4:
        print("|" + "\|/".rjust(displaySize+1, ' '))
      elif i==6:
        #displaySize-1 must be used to print the leg to the left of the "|" character representing the body above it
        print("|" + "/".rjust(displaySize-1, ' '))
      else:
        print("|")
    print("_"*(displaySize//3))
  
  #If no tries remain, print the complete hangman with 2 legs
  elif triesRemaining==0:
    print("_"*displaySize)
    for i in range (displaySize//2):
      if i<3 or i==5:
        print("|" + "|".rjust(displaySize, ' '))
      elif i==3:
        print("|" + "O".rjust(displaySize, ' '))
      elif i==4:
        print("|" + "\|/".rjust(displaySize+1, ' '))
      elif i==6:
        #\" causes a " to be printed, since \ is a special character. To print a \, \\ must be used. displaySize+1 used to align centre of legs with '|' character representing body in the previous line
        print("|" + "/ \\".rjust(displaySize+1, ' '))
      else:
        print("|")
    print("_"*(displaySize//3))
  return

def hangman():
  '''
  Plays a game of hangman with the user.
  
  Chooses a random word from the dictionary and prints all of its characters in asterisks. Asks user to guess letters in the word before 6 failures.

  Parameters
  ----------
  parameter1 : type
    description of parameter1
  parameter2 : type
    description of parameter2
  parameter3 : type, optional
    description of parameter3
  
  Returns
  -------
  type
    description of what's being returned
  
  Warnings (this section is optional)
  --------
  This is a free-text area that describes any warnings that could propogate
  in this program

  Raises (this section is only applicable if your function raises an exception)
  ------
  ExceptionType
    Describe why/how this exception gets raised
  '''
  logging.debug("hangman called")

  #Welcome message
  print("Welcome to hangman! I will pick a word from my dictionary and ask you to guess a letter in the word.".center(screenSize) + "\n" + "Be careful, you have only 6 tries to guess the word!".center(screenSize))
  #Pause so user can read message
  sleep(2)
  #Open the dictionary and read all lines
  dictionary = open('dictionary.txt', 'r')
  dictionaryWords = dictionary.readlines()
  dictionary.close()
  #Delete all newline characters in the dictionary.
  for index, word in enumerate(dictionaryWords):
    if word.endswith('\n'):
      dictionaryWords[index] = word[:-1]
  #logging.debug("Here's the words in the dictionary: " + str(dictionaryWords))
  
  #create a variable to hold the answer to the hangman game
  wordAnswer = ''
  #Search for random words in the dictionary until a word at least 3 characters long is found.
  while len(wordAnswer)<3:
    #Find a random word by looking for a random index in the dictionary
    wordAnswer = dictionaryWords[random.randint(0, (len(dictionaryWords)-1))]
  #Create a variable to hold the hangman guess string
  guessState = ""
  #Place an asterisk in the guess string for every character in the selected hangman word
  for character in wordAnswer:
    guessState+="*"
  logging.info("The chosen word is: " + str(wordAnswer))

  #Set a variable to hold the number of tries remaining.
  guessesLeft = 6
  #Create a list that holds all the letters previously guessed.
  lettersGuessed = []
  #stillGuessing will hold whether or not the word has been solved
  stillGuessing = True
  #As long as the word has not been solved and there are more than 0 tries remaining, allow the user to continue guessing
  while guessesLeft>0 and stillGuessing:
    #Display the corresponding hangman figure for the number of tries remaining.
    displayHangman(guessesLeft)
    #Print the number of guesses left
    print("You have " + str(guessesLeft) + " tries remaining.")
    #Print the state of the hangman guess
    print("Here's your word: " + str(guessState))

    #Ask user to enter a letter guess
    guess = input("Guess a letter in this word: ")
    #Convert the string to lowercase letters
    guess = guess.lower()
    if guess in lettersGuessed:
      #If the letter has already been guessed, tell the user to enter a different guess
      print("You've already guessed the letter " + str(guess) + ".")
      sleep(1)
      continue
    #Tries to call checkGuess function to see if guess is correct
    try:
      guessState = checkGuess(guess, wordAnswer, guessState)
    #Print any exceptions and restart the guessing loop if any are raised
    except Exception as e:
      print(str(e))
      continue
    else:
      #Add the guessed letter to the list of guessed letters
      lettersGuessed.append(guess)
    #If the guessed letter is not the word, take away one try
    if guess not in wordAnswer:
      guessesLeft-=1
    #If, at this point, all letters in the word have been guessed, display a success message and exit the loop using a break statement. Setting stillGuessing to False indicates that the guessing was successful.
    if guessState == wordAnswer:
      print("You have guessed the answer!\nThe word was: " + str(wordAnswer))
      stillGuessing = False
      break
    #If the word has not yet been guessed:
    else:
      #While loop to ensure a valid answer to the following question is given before moving on
      while True:
        #If there are still tries left, ask the user whether they would like to guess the word
        if guessesLeft>0:
          finalGuess = input("Would you like to guess the word?\n1. Yes\n0. No\n")
        else:
          #If no tries are left, ignore this while loop
          break
        #Check if the input is an appropriate integer. If not, raise an exception.
        try:
          #If the string is not a number, ask the user to enter an appropriate number.
          if not finalGuess.isdecimal():
            raise ValueError("Please enter an integer.")
          #Convert the string into an integer
          finalGuess = int(finalGuess)
          #If the user did not enter 0 or 1, ask the user to enter an appropriate number.
          if finalGuess!=0 and finalGuess!=1:
            raise ValueError("Please enter either 1 or 0")
        #Catch any errors from the above try block, print messages, and reset the loop if any are encountered.
        except ValueError as e:
          print(str(e))
          continue
        #If the user does wish to guess, ask them to enter a guess
        if finalGuess == True:
          guessedWord = input("Please enter your guess: ")
          #Strip any excess spaces before and after the guessed answer
          guessedWord = guessedWord.strip(' ')
          #If the guessed word is the same as the answer, print a success message and exit the function.
          if guessedWord.lower() == wordAnswer:
            print("You did it!")
            return
          #If the guessed word is not the same as the answer, print an error message and remove a try from the remaining guesses for the hangman game
          else:
            print("Uh oh. That isn't the word.")
            guessesLeft-=1
            #break statement exits the user-word-guess while loop
            break
        else:
          #Else break statement: If the user does not wish to guess the word right now, exit the user-word-guess while loop.
          break
  if guessesLeft<=0:
    #If there are 0 tries left, print a game over message and exit the function
    displayHangman(guessesLeft)
    print("You have lost. The answer was: " + str(wordAnswer))
  return
  
def percentComp(searchedWord):
  logging.debug("percentComp called")

  '''
  Finds the percentage of a particular word to the total number of words in Macbeth.
  
  Takes in an English word to search for in Macbeth, and finds its frequency. Then finds percentage of this word compared to total words.

  Parameters
  ----------
  searchedWord : str
    Singular, English word not containing any non-alpha characters to be searched for inside the Macbeth file.

  Returns
  -------
  float
    Returns a percentage that represents number of discovered instances of given word to total words in dictionary.

  Raises
  ------
  ValueError
    If the searchedWord parameter is not a string as it should be, raise an exception.
  ValueError
    If the searchedWord is not in English or includes spaces, apostrophes or other non-alpha characters, raise an exception.
  '''
  #If searchedWord is not a string, raise an error and log a critical flaw
  if not isinstance(searchedWord, str):
    logging.critical("Parameter searchedWord into function percentComp is not a string!")
    raise ValueError("An unexpected error occurred")
  #If the searchedWord includes non-alpha characters, raise an exception
  if not searchedWord.isalpha():
    raise ValueError("Please choose a word without punctuations/special characters/numbers".center(screenSize))
  #If the word searched is not in English, raise an Exception
  if not checkEnglish(searchedWord):
    raise ValueError("Hmm. That doesn't seem like an English word! If you think it is, please add it to my dictionary.".center(screenSize))
  #Opens macbeth file and reads all the lines
  macbeth = open('story.txt', 'r')
  macbethLines = macbeth.readlines()
  macbeth.close()
  #Make a list to hold all the words
  macbethWords = []
  #Split the lines into words
  for line in macbethLines:
    #Delete any newline characters by slicing to -1
    if line.endswith('\n'):
      line = line[:-1]
    #Split the current line into a list of words
    words = line.split(' ')
    #For each word in the list, add it to macbethWords
    macbethWords.extend(words)
  #Find number of words in Macbeth
  numOfWords = len(macbethWords)
  logging.info("There are " + str(numOfWords) + " words in Macbeth")
  #Set a variable to count the number of discovered instances of a word in Macbeth
  wordCount=0
  #Iterate through all the words in Macbeth
  for word in macbethWords:
    #If the searched word matches the word in Macbeth, add 1 to the count
    if searchedWord.lower() == word.lower():
      wordCount+=1
    #Else, if the length of the word is greater than 1 and the final character in the word is taken away (whether it is a space or a letter 's'), add one to the count if the searchedWord matches the indexed word
    elif len(word)>1 and searchedWord.lower() == word[:-1].lower():
      wordCount+=1
  logging.info("There are " + str(wordCount) + " '" + str(searchedWord) + "'s  in Macbeth")
  #Find the percent composition of the word and return it
  percentage = (wordCount/numOfWords)*100
  logging.info("The total percentage is " + str(percentage))
  return percentage

def findAndReplace(searchedWord):
  '''
  Finds and replaces given words in Macbeth.
  
  Takes in a word to find in Macbeth and prints all instances of the word in the play. Asks the user if they would like to replace all instances of this word in the text file, and does so.

  Parameters
  ----------
  searchedWord : str
    Singular, English word not containing any non-alpha characters to be searched for inside the Macbeth file.
  
  Returns
  -------
  None
  
  Raises
  ------
  ValueError
    If the searchedWord parameter is not a string as it should be, raise an exception.
  ValueError
    If the searchedWord is not in English or includes spaces, apostrophes or other non-alpha characters, raise an exception.
  Exception
    If, when the user is asked whether they would like to replace words or not, the input escapes a series of filters, print an error message.
  '''
  logging.debug("findAndReplace called")

  #If searchedWord is not a string, raise an error and log a critical flaw
  if not isinstance(searchedWord, str):
    raise ValueError("An unexpected error occurred")
    logging.critical("Parameter searchedWord into function findAndReplace is not a string!")
  #If the searchedWord includes non-alpha characters, raise an exception
  if not searchedWord.isalpha():
    raise ValueError("Please choose a word without punctuations/special characters/numbers")
  #If the word searched is not in English, raise an Exception
  if not checkEnglish(searchedWord):
    raise ValueError("Hmm. That doesn't seem like an English word! If you think it is, please add it to my dictionary.")
  #Opens macbeth file and reads all the lines
  macbeth = open('story.txt', 'r')
  macbethLines = macbeth.readlines()
  macbeth.close()
  #Make a list to hold all indexes in the file that contain instances of the word
  instances = []
  for index, line in enumerate(macbethLines):
    #Delete any newline characters by slicing to -1
    if line.endswith('\n'):
      macbethLines[index] = line[:-1]
    #If the searched word is found, add the index of the subsequent line to instances list
    if searchedWord.lower() in line.lower():
      instances.append(index)

  logging.debug("Found word at " + str(instances))
  #If there are instances of the word, print the number of instances and the line where they are
  if len(instances) != 0:
    #Print total instances
    print(str(len(instances)) + " instances of " + str(searchedWord) + " were found:")
    #Print each line where searchedWord was found
    for i in range (len(instances)-1):
      print("Line " + str(instances[i]) + ": '" + str(macbethLines[instances[i]]) + "'")
    #While loop runs until replace is handled
    while True:
      #Ask the user if they would like to use the replace function
      print("Would you like to replace all instances of this word with another?".center(screenSize) + "\n1. Yes\n0. No")
      performReplace = input()
      try:
        #Check if the input is an appropriate integer. If not, print a custom error message
        if not performReplace.isdecimal():
          raise ValueError ("Please choose an appropriate integer answer.".center(screenSize))
        #Convert the integer
        performReplace = int(performReplace)
        #If the integer is not 1 or 0, raise an exception
        if performReplace != 0 and performReplace != 1:
          raise ValueError("Please enter either 1 or 0.".center(screenSize))
      #Catch all errors from previous try block
      except ValueError as e:
        #If there is an error in answering the question, restart the while loop
        print(str(e))
        continue
      #If no errors were encountered, check whether the user wishes to replace or not
      if performReplace:
        #If the user does wish to replace, ask them to enter a replacing word
        replacingWord = input("Choose a word to replace the findings with: ")
        try:
          #Check if the word includes any special characters. If it does, raise an exception.
          if not replacingWord.isalpha():
            raise ValueError("Please choose a word without punctuations/special characters/numbers".center(screenSize))
          #If the replacing word is too short, ask user to enter a longer word.
          if len(replacingWord)<2:
            raise ValueError("Please enter at least two characters".center(screenSize))
        except ValueError as e:
          #Catch any errors and restart the while loop if any are found
          print(str(e))
          continue
        #If no errors are encountered from the try block:
        else:
          #Replace the words
          for index in range (len(instances)-1):
            #Run a for loop which cycles through every entry in instances list
            #Each value in instances corresponds to an index where the found word was discovered (therefore macbethLines[instances[index]])
            #User .replace() to find and replace the word in lowercase form by converting the whole line to lowercase and searching for similar words
            #Replace is happening to a list which holds collected lines from Macbeth
            macbethLines[instances[index]] = macbethLines[instances[index]].lower().replace(str(searchedWord.lower()), str(replacingWord))
            logging.debug("Replaced: " + str(macbethLines[instances[index]]))
          #Open macbeth in write mode and rewrite the altered file contents with a newline. Display a success message and exit the function
          macbeth = open('story.txt', 'w')
          for line in macbethLines:
            macbeth.write(str(line) + '\n')
          print("Completed replace.")
          macbeth.close()
          return
      #If the user does not want to perform the replacement, exit the function
      elif not performReplace:
        return
      #If neither of these options is true, record this fatal error
      else:
        logging.critical("Variable performReplace in findAndReplace is not 1 or 0: " + str(performReplace))
        raise Exception("An unexpected error occurred.")
  #If no search results were found for the word in the first place, print this message and exit the loop.
  else:
    print("No instances of this word were found.")
  return

def readCharacterLines(characterSelected):
  '''
  Prints all lines said by a specific character
  
  Looks for character line cue (name in capital letters), and prints line number, as well as proceeding lines until another character's lines are encountered.

  Parameters
  ----------
  characterSelected : str
    String containing name of selected character in lowercase letters (inputted by user)
  
  Returns
  -------
  None
  
  Raises
  ------
  LookupError
    If the user did not enter the correct name of a given character to read the lines of, raise an exception.
  '''
  logging.debug("readCharacterLines called")

  #List of all the characters whose lines can be read.
  characterList = ["macbeth","duncan","banquo","macduff","malcolm","ross","first witch","second witch","third witch","lady macbeth","donalbain","fleance","young siward","siward","seyton","lennox","porter","doctor","servant","hecate"]
  #If the selected character is not in the list of characters, raise an exception
  if characterSelected.lower() not in characterList:
    raise LookupError ("That character does not exist, does not have enough significant lines, or has been incorrectly entered")
  #Read all lines in Macbeth
  macbeth = open('story.txt', 'r')
  macbethLines = macbeth.readlines()
  macbeth.close()
  #Remove all newline characters
  for index in range (len(macbethLines)-1):
    if macbethLines[index].endswith('\n'):
      macbethLines[index]=macbethLines[index][:-1]
  #for each line in Macbeth, check if the current line is the uppercase version of the character's name, indicating a line cue.
  for index, line in enumerate(macbethLines):
    if characterSelected.upper() == line:
      #If the line cue is found, print the line number and the character's line cue
      print("Line " + str(index) + '\n' + str(macbethLines[index]))
      #Go to the next line
      indexedLine = index + 1
      #Keep printing lines until 1. the end of the play has been reached 2. If the line is a newline 3. The first word is "Exeunt", meaning the scene has ended 4. The first word is "Enter" or "Exit" and 5. The line does not include only uppercase letters (indicating a different character line cue)
      while (indexedLine < len(macbethLines)-1) and (macbethLines[indexedLine] != '') and (macbethLines[indexedLine][0:7] != "Exeunt") and (macbethLines[indexedLine][0:5]!="Enter") and (macbethLines[indexedLine][0:4]!="Exit") and (not macbethLines[indexedLine].isupper()):
        #print the line, go to the next one
        print(macbethLines[indexedLine])
        indexedLine+=1
      #Print a newline so further instructions can be read
      print()
  return

def findVoterID():
  '''
  Gives a chronological number to the next vote.
  
  Reads vote data file and checks for what the next voter's ID number will be.

  Parameters
  ----------
  None
  
  Returns
  -------
  int
    Returns a number which corresponds to the latest chronological ID to be printed

  Raises
  ------
  LookupError
    If the voter ID cannot be found in the data file.
  '''
  logging.debug("findVoterID called")

  #Open the file and read the text
  voters = open('data.txt', 'r')
  voterData = voters.readlines()
  #Read the second-last line in the file, which will contain the voter ID
  #Ignore the first 10 characters "Voter ID: " and read the number only
  #Add one to the number
  try:
    voterID = int(voterData[-2][10:-1]) + 1
  #If something goes wrong (e.g. not in range error, print an error message)
  except LookupError:
    print("Couldn't find voter ID")
  except Exception as e:
    print(str(e))
  voters.close()
  return voterID
  
def generateVotes(population):
  '''
  Creates a given number of random votes for candidates 1-3.
  
  Takes in a number of votes which need to be produced, and uses the random function to assign a vote to each ID, writing the votes to the data file.

  Parameters
  ----------
  population : int
    Takes in a number of voters to generate votes for.
  
  Returns
  -------
  Nothing

  Raises
  ------
  TypeError
    Given population for voters is not an integer.
  ValueError
    User selected more than 10 000 voters or less than 1 voter
  '''
  logging.debug("generateVotes called")

  if not isinstance (population, int):
    raise TypeError("Please enter a positive integer for the number of voters you would like to generate.")
  if population>1000000 or population<1:
    raise ValueError("Please enter a value between 1 and 1000000 for the number of voters.")
  #Opens file to "append"
  voters = open('data.txt', 'a')
  #Gets latest voter ID
  voterNum = findVoterID()

  #Iterates through a for loop to create votes for each voterID
  for i in range (0, population):
    #Generate a vote for a random politician
    vote = random.randint(1, 3)
    #Creates a newline, so that appended lines are on a new line
    voters.write('\n')
    #Stamps new voter ID and creates a new line
    voters.write("Voter ID: " + str(voterNum))
    voters.write('\n')
    #Writes vote to file, creates a new line
    voters.write(str(vote))
    #Ensuring proper voter ID is written
    #logging.info('Writing: "Voter ID: ' + str(voterNum)+'\n'+str(vote)+'\n')
    #Iterate to next voter ID
    voterNum+=1
  voters.close()
  return

def countVotes():
  '''
  Reads voter data file and counts votes given to each politician, returning election results.
  
  Opens voter data file and reads every other line (corresponding to votes only - ignoring voter ID), and adds to tally for each politician.

  Parameters
  ----------
  None
  
  Returns
  -------
  dictionary{"Politician Name":votes(int), ...}
    Returns a dictionary containing three keys, where each key contains the politician's full name, and each value contains the number of votes the politician received.

  Raises
  ------
  Exception
    If the random function experiences an error and selects a vote for a politician which is out of range.
  '''
  logging.debug("countVotes called")

  voters = open('data.txt', 'r')
  results = voters.readlines()
  #Initiates vote tally at 0
  voteTally = {'Justin Trudeau':0, 'Andrew Scheer':0, 'Jagmeet Singh':0}
  #Logging to ensure tallying is representing proper votes as given in data file
  logging.debug("Votes as detected: ")
  #Runs through a loop to check every other line and determine what votes have been casted
  for voter in range (1, len(results), 2):
    #Checks data file and looks for the first character (i.e. integer corresponding to politician selected)
    vote = int(results[voter][0])
    #Prints detected vote to ensure that the correct characters are being read
    #logging.debug(str(vote))
    #A vote of 1 corresponds to Justin Trudeau, 2 to Andrew Scheer and 3 to Jagmeet Singh. Adds 1 to integer value assigned to the tally of the corresponding politician's votes
    if vote == 1:
      voteTally['Justin Trudeau']+=1
    elif vote == 2:
      voteTally['Andrew Scheer']+=1
    elif vote == 3:
      voteTally['Jagmeet Singh']+=1
    else:
      raise Exception('A voter ruined their ballot by picking someone outside of the range of candidates.')
  voters.close()
  #Log to check whether votes have been counted correctly
  logging.info("Final votes: " + str(voteTally))
  return voteTally

def generateResults(result):
  '''
  Prints a short statement summarizing the results of the election and tally.
  
  Takes in tally of the results and interprets the winner. Prints a summary of votes given to each candidate as well as who the winner is (or if a tie occured).

  Parameters
  ----------
  result : dictionary{"Politician name":votes(int),...}
    This function requires a tally of the election results in a dictionary which has a name corresponding to a number of votes
  
  Returns
  -------
  Nothing

  Raises
  ------
  TypeError
    If the election results were not presented in a dictionary to this function.
  Exception
    If a possible situation/outcome for the votes is not caught.
  '''
  logging.debug("generateResults called")

  #Check if result data is in the proper form
  if not isinstance(result, dict):
    raise TypeError ("Results of the election were not delivered in a dictionary.")
  #Print total number of votes for each politcian
  print("Here are the results:".center(screenSize))
  outputString = "Justin Trudeau: " + str(result['Justin Trudeau'])
  print(outputString.center(screenSize))
  outputString = "Andrew Scheer: " + str(result['Andrew Scheer'])
  print(outputString.center(screenSize))
  outputString = "Jagmeet Singh: " + str(result['Jagmeet Singh'])
  print(outputString.center(screenSize))
  #Checks win situations
  #If Justin Trudeau gets more votes than both
  if result['Justin Trudeau']>result['Jagmeet Singh'] and result['Justin Trudeau']>result['Andrew Scheer']:
    print("The winner is Justin Trudeau".center(screenSize))
  #If Andrew Scheer gets more votes than both
  elif result['Andrew Scheer']>result['Jagmeet Singh'] and result['Andrew Scheer']>result['Justin Trudeau']:
    print("The winner is Andrew Scheer".center(screenSize))
  #If Jagmeet Singh gets more votes than both
  elif result['Jagmeet Singh']>result['Justin Trudeau'] and result['Jagmeet Singh']>result['Andrew Scheer']:
    print("The winner is Jagmeet Singh".center(screenSize))
  #If Justin and Jagmeet tie
  elif result['Justin Trudeau']==result['Jagmeet Singh'] and result['Justin Trudeau']>result['Andrew Scheer']:
    print("It is a tie between Justin Trudeau and Jagmeet Singh".center(screenSize))
  #If Justin and Andrew Scheer tie
  elif result['Andrew Scheer']==result['Justin Trudeau'] and result['Andrew Scheer']>result['Justin Trudeau']:
    print("It is a tie between Justrin Trudeau and Andrew Scheer".center(screenSize))
  #If Andrew Scheer and Jagmeet tie
  elif result['Jagmeet Singh']==result['Andrew Scheer'] and result['Jagmeet Singh']>result['Justin Trudeau']:
    print("It is a tie between Jagmeet Singh and Andrew Scheer".center(screenSize))
  elif result['Jagmeet Singh'] == result['Andrew Scheer'] and result['Andrew Scheer']==result['Justin Trudeau']:
    print("It is a three-way tie".center(screenSize))
  #If nothing was detected, rais an error.
  else:
    raise Exception('Error determining winner.')
  return

def slope(x1, y1, x2, y2):
  '''
  Finds the slope of a given line
  
  If two of the given x-values are equivalent and the y-values are not, return "undefined" as the answer. Otherwise, return deltaY/deltaX

  Parameters
  ----------
  x1 : float
    X-coordinate of first point.
  y1 : float
    Y-coordinate of first point
  x2 : float
    X-coordinate of second point.
  y2 : float
    Y-coordinate of second point.

  Returns
  -------
  str, float
    returns a float representing the slope of the line, or "undefined" if the slope is not defined.
  '''
  logging.debug("slope called")

  #If the x values are equal and the y-values are not, return 'undefined'
  if x1==x2 and y1!=y2:
    logging.info("undefined slope detected")
    return "undefined"
  #If the 2 points are the same, leave the slope as undefined
  elif x1==x2 and y1==y2:
    logging.info("point on point slope detected")
    return "undefined"
  #Otherwise, calculate the slope of the line and return it
  else:
    logging.info(str((y2-y1)/(x2-x1)))
    return (y2-y1)/(x2-x1)

def translate(xTranslate, yTranslate, trianglePoints):
  '''
  Translates a triangle horizontally and vertically.
  
  Takes in a value for translation size and a dictionary continaing the points, and adds the x-translation to the x-value of each point, and the y-translation to the y-value.

  Parameters
  ----------
  xTranslate : float
    Represents the user-inputted positive or negative amount to shift the triangle in the x direction.
  yTranslate : float
    Represents the user-inputted positive or negative amount to shift the triangle in the y direction.
  trianglePoints : dict['Coordinate':value]
    Dictionary containing the coordinates of each triangle point and its value in a float
  
  Returns
  -------
  dict['Coordinate':value]
    Returns the dictionary containing all coordinates and their values

  Raises (this section is only applicable if your function raises an exception)
  ------
  TypeError
    If xTranslate and yTranslate are not strings when first entered, or cannot be converted to floats, raise an error.
  '''
  logging.debug("translate called")

  #Check to see if the parameters are of the right type, and can be converted:
  if not isinstance (xTranslate, str):
    raise TypeError("An unexpected error occurred.")
  if not isinstance (yTranslate, str):
    raise TypeError("An unexpected error occurred.")
  xTranslate = float(xTranslate)
  yTranslate = float(yTranslate)
  #Add the x translation to all the x-coordinates
  trianglePoints['xA'] += xTranslate
  trianglePoints['xB'] += xTranslate
  trianglePoints['xC'] += yTranslate
  #Add the y translation to all the y-coordinates
  trianglePoints['yA'] += yTranslate
  trianglePoints['yB'] += yTranslate
  trianglePoints['yC'] += yTranslate
  logging.debug("New points: " + str(trianglePoints))
  return trianglePoints

def rotate(rotationAngle, centreOfRotationX, centreOfRotationY, trianglePoints):
  '''
  Rotates a triangle around a particular centre of rotation by either 90, 180, or 270 degrees.
  
  Checks how much the user wants to rotate the triangle as well as what the centre of rotation is, and uses properties about the distances from the triangle points to the centre to find the rotated image points.

  Parameters
  ----------
  rotationAngle : int
    An integer, 1 representing 90 degrees CW, 2 representing 180 degrees and 3 representing 90 degrees CCW, inputted by the user.
  centreOfRotationX : float
    X-coordinate of centre of rotation point.
  centreOfRotationY : float
    Y-coordinate of centre of rotation point.
  trianglePoints : dict['Coordinate':value]
    Dictionary containing the coordinates of each triangle point and its value in a float
  
  Returns
  -------
  dict['Coordinate':value]
    Returns the dictionary containing all triangle image coordinates and their values

  Raises
  ------
  TypeError
    If rotationAngle is not a valid integer, centreOfRotationX is not a valid float, or centreOfRotationY is not a valid float, raise an exception
  '''
  logging.debug("rotate called")
  #Ensuring all parameters are of the right type
  if not isinstance (rotationAngle, int):
    raise TypeError("An unexpected error occurred.")
  if not isinstance (centreOfRotationX, float):
    raise TypeError("An unexpected error occurred.")
  if not isinstance (centreOfRotationY, float):
    raise TypeError("An unexpected error occurred.")

  #If rotating 90 degrees CW
  if rotationAngle == 1:
    #Find x distance to point A and y distance to point A from centre of rotation
    xDistance = trianglePoints['xA'] - centreOfRotationX
    yDistance = trianglePoints['yA'] - centreOfRotationY
    logging.debug("xDistance for A: " + str(xDistance))
    logging.debug("yDistance for A: " + str(yDistance))
    #Add the y distance to the centre of rotation x coordinate to get the image point A' x-coordinate
    trianglePoints['xA'] = centreOfRotationX + yDistance
    #Subtract the x distance from the centre of rotation y coordinate to get the image point A' y-coordinate
    trianglePoints['yA'] = centreOfRotationY - xDistance

    #Repeat with B
    xDistance = trianglePoints['xB'] - centreOfRotationX
    yDistance = trianglePoints['yB'] - centreOfRotationY
    logging.debug("xDistance for B: " + str(xDistance))
    logging.debug("yDistance for B: " + str(yDistance))
    trianglePoints['xB'] = centreOfRotationX + yDistance
    trianglePoints['yB'] = centreOfRotationY - xDistance

    #Repeat with C
    xDistance = trianglePoints['xC'] - centreOfRotationX
    yDistance = trianglePoints['yC'] - centreOfRotationY
    logging.debug("xDistance for C: " + str(xDistance))
    logging.debug("yDistance for C: " + str(yDistance))
    trianglePoints['xC'] = centreOfRotationX + yDistance
    trianglePoints['yC'] = centreOfRotationY - xDistance


  #If the rotation angle is 180 degrees:
  elif rotationAngle == 2:
    #Find the x-distance to the centre of rotation from each point and subtract it from the x value of the centre of rotation to get the image point x-coordinate
    trianglePoints['xA'] = centreOfRotationX - (trianglePoints['xA'] - centreOfRotationX)
    trianglePoints['xB'] = centreOfRotationX - (trianglePoints['xB'] - centreOfRotationX)
    trianglePoints['xC'] = centreOfRotationX - (trianglePoints['xC'] - centreOfRotationX)

    #Find the y-distance to the centre of rotation from each point and subtract it from the y value of the centre of rotation to get the image point y-coordinate
    trianglePoints['yA'] = centreOfRotationY - (trianglePoints['yA'] - centreOfRotationY)
    trianglePoints['yB'] = centreOfRotationY - (trianglePoints['yB'] - centreOfRotationY)
    trianglePoints['yC'] = centreOfRotationY - (trianglePoints['yC'] - centreOfRotationY)

  #If rotating 90 degrees CCW
  elif rotationAngle == 3:
    #Find x distance to point A and y distance to point A from centre of rotation
    xDistance = trianglePoints['xA'] - centreOfRotationX
    yDistance = trianglePoints['yA'] - centreOfRotationY
    logging.debug("xDistance for A: " + str(xDistance))
    logging.debug("yDistance for A: " + str(yDistance))
    #Add the y distance to the centre of rotation x coordinate to get the image point A' x-coordinate
    trianglePoints['xA'] = centreOfRotationX - yDistance
    #Subtract the x distance from the centre of rotation y coordinate to get the image point A' y-coordinate
    trianglePoints['yA'] = centreOfRotationY + xDistance

    #Repeat with B
    xDistance = trianglePoints['xB'] - centreOfRotationX
    yDistance = trianglePoints['yB'] - centreOfRotationY
    logging.debug("xDistance for B: " + str(xDistance))
    logging.debug("yDistance for B: " + str(yDistance))
    trianglePoints['xB'] = centreOfRotationX - yDistance
    trianglePoints['yB'] = centreOfRotationY + xDistance

    #Repeat with C
    xDistance = trianglePoints['xC'] - centreOfRotationX
    yDistance = trianglePoints['yC'] - centreOfRotationY
    logging.debug("xDistance for C: " + str(xDistance))
    logging.debug("yDistance for C: " + str(yDistance))
    trianglePoints['xC'] = centreOfRotationX - yDistance
    trianglePoints['yC'] = centreOfRotationY + xDistance
  
  logging.debug("New points: " + str(trianglePoints))
  #Return the image triangle
  return trianglePoints




#------------------------ MAIN CODE -----------------------#
#Create a global variable to control size of screen (and adjust alignment of text)
screenSize = 150
#--------------------- LOGIN HANDLING -------------------#
#Read all usernames and passwords
try:
  userData = readUserData()
except Exception as e:
  print("An unexpected error occurred")
  logging.critical(str(e))

#Welcome message
print("Welcome! To access these top secret tools, you require an account.".center(screenSize))

#Ask user whether they would like to login or not, and verify their login
while True:
  try:
    checkAccountStatus(userData)
  except Exception as e:
    print(str(e))
  else:
    break
#---------------- EXTRACT ENGLISH WORDS FROM MACBETH AND TEXTS TO DICTIONARY --------------#
print("Logging in and prepping...".center(screenSize))
print("This will take a short while...".center(screenSize))
print("Please stay patient while I read from enormous text files to create an English dictionary...".center(screenSize))
#Open Macbeth as read
macbeth = open('story.txt', 'r')
#Read all the lines
macbethLines = macbeth.readlines()
#Close the file, add all words to the dictionary
macbeth.close()
#Add all words from Macbeth to the dictionary
try:
  addToDictionary(macbethLines)
except Exception as e:
  print(str(e))

#Open rest of the texts as read only
moreStories = open('moreStories.txt', 'r')
#Read all the lines
moreStoriesLines = moreStories.readlines()
#Close the file, add all words to the dictionary
moreStories.close()
#Add all words from other stories to the dictionary
try:
  addToDictionary(moreStoriesLines)
except Exception as e:
  print(str(e))

#Delete to conserve memory space
del moreStoriesLines
del macbethLines
#-------------------------------------- MAIN MENU -----------------------------------------#
#Set a variable that determines whether to continue running the menu or not
usingApp = True
#Menu while loop
while usingApp:
  while True:
    #Print the menu until an appropriate answer is given (while True loop)
    print("*"*screenSize)
    print("What would you like to do?".center(screenSize) + "\n" + "1. Teach me English!".center(screenSize) + "\n" + "2. Test my English skills!".center(screenSize) + "\n" + "3. Let's play Hangman!".center(screenSize) + "\n" + "4. Find the percent composition of a word in Macbeth.".center(screenSize) + "\n" + "5. Find and Replace a word in Macbeth.".center(screenSize) + "\n" + "6. Read all of a character's lines in Macbeth.".center(screenSize) + "\n" + "7. Run an election.".center(screenSize) + "\n" + "8. Perform transformations on a triangle.".center(screenSize) + "\n" + "0. Exit.".center(screenSize))
    print("*"*screenSize)
    ans = input()
    #Try to convert the answer to an integer
    #If this does not work, or the integer entered is not between 0 and 8, print an error message
    try:
      ans = int(ans)
      if ans<0 or ans>8:
        raise ValueError()
      break
    except ValueError:
      print("Please pick an integer between 0 and 8".center(screenSize))
  #Check user input and call appropriate function based on input
  #Add to dictionary function
  if ans == 1:
    #Asks user to enter a valid English phrase
    userPhrase = input("Please enter a phrase or document with all the words in English, and I will add new words to my dictionary.".center(screenSize) + "\n" + "Please note that I cannot validate your answer, so ensure you really ARE entering an English phrase.".center(screenSize) + "\n")
    #Put userPhrase into a list, since this is how it is expected by addToDictionary
    userPhrase = [userPhrase]
    try:
      #Add the user's phrase to the dictionary and display a success message
      addToDictionary(userPhrase)
      print("Okay, I added all applicable words to my dictionary.".center(screenSize))
    #Catch any errors
    except Exception as e:
      print(str(e))
  
  #Test English function
  elif ans == 2:
    #Ask user to enter a phrase in English and verify whether it is or is not in English
    print("Enter a sentence/paragraph, and I will determine whether what you typed is in English or not.".center(screenSize) + "\n" + "Note that this function works best when there are no non-alpha characters, other than punctuation in the sentence.".center(screenSize))
    userSentence = input("Enter a phrase: ")
    #Set variable isEnglish to an out-of-scope number (should be 1 or 0) to catch any errors
    isEnglish = 3
    try:
      #Check whether the given phrase is in English
      isEnglish = checkEnglish(userSentence)
    except Exception as errorMessage:
      #Catch any errors
      print("An error occurred: " + str(errorMessage))
    else:
      #If the function runs successfully:
      #If the phrase is not in English, print the subsequent message
      if not isEnglish:
        print("You have entered a phrase which is either not in English, or includes special characters which I cannot read!".center(screenSize))
      #If the phrase is in English, print the subsequent message.
      elif isEnglish:
        print("This phrase is in English!".center(screenSize))
      else:
        #If any unexpected errors occurred, restart the loop
        continue
      
      #Ask user a question and engage a loop until answered
      while True:
        #Ask user if answer was correct
        answerCorrect = input("Was my answer correct?".center(screenSize) + "\n1. Yes\n0. No\n")
        try:
          #Check to see if answerCorrect can be changed to an integer and is between 0 and 1. If not, raise an exception and restart the loop, otherwise break out of the loop
          answerCorrect = int(answerCorrect)
          if answerCorrect!=0 and answerCorrect!=1:
            raise ValueError()
        except:
          print("Please enter either 1 or 0.".center(screenSize))
          continue
        else:
          break
      
      #If the answer was correct, print a success message and exit
      if answerCorrect:
        print("Thanks for the feedback!".center(screenSize))
      #If the answer was incorrect and the phrase was not in English, add all new words to the English dictionary
      elif not answerCorrect and not isEnglish:
        try:
          #Add words to English dictionary by putting it in a list first (this is how it is expected by userSentence)
          userSentence = [userSentence]
          addToDictionary(userSentence)
        #Catch any errors in running function
        except Exception as e:
          print(str(e))
        else:
          print("I added new words to my dictionary. Thanks.".center(screenSize))
      #If the answer is incorrect but the phrase is in English, the user may be speaking incorrectly. Print subsequent message.
      elif not answerCorrect and isEnglish:
        print("Hmm. Perhaps thou hast spoken Shakespearean English without knowing it!".center(screenSize))

  #Hangman
  elif ans == 3:
    #Call hangman function and catch any exceptions
    try:
      hangman()
    except Exception as e:
      print("An unexpected error occurred")
      logging.critical(str(e))
  
  #Percent Composition of Word in Macbeth function
  elif ans == 4:
    #Ask user to enter a word search, and do not exit loop until acceptable answer is given
    while True:
      print("Please enter a word which you would like to search for. Do not search for a word with non-alphabetic characters.".center(screenSize))
      word = input()
      #Create a variable to hold the answer
      wordPercent = 0
      try:
        #Try to run the word search
        wordPercent = percentComp(word)
      #Catch any errors and restart the loop if they occur
      except Exception as errorMessage:
        print(str(errorMessage))
        continue
      #If everything works well, print the final message and exit the loop
      else:
        outputString = '"' + str(word) + '" makes up ' + str(wordPercent) + "% of Macbeth."
        print(outputString.center(screenSize))
        break

  #Find and Replace function
  elif ans == 5:
    #While True loop continues running until acceptable answer has been given for question
    while True:
      print("Please enter a word to find in Macbeth.".center(screenSize))
      word = input()
      try:
        #Check if findAndReplace function can be run
        findAndReplace(word)
      except Exception as e:
        #Catch and print any errors, then reset the loop
        print(str(e))
        continue
      else:
        #If function runs without error, break out of loop
        break
  
  #Read all of a particular character's lines in Macbeth
  elif ans == 6:
    while True:
      #Ask user to choose a character from a list
      print("Choose a character to read lines from (type name):".center(screenSize))
      sleep(2)
      print('*'*screenSize)
      print("Macbeth".center(screenSize) + "\n" + "Duncan".center(screenSize) + "\n" + "Banquo".center(screenSize) + "\n" + "Macduff".center(screenSize) + "\n" + "Malcolm".center(screenSize) + "\n" + "Ross".center(screenSize) + "\n" + "First Witch".center(screenSize) + "\n" + "Second Witch".center(screenSize) + "\n" + "Third Witch".center(screenSize) + "\n" + "Lady Macbeth".center(screenSize) + "\n" + "Donalbain".center(screenSize) + "\n" + "Fleance".center(screenSize) + "\n" + "Young Siward".center(screenSize) + "\n" + "Siward".center(screenSize) + "\n" + "Seyton".center(screenSize) + "\n" + "Lennox".center(screenSize) + "\n" + "Porter".center(screenSize) + "\n" + "Doctor".center(screenSize) + "\n" + "Servant".center(screenSize) + "\n" + "Hecate".center(screenSize))
      print('*'*screenSize)
      chosenCharacter = input()
      chosenCharacter=chosenCharacter.lower()
      try:
        #Try to read the character's lines
        readCharacterLines(chosenCharacter)
      except Exception as e:
        #Catch any errors and restart while loop
        print(str(e))
        continue
      else:
        #If no issues occur, exit while loop and function
        break
  
  #Voter election function
  elif ans == 7:
    while True:
      #Creates a intro message which asks user whether they would like to generate votes or not
      asking = input("This program runs an imaginary 'election', where candidates are chosen at random and given random votes. Would you like to generate votes?".center(screenSize) + "\n1. Yes\n0. No\n")
      try:
        #Checks if the input can be converted to an int
        asking = int(asking)
      except Exception:
        #Catch exception
        print("An error occurred.")
      #If answer is 1 or 0, break out of question loop
      if asking == 0 or asking == 1:
        break
      else:
        #Otherwise, ask the user to choose a valid answer
        print("Please choose a valid option.")
    #Keeps asking to generate new votes while user continues to wish so
    while asking:
      #Asks for a number of votes and calls the generate votes function
      loop = True
      while loop:
        print("How many votes would you like to generate? Pick a number between 1 and 1000000.".center(screenSize))
        numOfVotes = input()
        try:
          #Try to convert answer to an integer
          numOfVotes = int(numOfVotes)
          generateVotes(numOfVotes)
        except Exception as e:
          #Catch and print any errors, continue looping
          print("An error occurred".center(screenSize))
          print("Please enter a valid integer.".center(screenSize))
          loop = True
        else:
          break
          #If everything works, break out of loop
      
      #Asks if the user wishes to continue generating votes
      while loop:
        asking = input("Would you like to generate more votes?".center(screenSize) + "\n1. Yes\n0. No\n")
        try:
          #See if given answer was 1 or 0
          asking = int(asking)
          if asking != 0 and asking !=1:
            raise ValueError("Please select a valid option (1 or 0).".center(screenSize))
        except Exception as e:
          #If you run into an error, print the error and reset the loop
          print("An error occurred".center(screenSize))
          continue
        else:
          #If everything done correctly, exit while loop
          break
      #If the user wishes to continue generating votes (asking == 1), continue loop, otherwise break (if asking == False)
      if asking == 0:
        break
      elif asking == 1:
        pass

    #Tallies the votes and prints the results
    try:
      finalTally = countVotes()
      generateResults(finalTally)
    except Exception as e:
      #Catch any errors
      print("An error occurred: " + str(e))

  #Triangle transformations function
  elif ans == 8:
    #Ask user to enter a triangle's coordinates
    print("Enter a triangle's coordinates.".center(screenSize))
    #Create a dictionary to hold coordinates
    triangleCoordinates = {}
    xCoA = input("Enter the x-coordinate of point A.".center(screenSize)+ "\n")
    yCoA = input("Enter the y-coordinate of point A.".center(screenSize) + "\n")
    xCoB = input("Enter the x-coordinate of point B.".center(screenSize)+ "\n")
    yCoB = input("Enter the y-coordinate of point B.".center(screenSize)+ "\n")
    xCoC = input("Enter the x-coordinate of point C.".center(screenSize)+ "\n")
    yCoC = input("Enter the y-coordinate of point C.".center(screenSize)+ "\n")

    try:
      #Check if entered values are all convertible to floats
      xCoA = float(xCoA)
      xCoB = float(xCoB)
      xCoC = float(xCoC)
      yCoA = float(yCoA)
      yCoB = float(yCoB)
      yCoC = float(yCoC)
    except ValueError:
      print("Please enter an appropriate number for all the points.".center(screenSize))
      continue
      #Ask user to re-enter coordinates

    #Calculate all slopes of the lines
    slopeAtoB = slope(xCoA, yCoA, xCoB, yCoB)
    slopeBtoC = slope(xCoB, yCoB, xCoC, yCoC)
    slopeAtoC = slope(xCoA, yCoA, xCoC, yCoC)

    try:
      #If any of the slopes are equivalent, or if any two points have the same x and y coordinates, raise an exception
      if slopeAtoB == slopeBtoC or slopeAtoB == slopeAtoC or slopeAtoC == slopeAtoB or (xCoA == xCoB and yCoA == yCoB) or (xCoA == xCoC and yCoA == yCoC) or (xCoB == xCoC and yCoB == yCoC):
        raise ValueError("Please enter proper coordinates of a triangle.")
    except ValueError as e:
      print (str(e))
      continue
      #Ask user to re-enter coordinates

    #Place all values into the dictionary
    triangleCoordinates["xA"] = xCoA
    triangleCoordinates["yA"] = yCoA
    triangleCoordinates["xB"] = xCoB
    triangleCoordinates["yB"] = yCoB
    triangleCoordinates["xC"] = xCoC
    triangleCoordinates["yC"] = yCoC

    #This loop runs as long as the user wishes to continue performing transformations
    while True:
      #Ask user what transformation they would like to do
      transformation = input("What would you like to do?".center(screenSize) + "\n" + "1. Translation".center(screenSize) + "\n" + "2. Reflection".center(screenSize) + "\n" + "3. Rotation".center(screenSize) + "\n")
      try:
        #Check if answer is a valid integer between 1 and 3
        if not transformation.isdecimal():
          raise ValueError("Please enter an appropriate integer value.")
        transformation = int(transformation)
        if transformation != 1 and transformation != 2 and transformation != 3:
          raise ValueError("Please select an appropriate value between 1 and 3.")
      except ValueError as e:
        print(str(e))
        continue
        #Get user to answer question again if error arises
      else:
        #Check the value of transformation to see which one the user wants to perform  
        if transformation == 1:
          while True:
            #Ask user to input a vertical and horizontal transformation
            print("Choose a number of units to translate horizontally. Positive for right, negative for left.".center(screenSize)+ "\n")
            horizontalTranslation = input()
            print("Choose a number of units to translate vertically. Positive for up, negative for down".center(screenSize) + "\n")
            verticalTranslation = input()
            try:
              #Try to run translation
              triangleCoordinates = translate(horizontalTranslation, verticalTranslation, triangleCoordinates)
            except ValueError:
              #Catch any errors and restart translation loop if any are caught
              print("Please enter an appropriate positive or negative decimal number as your input.")
              continue
            except Exception as e:
              print(str(e))
              continue
            else:
              #If no errors caught, exit the translation loop
              break
        #If the user wishes to perform reflections:
        elif transformation == 2:
          while True:
            #Ask which direction they would like to perform the reflections in
            print("Would you like to reflect through a horizontal, vertical, or diagonal line?".center(screenSize)+ "\n" + "1. Horizontal".center(screenSize) + "\n" + "2.Vertical".center(screenSize) + "\n" + "3.Over y=x".center(screenSize) + "\n")
            direction = input()
            try:
              #Check if direction given is a valid integer between 1 and 3. If not, raise an exception
              direction = int(direction)
              if direction!=1 and direction !=2 and direction != 3:
                raise ValueError()
            except ValueError:
              print("Please enter a valid integer.".center(screenSize))
              continue
            else:
              break
              #If no errors occur, break out of questioning loop
          #If horizontal reflection is to be performed:
          if direction == 1:
            while True:
              #Ask user for a valid y-coordinate for the reflection line
              lineCoordinate = input("Please enter a y-coordinate for the reflection line.")
              try:
                #Check if entered coordinate is valid
                lineCoordinate = float(lineCoordinate)
              except ValueError:
                print("Please enter a valid positive or negative decimal number as your answer.")
                continue
              else:
                break
            #Find the distance from each of the y coordinates of the triangle to the lineCoordinate. Put the new y-coordinate on the other side of the lineCoordinate, at the same distance, by subtracting this distance from lineCoordinate
            triangleCoordinates['yA'] = lineCoordinate - (triangleCoordinates['yA'] - lineCoordinate)
            triangleCoordinates['yB'] = lineCoordinate - (triangleCoordinates['yB'] - lineCoordinate)
            triangleCoordinates['yC'] = lineCoordinate - (triangleCoordinates['yC'] - lineCoordinate)

          #To perform a vertical reflection
          elif direction == 2:
            while True:
              lineCoordinate = input("Please enter an x-coordinate for the reflection line: ")
              try:
                #Check if entered coordinate is valid
                lineCoordinate = float(lineCoordinate)
              except ValueError:
                print("Please enter a valid positive or negative decimal number as your answer.")
                continue
              else:
                break
            #Find the distance from each of the x coordinates of the triangle to the lineCoordinate. Put the new x-coordinate on the other side of the lineCoordinate, at the same distance, by subtracting this distance from lineCoordinate
            triangleCoordinates['xA'] = lineCoordinate - (triangleCoordinates['xA'] - lineCoordinate)
            triangleCoordinates['xB'] = lineCoordinate - (triangleCoordinates['xB'] - lineCoordinate)
            triangleCoordinates['xC'] = lineCoordinate - (triangleCoordinates['xC'] - lineCoordinate)         
          
          #Reflecting over y=x (Just switch x and y coordinates)
          elif direction == 3:
            #Create a temporary variable to hold the x coordinate of A
            temp = triangleCoordinates['xA']
            #Set the x coordinate of A to the y coordinate of A
            triangleCoordinates['xA'] = triangleCoordinates['yA']
            #Set the y coordinate of A to the x coordinate of A
            triangleCoordinates['yA'] = temp
            #Repeat for B
            temp = triangleCoordinates['xB']
            triangleCoordinates['xB'] = triangleCoordinates['yB']
            triangleCoordinates['yB'] = temp
            #Repeat for C
            temp = triangleCoordinates['xC']
            triangleCoordinates['xC'] = triangleCoordinates['yC']
            triangleCoordinates['yC'] = temp

        #If the user wishes to perform a rotation:
        elif transformation == 3:
          while True:
            #Ask for what angle the user wishes to rotate by
            rotateAmount = input("Please choose from one of the following rotation angles.".center(screenSize) + "\n" + "1. 90 degrees CW".center(screenSize) + "\n" + "2. 180 degrees".center(screenSize) + "\n" + "3. 90 degrees CCW".center(screenSize)+ "\n")
            try:
              #Check if input is a valid integer between 1 and 3
              rotateAmount = int(rotateAmount)
              if rotateAmount != 1 and rotateAmount !=2 and rotateAmount !=3:
                raise ValueError
            except ValueError:
              print("Please enter a valid integer between 1-3 to choose your rotation angle.")
              continue
              #If an error occurs, restart the questioning loop
            
            #Ask user to enter coordinates for centre of rotation
            rotateX = input("Please enter an x-coordinate for the centre of rotation.".center(screenSize) + "\n")
            rotateY = input("Please enter a y-coordinate for the centre of rotation.".center(screenSize) + "\n")
            try:
              #Check if coordinates entered are accurate float values
              rotateX = float(rotateX)
              rotateY = float(rotateY)
            except ValueError:
              print("Please enter a positive or negative decimal for the coordinates of the centre of rotation.".center(screenSize))
              continue
              #If an error occurs, restart the questioning loop
            else:
              break
              #Otherwise, begin the transformation by exiting the loop
          try:
            #Try to perform the rotation
            triangleCoordinates = rotate(rotateAmount, rotateX, rotateY, triangleCoordinates)
          except Exception as e:
            #Catch any errors
            print(str(e))

        #Once the user has exited from the transformations, print the result of the transformations on the triangle.
        print("The triangle's new coordinates are:".center(screenSize))
        outputString = "Point A: (" + str(triangleCoordinates['xA']) + ", " + str(triangleCoordinates['yA']) + ")"
        print (outputString.center(screenSize))
        outputString = "Point B: (" + str(triangleCoordinates['xB']) + ", " + str(triangleCoordinates['yB']) + ")"
        print (outputString.center(screenSize))
        outputString = "Point C: (" + str(triangleCoordinates['xC']) + ", " + str(triangleCoordinates['yC']) + ")"
        print (outputString.center(screenSize))
        
        #Ask user if they would like to continue performing transformations
        while True:
          ans = input("Would you like to continue performing transformations?".center(screenSize) + "\n1. Yes\n0. No\n")
          try:
            #Check if answer is a valid integer between 1 or 0
            ans = int(ans)
            if ans!=1 and ans !=0:
              raise ValueError
          except ValueError:
            #If not, raise an exception
            print("Please choose either 1 or 0.")
            continue 
          else:
            break
            #Otherwise, break out of questioning loop
        #If user wished to continue doing transformations, restart the loop
        if ans == 1:
          continue
        #If the user wished to exit transformations, break the main transformations loop
        elif ans == 0:
          break


  #If the user selected exit, print a message and exit the loop by setting checking variable to False
  elif ans == 0:
    #If the user wishes to exit the program, return False to indicate to the while loop in the main code that user wishes to exit
    print("Logging Out...")
    usingApp = False

#Succesful completion of program
logging.info("Program finished.")