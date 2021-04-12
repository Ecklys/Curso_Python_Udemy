#Declaramos variables globales para crear el mazo

from random import shuffle
Suite = ["Clubs","Diamonds","Hearts","Spades"]
Ranks = ["Ace","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King"]
Values = {"Ace":11,"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10}

#Declaramos la clase Cards, para la creación de cartas del mazo

class Cards():
    
    def __init__(self,suite,rank):
        
        self.suite = suite
        self.rank = rank
        self.value = Values[rank]
        
    def __str__(self):
        return f"{self.rank} of {self.suite}"
    
    
#Declaramos la clase Deck, donde inicializamos el mazo, creando las 52 cartas necesarias 

class Deck():
    
    def __init__(self): 
        
        self.all_cards = []
        for suite in Suite:
            for rank in Ranks:
                self.all_cards.append(Cards(suite,rank))
                
    def add_cards(self,cards):
        if type(cards) == type([]):
            return self.all_cards.extend(cards)            
        else:
            return self.all_cards.append(cards)
    
    def shuffle_deck(self):        
        shuffle(self.all_cards)
        
    def deal_card(self):
        return self.all_cards.pop()
    
    def __str__(self):
        self.deck_comp = ""
        for card in self.all_cards:
            self.deck_comp += "\n" + card.__str__()
        return "The deck has:" + self.deck_comp
            

#Declaramos la clase Player, donde inicializamos al jugador y el dinero con el que cuenta
class Player():

    def __init__(self,money):
        
        self.hand_cards = []
        self.money = money
        
    def lose_bet(self,amount):
        self.money -= amount
    
    def win_bet(self,amount):
        self.money += amount                     
    
    def add_cards(self,cards):
        if type(cards) == type([]):
            return self.hand_cards.extend(cards)            
        else:
            return self.hand_cards.append(cards)  
           
    def __str__(self):
        return f"El jugador tiene {self.money} en fichas"
        

#Funcion para obtener apuesta del jugador
def take_bet():
    
    ask_bet = True
    
    while ask_bet == True:             
        try:
            bet_amount = int((input("\nIngrese monto de apuesta: ")))  
            print("")
        except:
             print("Error! Ingrese un monto de apuesta (númerico)")        
        else:
            if bet_amount <= player_one.money:
                ask_bet = False
                return bet_amount
            else:
                print("No tienes suficientes fichas")  
                
#Función para desplegar cartas
def display_board_cards(game_on):
    #Si aun se esta jugando solo muestra una carta de la computadora 
    if game_on:
        print("Computer: {}".format(computer.hand_cards[0]))
        print("Computer: ?")
        print("")
        for num_cards in range(len(player_one.hand_cards)):
            print("Player: {}".format(player_one.hand_cards[num_cards])) 
        print("")
            
    #CUando termine el juego se muestran todas las cartas en mesa         
    else:
        for num_cards in range(len(computer.hand_cards)):
            print("Computer: {}".format(computer.hand_cards[num_cards]))
        print("")
        for num_cards in range(len(player_one.hand_cards)):
            print("Player: {}".format(player_one.hand_cards[num_cards]))

#Función para decidir si pedir otra carta o mantenerse
def stand_or_hit():
    
    decision = "none"
        
    while decision.lower() not in ["stand","hit"]:          
        decision = input("\nQuiere mantenerse(stand) o pedir(hit): ")
        print("")
        if decision.lower() not in ["stand","hit"]:          
            print("\nError! Elija entre mantenerse(stand) o pedir(hit)")
    return decision.lower()

#Función para preguntar si el jugador desea otra ronda
def keep_playing():
    
    play = "none"
    
    while play.upper() not in ["Y","N"]:
        play = input("\nDesea seguir jugando (Y o N): ")
        if play.upper() not in ["Y","N"]:
            print("\nOpción Incorrecta, Ingrese Y o N")
    
    if play.upper() == "N":
        clear_output()
        print("\nGracias por jugar")
        return False
        
    else:
        clear_output()
        return True      
        
from IPython.display import clear_output

# Variables de juego, jugador comienza con 500 fichas
player_one = Player(500)
computer = Player(0)

bet_amount = 0
new_deck = Deck()

#Comenzamos el juego
game_on = True
while game_on:    
    
    decision = "hit"
    new_deck.shuffle_deck()    
    player_hand_value = 0
    computer_hand_value = 0    
    
    
    #Solicitamos la apuesta del jugador
    print(player_one)
    bet_amount = take_bet()        
    
    #Damos las 2 primeras cartas al jugador y la computadora y sumamos los valores de las cartas
    for deal in range(2):
        player_one.add_cards(new_deck.deal_card())
        player_hand_value += player_one.hand_cards[-1].value
        
        computer.add_cards(new_deck.deal_card()) 
        computer_hand_value += computer.hand_cards[-1].value     
                    
    #Turno Jugador
    while decision == "hit":
        
        #Desplegamos las cartas de la computadora y del jugador
        clear_output()        
        display_board_cards(True)         
        
        #Si el valor de nuestra mano es 21, obtenemos un blackjack y ganamos 1.5 veces el monto de la apuesta
        if player_hand_value == 21:
            clear_output()
            print("\nBLACKJACK!\n")
            player_one.win_bet(bet_amount*1.5)
            break           
        
        #Si tenemos una mano mayor a 21, verificamos si tenemos un ACE, si tenemos restamos 10 al valor de la mano
        elif player_hand_value > 21:
            for cards in range(len(player_one.hand_cards)):
                if player_one.hand_cards[cards].rank == "Ace" and player_one.hand_cards[cards].value == 11:
                    player_hand_value -= 10
                    player_one.hand_cards[cards].value = 1
                    break
            else:
                clear_output()
                print("\nBUST\n")
                player_one.lose_bet(bet_amount)
                game_on = False
                break        
        
        #Consultamos al jugador si mantiene o pide
        decision = stand_or_hit()               
               
        if decision == "hit":          
            player_one.add_cards(new_deck.deal_card())
            player_hand_value += player_one.hand_cards[-1].value
    
    
    #Turno Computadora
    while decision == "stand":      
        
        #Desplegamos las cartas de la computadora y del jugador
        clear_output()        
        display_board_cards(True)            
                   
        #Si la computadora tiene una mano mayor a 21, verificamos si tiene un ACE, si tiene restamos 10 al valor de la mano
        if computer_hand_value > 21:
            for cards in range(len(computer.hand_cards)):
                if computer.hand_cards[cards].rank == "Ace" and computer.hand_cards[cards].value == 11:
                    computer_hand_value -= 10
                    computer.hand_cards[cards].value = 1
                    break
            else:
                clear_output()
                print("\nPlayer wins!\n")
                player_one.win_bet(bet_amount)
                decision = "none"
                break
        
        #Si el valor de la mano de la computadora es mayor al del jugador, entonces el jugador pierde
        elif computer_hand_value > player_hand_value:
            clear_output()
            print("\nPlayer loses!\n")
            player_one.lose_bet(bet_amount)
            decision = "none"
            break    
        
        else:
            computer.add_cards(new_deck.deal_card())
            computer_hand_value += computer.hand_cards[-1].value                  
    
    display_board_cards(False)
    
    #Devolvemos las cartas al mazo
    new_deck.add_cards(player_one.hand_cards)
    new_deck.add_cards(computer.hand_cards)      
    
    player_one.hand_cards = []
    computer.hand_cards = []
    
    #variable para seguir jugando
    game_on = keep_playing()
    
     
    