import keyboard
import random
#Tre I Rad
class Playertype:   #Class decides which turn it currently is
    def __init__(self):
        self.player1 = 'X'
        self.player2 = 'O'
        self.starter = random.randint(0, 1)
        self.current = 0
        if self.starter == 1:
            self.current = self.player1
        else:
            self.current = self.player2
    def __str__(self):
        pass

    def next_round(self):
        if self.current == self.player1:
            self.current = self.player2
        else:
            self.current = self.player1



#Skapa två objekt? X och O
#Skapa 3x3 rutnät
class ThreeInARow:
    def __init__(self):
        self.gridnet = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        #self.player = ['X','O']
        #self.starter = random.randint(0,1) #if self.starter = 0, X starts, otherwise O starts
        self.player = Playertype() #Creates and decides who is playing
        self.board_list = [ str(i) for i in range(1,10) ]
        self.board_dictionary = {}
        self.stalemate = 0
        self.wincount = [0, 0]
        for i in self.board_list:
            self.board_dictionary[i] = ''

    def showboard(self):
        for i in range(3):
            print(f'{self.gridnet[i]}')
    def reset_game(self):
        self.player = Playertype()  # Creates and decides who is playing
        for i in self.board_list:
            self.board_dictionary[i] = ''


    def start_game(self):
        pass # Loopa Spelet, Turbaserat, input med numpad
    def display_current_state(self):
        print(f"[ {self.board_dictionary['7']} | {self.board_dictionary['8']} | {self.board_dictionary['9']} ]")
        print(f"[ {self.board_dictionary['4']} | {self.board_dictionary['5']} | {self.board_dictionary['6']} ]")
        print(f"[ {self.board_dictionary['1']} | {self.board_dictionary['2']} | {self.board_dictionary['3']} ]")
    def game_round(self):
        print(f"It is currently {self.player.current}'s turn!")
        self.stalemate = 0
        while True:
            self.roundvalue = 0
            self.templist = []
            self.roundvalue = keyboard.read_key()
            #print(f'You Pressed {self.roundvalue}') #For Test
            for i in self.board_list:             #Test for numerical relevance
                if i == self.roundvalue:            #If matching break loop
                    self.templist.append(i)                       #Otherwise repeat while loop
            if self.templist == []:
                print("You entered a value that does not correspond to the game grid! Try Again")
                continue
            if self.board_dictionary[self.roundvalue] == '':
                self.board_dictionary[self.roundvalue] = self.player.current # add value to dictionary if slot is empty

                break
            else:
                print('That position has already been played! Try Again!')


    def win_check(self): #Test win conditions and check if board is full
        if (self.board_dictionary["7"] == self.board_dictionary["8"] == self.board_dictionary["9"] != '' or
            self.board_dictionary["7"] == self.board_dictionary["5"] == self.board_dictionary["3"] != '' or
            self.board_dictionary["4"] == self.board_dictionary["5"] == self.board_dictionary["6"] != '' or
            self.board_dictionary["1"] == self.board_dictionary["2"] == self.board_dictionary["3"] != '' or
            self.board_dictionary["7"] == self.board_dictionary["4"] == self.board_dictionary["1"] != '' or
            self.board_dictionary["8"] == self.board_dictionary["5"] == self.board_dictionary["3"] != '' or
            self.board_dictionary["9"] == self.board_dictionary["6"] == self.board_dictionary["3"] != '' or
            self.board_dictionary["1"] == self.board_dictionary["5"] == self.board_dictionary["9"] != '' ):
            if self.player.current == self.player.player1:
                self.wincount[0] += 1
            else:
                self.wincount[1] += 1
            return True
        else:
            return False
    def stalemate_check(self):
        for i in self.board_list:
            if self.board_dictionary[i] != '':
                self.stalemate += 1
        if self.stalemate >= 9:
            return True
    def congratulations(self):
        print(f'Player {self.player.current} wins! Congratulations!')
        print(f'Player X has {self.wincount[0]} Wins, and Player O has {self.wincount[1]} wins currently!')
        print(f'Do you want to play again? Press Y/N')
    def restart_ask(self):
        while True:
            self.restart = keyboard.read_key()
            if self.restart == 'y':
                print('Game is restarting...')
                return True

            if self.restart == 'n':
                return False

            else:
                print('Wrong key press')



           #Value has been checked to not be a letter
        #Time to check if the slot is available in the dictionary
        #If the dictionary slot isn't empty The whole cycle has to repeat + tell the player

    #Start information vem börjar


    # Start information vem börjar
    #Kontrollera om en position är ockuperad blockera input.

    #Kontrollera, om 3 i rad horisontellt, Vertikalt eller Snett, Vinst
x = ThreeInARow()
print('Welcome to Three in a row!')

while True:
    x.display_current_state()
    x.game_round()
    x.display_current_state()
    if x.win_check() == True:
        x.congratulations()
        if x.restart_ask() == True:
            x.reset_game()
        else:
            break
    if x.stalemate_check() == True:
        print('Stalemate! Do you want to reset? Y/N')
        if x.restart_ask() == True:
            x.reset_game()
        else:
            break
    x.player.next_round()

