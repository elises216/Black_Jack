import picture
import sum
import create
import sys
import drawing

#THIS IS THE MAIN CODE. PLEASE RUN THIS ONE FOR TESTING

#the main space for the drawing
def photo(canvas,cards,iteration,x,y):
  #base case 
  if iteration == 0: 
    #set color to green 
    canvas.setFillColor(34,139,34)
    #make the whole background green to represent the tabletop at a casino
    canvas.drawRectFill(0,0,525,500)
   
  if iteration >= 0 and iteration < 4: 
    card = cards[iteration]

    #set the outline color to black 
    canvas.setOutlineColor(0,0,0)
    #set the fill color to white 
    canvas.setFillColor(255,255,255)
    #create a card 
    canvas.drawRectFill(x, y, 100, 160) 

    #call the determie color function 
    color = create.determineColor(canvas,card)
    create.createCard_Value(canvas,card,x,y,color)
    create.createCard_Suit(canvas,card,x,y,color)

    if iteration == 0:
      photo(canvas,cards,iteration + 1, 150, 25)
    if iteration == 1: 
      photo(canvas,cards,iteration + 1, 25, 300)
    if iteration == 2: 
      photo(canvas,cards,iteration + 1, 150, 300)

#will the player HIT or STAND? 
def PlayerChoice(canvas,x,y,sum1,choice):
  #if the player decides to HIT 
  if choice == 1:
    #create another card
    playerCard3 = create.GenerateCards()

    #is this new card that the player drew an ace? 
    import ace
    ace = ace.AceValue_Player(playerCard3)
    if ace == 1 or ace == 11: 
      print()
      print("Ace value for third player card:", ace)
    print()

    #adds to the player sum 
    #put the next card into a list
    playerCard3 = [playerCard3]
    #call the new sum function 
    new_sum = sum.SUM_final(playerCard3,ace,sum1)
    print("the sums of the player's cards are",new_sum)

    #set the outline color to white 
    canvas.setOutlineColor(0,0,0)
    #set the fill color to black 
    canvas.setFillColor(255,255,255)

    #create a card outline
    canvas.drawRectFill(x, y, 100, 160) 

    #call the determie color function 
    color = create.determineColor(canvas,playerCard3[0])
    create.createCard_Value(canvas,playerCard3[0],x,y,color)
    create.createCard_Suit(canvas,playerCard3[0],x,y,color)
    input()

    if new_sum == 21: 
      print("Congratulations")
      print("Player Wins!")
      drawing.winner(canvas,0,0)
      input()
      sys.exit(-1)
    if end(new_sum) == False: 
      print("Oh no, you went over 21.")
      print("Computer Wins")
      drawing.loser(canvas,0,0)
      input()
      sys.exit(-1)

    return new_sum
  elif choice == 2: 
    #set color to green 
    canvas.setFillColor(34,139,34)

    #set the outline color to white 
    canvas.setOutlineColor(34,139,34)

    #create a card outline
    canvas.drawRectFill(x, y, 100, 160) 

    return sum1

#will the computer HIT or STAND?
def ComputerChoice(canvas,x,y,sum1):
  if sum1 <= 16 and sum1 > 0: 
    #draw a third card for the computer 
    computerCard3 = create.GenerateCards()
    #put the card into a list
    computerCard3 = [computerCard3]

    #is this new card that the player drew an ace? 
    import ace
    ace = ace.AceValue_Computer(computerCard3)
    if ace == 1 or ace == 11: 
      print("Ace value for third computer card:", ace)
      print()

    #adds to the computer sum 
    new_sum = sum.SUM_final(computerCard3,ace,sum1)
    print("the sums of the computers's cards are",new_sum)

    #set the outline color to white 
    canvas.setOutlineColor(0,0,0)
    #set the fill color to black 
    canvas.setFillColor(255,255,255)

    #create a card outline
    canvas.drawRectFill(x, y, 100, 160) 

    #call the determie color function 
    color = create.determineColor(canvas,computerCard3[0])
    create.createCard_Value(canvas,computerCard3[0],x,y,color)
    create.createCard_Suit(canvas,computerCard3[0],x,y,color)
    input()

    if end(new_sum) == True: 
      print("Oh no")
      print("Computer Wins!")
      drawing.loser(canvas,0,0)
      input()
      sys.exit(-1)
    if end(new_sum) == False: 
      print("The computer went over 21")
      print("Player Wins!")
      drawing.winner(canvas,0,0)
      input()
      sys.exit(-1)

    return new_sum 
  else: 
    return sum1

def end(sum):
  if sum == 21: 
    return True 
  if sum > 21: 
    return False  

#main function
def main(): 
  print("Hello! Welcome to my game of Black Jack!")
  print("Try to get as close to 21 without going over!")
  print()
  print("Your cards are on the bottom!")
  print("The computer's cards are on the top!")

  #create the canvas of the game play 
  canvas = picture.Picture(525, 500)

  #create a list of all the randomly selected cards 
  #2 for the player, 2 for the computer 
  cards = create.ChooseCards()

  #call the photo function to display the cards
  photo(canvas,cards,0,25,25)

  #if one of the player's cards is an ace, ask them if they want it to be an 11 or 1
  import ace
  ace_player1 = ace.AceValue_Computer(cards[0])
  ace_player2 = ace.AceValue_Computer(cards[1])
  ace_computer1 = ace.AceValue_Player(cards[2])
  ace_computer2 = ace.AceValue_Player(cards[3])

  #sum up the values of the player's cards 
  sum_player_initial = sum.SUM_initial(cards[:2],ace_player1,ace_player2,0)
  if sum_player_initial == 21: 
    print("Player Wins")
    drawing.winner(canvas,0,0)
  #sum up the values of the computer's cards 
  sum_computer_initial = sum.SUM_initial(cards[2:],ace_computer1,ace_computer2,0)
  if sum_computer_initial == 21: 
    print("Computer Wins")
    drawing.loser(canvas,0,0)

  print()
  print("the sums of the player's cards are",sum_computer_initial)
  print("the sums of the computers's cards are", sum_player_initial)
  
  #determine if the player hits or stands 
  print()
  print("Enter 1 to HIT")
  print("Enter 2 to STAND")
  choice = int(input("Would you like to hit or stand? "))

  #if the player inputs something invalid 
  if choice <= 0 or choice > 2: 
    print("Please enter 1 or 2. ")
    #recall the choice function so they can enter one or two 
    print()
    print("Enter 1 to HIT")
    print("Enter 2 to STAND")
    choice = int(input("Would you like to hit or stand? "))

    PlayerChoice(canvas,275,300,sum_computer_initial,None)

  psum = player_choice = PlayerChoice(canvas,275,300,sum_computer_initial,choice)
 
  #determine if the computer hits or stands 
  csum = ComputerChoice(canvas,275,25, sum_player_initial)

  if csum > psum: 
    print("Computer Wins")
    drawing.loser(canvas,0,0)
  if psum > csum: 
    print("Player Wins")
    drawing.winner(canvas,0,0)
  if psum == csum: 
    print("TIE")

  if player_choice == 1: 
    print("Enter 1 to HIT")
    print("Enter 2 to STAND")
    choice = int(input("Would you like to hit or stand? "))
    player_sum = PlayerChoice(canvas,400,300,sum_computer_initial,choice)
 
    #determine if the computer hits or stands 
    computer_sum = ComputerChoice(canvas,400,25, sum_player_initial)

    if computer_sum > player_sum: 
      print("Computer Wins")
      drawing.loser(canvas,0,0)
    if player_sum > computer_sum: 
      print("Player Wins")
      drawing.winner(canvas,0,0)

main()
input()