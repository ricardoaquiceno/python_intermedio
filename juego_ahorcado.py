from pickle import FALSE
import random
import os
from functools import reduce
from signal import pause
from sys import intern
import re

def f_remove_accents(old):
    """
    Removes common accent characters, lower form.
    Uses: regex.
    """
    new = old.lower()
    new = re.sub(r'[àáâãäå]', 'a', new)
    new = re.sub(r'[èéêë]', 'e', new)
    new = re.sub(r'[ìíîï]', 'i', new)
    new = re.sub(r'[òóôõö]', 'o', new)
    new = re.sub(r'[ùúûü]', 'u', new)
    return new

def read():
    """ reads all the words from the file """
    game_words=[]
    with open("./data.txt","r",encoding="utf-8") as f:
        game_words=[i for i in f]
    return game_words

def game(word):

    """ creates the game "Hang man" by verifying the characters and checking if they are correct ot not """
    word=f_remove_accents(word)
    word=[i for i in word if i!="\n"] #here we remove the \n from the word
    letras=["-" for i in range(1,len(word)+1)] #here we will save the letters that have been correct
    used_ones=[]
    current_word=reduce(lambda a,b : a+b, letras) #a way to convert the list yo string
    fail=True
    

    while fail:
        try:
            # this part is just the interface
            os.system("clear")   
            print("Guess the word")
            print(current_word)
            print(used_ones)
            x=input("\n ingresa una letra: ")
            

            if x.isnumeric()==True: #checking that the character is alfa
                raise ValueError("please only use alphabetic characters")

            if len(used_ones)==0: #initializing the "used ones" list/array 
                used_ones.append(x)
            #this part checks whether the letter was already used, if not, will be added to the "Used ones"  
            cont_used_ones=0
            for i in used_ones:
                
                if x==i:  
                    break
                else:
                    cont_used_ones+=1
                if cont_used_ones==len(used_ones):
                    used_ones.append(x)
            #this part checks if the letter is within the word            
            cont=0
            for i in word:
                if i==x:
                    letras[cont]=x
                cont+=1
            current_word=reduce(lambda a,b : a+b, letras)
            
                

            #the last part checks if the current word is the same as the word for this game

            if letras==word:
                fail=False
                os.system("clear")    
                print(current_word)
                print(""" 
                          YYYYYYY       YYYYYYY     OOOOOOOOO     UUUUUUUU     UUUUUUUU     WWWWWWWW                           WWWWWWWWIIIIIIIIIINNNNNNNN        NNNNNNNN
                          Y:::::Y       Y:::::Y   OO:::::::::OO   U::::::U     U::::::U     W::::::W                           W::::::WI::::::::IN:::::::N       N::::::N
                          Y:::::Y       Y:::::Y OO:::::::::::::OO U::::::U     U::::::U     W::::::W                           W::::::WI::::::::IN::::::::N      N::::::N
                          Y::::::Y     Y::::::YO:::::::OOO:::::::OUU:::::U     U:::::UU     W::::::W                           W::::::WII::::::IIN:::::::::N     N::::::N
                          YYY:::::Y   Y:::::YYYO::::::O   O::::::O U:::::U     U:::::U       W:::::W           WWWWW           W:::::W   I::::I  N::::::::::N    N::::::N
                             Y:::::Y Y:::::Y   O:::::O     O:::::O U:::::D     D:::::U        W:::::W         W:::::W         W:::::W    I::::I  N:::::::::::N   N::::::N
                              Y:::::Y:::::Y    O:::::O     O:::::O U:::::D     D:::::U         W:::::W       W:::::::W       W:::::W     I::::I  N:::::::N::::N  N::::::N
                               Y:::::::::Y     O:::::O     O:::::O U:::::D     D:::::U          W:::::W     W:::::::::W     W:::::W      I::::I  N::::::N N::::N N::::::N
                                Y:::::::Y      O:::::O     O:::::O U:::::D     D:::::U           W:::::W   W:::::W:::::W   W:::::W       I::::I  N::::::N  N::::N:::::::N
                                 Y:::::Y       O:::::O     O:::::O U:::::D     D:::::U            W:::::W W:::::W W:::::W W:::::W        I::::I  N::::::N   N:::::::::::N
                                 Y:::::Y       O:::::O     O:::::O U:::::D     D:::::U             W:::::W:::::W   W:::::W:::::W         I::::I  N::::::N    N::::::::::N
                                 Y:::::Y       O::::::O   O::::::O U::::::U   U::::::U              W:::::::::W     W:::::::::W          I::::I  N::::::N     N:::::::::N
                                 Y:::::Y       O:::::::OOO:::::::O U:::::::UUU:::::::U               W:::::::W       W:::::::W         II::::::IIN::::::N      N::::::::N
                              YYYY:::::YYYY     OO:::::::::::::OO   UU:::::::::::::UU                 W:::::W         W:::::W          I::::::::IN::::::N       N:::::::N
                              Y:::::::::::Y       OO:::::::::OO       UU:::::::::UU                    W:::W           W:::W           I::::::::IN::::::N        N::::::N
                              YYYYYYYYYYYYY         OOOOOOOOO           UUUUUUUUU                       WWW             WWW            IIIIIIIIIINNNNNNNN         NNNNNNN                                                                                                                
                                                                                                                                               
                        """)

        except ValueError as error:
            print(error)




def main():
    os.system("clear")
    possible_words=read()
    number=random.randint(0,len(possible_words))
    word=possible_words[number] #escoge una palabra de las possibles 
    game(word)

if __name__=="__main__":
    main()

