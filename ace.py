import random

#will the ace be an 11 or 1? (player's choice)
#the player gets to choose 
def AceValue_Player(cards): 
  if cards[0] == "A":
    print()
    print("Type 1 - Let the ace equal 1")
    print("Type 11 - Let the ace equal 11")
    value = int(input("What value would like to assign to the ace? "))

    #return the value the user inputed 
    return value

#will the ace be an 11 or 1? (computer's choice)
#the ace value will be randomly selected
def AceValue_Computer(card): 
  if card[0] == "A": 
    rand_A = int(random.randrange(2))

    if rand_A == 0: 
      return 1
    if rand_A == 1: 
      return 11 
