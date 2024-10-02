#pip install requests beautifulsoup4

import sys
import requests
import re
import random
from bs4 import BeautifulSoup


def clean_string(input_string):
  
    
    pattern = r'[0-9(),.|%;-]'
    
    cleaned_string = re.sub(pattern, '', input_string)
    cleaned_string = re.sub(r'\b\w{1,3}\b', '', cleaned_string)
    
    return cleaned_string

def pickRandom(input_string):
    
    return random.choice(input_string)

def printWelcomeandNumber(pickedString,howManyGuessesdoIHave):
    print('Hej och välkommen till Hangman!\n')
    lengthWord = (len(pickedString))
    print(f'Nu börjar spelet. Ordet har {lengthWord} antal bokstäver.\n')
    print(f"Du har totalt {howManyGuessesdoIHave} antal gissningar på dig.")

def GetWord():
    # URL of the web page you want to scrape
    url = 'https://seb.se/'
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract text from the page
    text = soup.get_text()
    cleaned_string = clean_string(text)

    word_list = cleaned_string.split()
   
    pickedWord = (pickRandom(word_list))
    pickedWord = pickedWord.lower()

    return pickedWord

def main():
    
    howManyGuessesdoIHave = 20
    pickedWord = GetWord()

    printWelcomeandNumber(pickedWord,howManyGuessesdoIHave)

    pickedWordCopy = pickedWord

    NrGuesses = 0
    #bra veta vad man redan gissat på
    storedRightGuessedLetters = ""
    storedWrongGuessedLetters = ""
   
   

    #fortsätt bara gissa tills du har rätt, och inte har gissat för många ggr
    while len(pickedWordCopy)>0 and NrGuesses<howManyGuessesdoIHave:

        #be om första gissningen
        Letter, NrGuesses = GuessALetter(NrGuesses,howManyGuessesdoIHave)

        if Letter in pickedWordCopy:

            count = pickedWordCopy.count(Letter)

            print(f"Ja, {Letter}  finns i ordet {count} gånger.")

            storedRightGuessedLetters = storedRightGuessedLetters+(Letter * count)

            pickedWordCopy = pickedWordCopy.replace(Letter,"")
          

        else:


            if Letter in storedWrongGuessedLetters:
                print(f"Du har redan gissat på {Letter}, och det finns inte i ordet")

            elif Letter in storedRightGuessedLetters:
                print(f"Du har redan gissat på {Letter} som finns i ordet.")

            else:
                storedWrongGuessedLetters = storedWrongGuessedLetters+Letter

            
        if len(storedWrongGuessedLetters)>0:
            print(f"Du har gissat på följande bokstäver: {storedWrongGuessedLetters} som inte finns i ordet.\n")
        
        if len(storedRightGuessedLetters)>0:
            print(f"Du har gissat rätt på följande bokstäver: {storedRightGuessedLetters}\n")


    
    
    else:

        if len(pickedWordCopy) == 0:
            print(f'Du har gissat alla bokstäver rätt, ordet är: {pickedWord}!')
        

        elif NrGuesses==howManyGuessesdoIHave:
             print(f'Du har gissat för många gånger tyvärr, spelet är slut. Det rätta order var: {pickedWord}.')





def GuessALetter(NrGuesses,howManyGuessesdoIHave):

 
        if (howManyGuessesdoIHave-NrGuesses)>0:
            user_input = input(f"Gissa på en bokstav, du har {howManyGuessesdoIHave-NrGuesses} gissningar kvar: \n")
            user_input = user_input.lower()
        

            print(f"Du gissade på: {user_input}")
            NrGuesses = NrGuesses+1
            print(f"Du har gissat {NrGuesses} gånger")


            if user_input.isalpha():
            
                return user_input, NrGuesses

            else:
                print('Du måste välja en bokstav.\n')

                user_input, NrGuesses = GuessALetter(NrGuesses,howManyGuessesdoIHave)

                return user_input, NrGuesses
        else:
            
            user_input = " "
            return user_input, NrGuesses

        



if __name__ == '__main__':
    if len(sys.argv) > 0:
        main()
    else:
        print("Too many arguments provided.")
