#calculate the sum of the intitial card's values 
def SUM_initial(cards,ace1,ace2,summation): 
  #values for the first card 
  if cards[0][0] == "2": 
    summation = summation + 2 
  if cards[0][0] == "3": 
    summation = summation + 3 
  if cards[0][0] == "4": 
    summation = summation + 4 
  if cards[0][0] == "5": 
    summation = summation + 5 
  if cards[0][0] == "6": 
    summation = summation + 6 
  if cards[0][0] == "7": 
    summation = summation + 7 
  if cards[0][0] == "8": 
    summation = summation + 8 
  if cards[0][0] == "9": 
    summation = summation + 9 
  if cards[0][0] == "T": 
    summation = summation + 10 
  if cards[0][0] == "J": 
    summation = summation + 10 
  if cards[0][0] == "Q": 
    summation = summation + 10 
  if cards[0][0] == "K": 
    summation = summation + 10 
  if ace1 == 1 or ace1 == 11: 
    summation = summation + ace1
  
  #values for the second card 
  if cards[1][0] == "2": 
    summation = summation + 2 
  if cards[1][0] == "3": 
    summation = summation + 3 
  if cards[1][0] == "4": 
    summation = summation + 4 
  if cards[1][0] == "5": 
    summation = summation + 5 
  if cards[1][0] == "6": 
    summation = summation + 6 
  if cards[1][0] == "7": 
    summation = summation + 7 
  if cards[1][0] == "8": 
    summation = summation + 8 
  if cards[1][0] == "9": 
    summation = summation + 9 
  if cards[1][0] == "T": 
    summation = summation + 10 
  if cards[1][0] == "J": 
    summation = summation + 10 
  if cards[1][0] == "Q": 
    summation = summation + 10 
  if cards[1][0] == "K": 
    summation = summation + 10 
  if ace2 == 1 or ace2 == 11: 
    summation = summation + ace2

  return(summation)

#calculate the sum with cards three or four
def SUM_final(card,ace,summation):
  #values for the third/fourth card 
  if card[0][0] == "2": 
    summation = summation + 2 
  if card[0][0] == "3": 
    summation = summation + 3 
  if card[0][0] == "4": 
    summation = summation + 4 
  if card[0][0] == "5": 
    summation = summation + 5 
  if card[0][0] == "6": 
    summation = summation + 6 
  if card[0][0] == "7": 
    summation = summation + 7 
  if card[0][0] == "8": 
    summation = summation + 8 
  if card[0][0] == "9": 
    summation = summation + 9 
  if card[0][0] == "T": 
    summation = summation + 10 
  if card[0][0] == "J": 
    summation = summation + 10 
  if card[0][0] == "Q": 
    summation = summation + 10 
  if card[0][0] == "K": 
    summation = summation + 10 
  if ace == 1 or ace == 11: 
    summation = summation + ace 

  return(summation)