#pip install requests beautifulsoup4

import sys
import requests
import re
import random
from bs4 import BeautifulSoup


class Hangman():
        
        def __init__(self,pickedWord):
            self.incorrect = 0
            self.pickedWord = pickedWord
            self.howManyGuesses = len(self.pickedWord)+10 #verkar rimligt
            self.NrGuesses = 0
            self.correct = 0
            self.pickedWordCopy = pickedWord

            self.game_progress = []
            self.incorrectprogress = []
            self.correctprogress = []

        def GuessALetter(self):

            user_input = input(f"Gissa på en bokstav, du har {self.howManyGuesses-self.NrGuesses} gissningar kvar: \n")
            user_input = user_input.lower()
            return user_input
    
        def CorrectFormat(self, input_):
            
            return input_.isdigit() or (input_.isalpha() and len(input_) > 1)

        def spelaHangman(self):

            print('Hej och välkommen till Hangman!\n')
            lengthWord = (len(self.pickedWord))
            print(f'Nu börjar spelet. Ordet har {lengthWord} antal bokstäver.\n')
            print(f"Du har totalt {self.howManyGuesses} antal gissningar på dig.")

        
        
            while self.NrGuesses<self.howManyGuesses:

                user_input = self.GuessALetter() # be om gissning

                self.NrGuesses = self.NrGuesses+1 # hur många gånger har jag gissat

                if self.CorrectFormat(user_input):
                    print('Du måste välja en bokstav.')
                    continue

                if user_input in self.incorrectprogress:
                    print('Du har redan gissat på den här bokstaven.')
                    continue

                if self.NrGuesses>self.howManyGuesses:
                    print('Du har tyvärr gissat för många gånger.')
                    print('Det rätta order är {0}'.format(self.pickedWord))
                    quit()


                if user_input in self.pickedWordCopy:

                    count = self.pickedWordCopy.count(user_input)

                    print(f"Ja, {user_input}  finns i ordet {count} gånger.")

                    if len(self.incorrectprogress)>0:
                        print(f"Du har gissat på följande bokstäver: {self.incorrectprogress} som inte finns i ordet.\n")
                   

                    self.correctprogress.append(user_input * count)
                    print(f"Du har gissat rätt på följande bokstäver: {self.correctprogress}\n")
             

                    self.pickedWordCopy = self.pickedWordCopy.replace(user_input,'')
                   

                    if len(self.pickedWordCopy)==0:
                        print(f'Du har gissat alla bokstäver rätt, ordet är: {self.pickedWord}!')
                        quit()


            

                else:
                    self.incorrectprogress.append(user_input)
                    print(f"Du har gissat på följande bokstäver: {self.incorrectprogress} som inte finns i ordet.\n")
                    if len(self.correctprogress)>0:
                        print(f"Du har gissat rätt på följande bokstäver: {self.correctprogress}\n")
             
            print('Tyvärr har du gissat för många gånger och spelet är slut.')
            print(f"Det rätta ordet är: {self.pickedWord}")


def clean_string(input_string):
  
    
    pattern = r'[0-9(),.:|%;-]'
    
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


if __name__ == '__main__':

    ordet = GetWord()
   
    hangman = Hangman(ordet)
    hangman.spelaHangman()
