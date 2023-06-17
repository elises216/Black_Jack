import random
import drawing

#randomly choose a card from the possible 52 
def GenerateCards(): 
  #list of all the possible suits 
  suits = ["S", "H", "D", "C"]
  #list of all possible card values 
  values = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]

  #randomly pick one of the 13 values and one of the 4 suits 
  rand_suit = int(random.randrange(4))
  rand_value = int(random.randrange(13))

  suit = suits[rand_suit]
  value = values[rand_value]

  #combine the value with the suit
  return(value + suit) 

#put cards into list 
def ChooseCards():
  #randomly pick the cards the players will use 
  playerCard1 = GenerateCards()
  playerCard2 = GenerateCards()
  computerCard1 = GenerateCards()
  computerCard2 = GenerateCards()

  #put all the cards in lists 
  cards = [playerCard1, playerCard2, computerCard1, computerCard2]

  return cards

#draw the values onto the cards in either red or black 
def createCard_Value(canvas,card,x,y,color): 
  color 

  if card[0] == "2": 
    drawing.two(canvas,x,y)
  if card[0] == "3": 
    drawing.three(canvas,x,y)
  if card[0] == "4": 
    drawing.four(canvas,x,y)
  if card[0] == "5": 
    drawing.five(canvas,x,y)
  if card[0] == "6": 
    drawing.six(canvas,x,y)
  if card[0] == "7": 
    drawing.seven(canvas,x,y)
  if card[0] == "8": 
    drawing.eight(canvas,x,y)
  if card[0] == "9": 
    drawing.nine(canvas,x,y)
  if card[0] == "T": 
    drawing.ten(canvas,x,y)
  if card[0] == "J": 
    drawing.jack(canvas,x,y)
  if card[0] == "Q": 
    drawing.queen(canvas,x,y)
  if card[0] == "K": 
    drawing.king(canvas,x,y)
  if card[0] == "A": 
    drawing.ace(canvas,x,y)

#draw the suits onto the cards in either red or black 
def createCard_Suit(canvas,card,x,y,color): 
  color

  if card[1] == "H": 
    drawing.hearts(canvas,x,y+80)
  if card[1] == "S": 
    drawing.spades(canvas,x,y+80)
  if card[1] == "C": 
    drawing.clubs(canvas,x,y+80)
  if card[1] == "D": 
    drawing.diamonds(canvas,x,y+80)

#figure out if the card should be red or black depending on the suit
def determineColor(canvas,card):
  #if the card is spades or clubs
  if card[1] == "S" or card[1] == "C":
    #set fill color to black 
    return(canvas.setFillColor(0,0,0),canvas.setOutlineColor(0,0,0))

  #if the card is hearts or diamonds 
  if card[1] == "H" or card[1] == "D":
    #set fill color to red 
    return(canvas.setFillColor(255,0,0),canvas.setOutlineColor(255,0,0))