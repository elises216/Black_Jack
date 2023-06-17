
def two(canvas,x,y):
  #draw the number 2 
  canvas.drawRectFill(x + 25,y + 5,50,10) 
  canvas.drawRectFill(x + 65,y + 15,10,20)
  canvas.drawRectFill(x + 25,y + 35,50,10)
  canvas.drawRectFill(x + 25,y + 45,10,20)
  canvas.drawRectFill(x + 25,y + 65,50,10)

def three(canvas,x,y):
  #draw the number three 
  canvas.drawRectFill(x + 25,y + 5,50,10) 
  canvas.drawRectFill(x + 25,y + 65,50,10)
  canvas.drawRectFill(x + 65,y + 15,10,20)
  canvas.drawRectFill(x + 65,y + 45,10,20)
  canvas.drawRectFill(x + 45,y + 35,30,10)

def four(canvas,x,y): 
  #draw the number four 
  canvas.drawRectFill(x + 25,y + 35,50,10)
  canvas.drawRectFill(x + 65,y + 5,10,70)
  canvas.drawRectFill(x + 25,y + 5,10,30)

def five(canvas,x,y): 
  #draw the number five 
  canvas.drawRectFill(x + 25,y + 5,50,10) 
  canvas.drawRectFill(x + 25,y + 15,10,20)
  canvas.drawRectFill(x + 25,y + 35,50,10)
  canvas.drawRectFill(x + 65,y + 45,10,20)
  canvas.drawRectFill(x + 25,y + 65,50,10)

def six(canvas,x,y): 
  #draw the number six
  canvas.drawRectFill(x + 25,y + 5,10,60)
  canvas.drawRectFill(x + 25,y + 65,50,10)
  canvas.drawRectFill(x + 25,y + 35,50,10)
  canvas.drawRectFill(x + 65,y + 45,10,20)

def seven(canvas,x,y): 
  #draw the number seven 
  canvas.drawRectFill(x + 65,y + 15,10,60)
  canvas.drawRectFill(x + 25,y + 5,50,10) 

def eight(canvas,x,y): 
  #draw the number eight 
  canvas.drawRectFill(x + 25,y + 5,50,10) 
  canvas.drawRectFill(x + 25,y + 15,10,20)
  canvas.drawRectFill(x + 25,y + 35,50,10)
  canvas.drawRectFill(x + 65,y + 45,10,20)
  canvas.drawRectFill(x + 25,y + 65,50,10)
  canvas.drawRectFill(x + 65,y + 15,10,20)
  canvas.drawRectFill(x + 25,y + 45,10,20)

def nine(canvas,x,y): 
  #draw the number nine 
  canvas.drawRectFill(x + 25,y + 5,50,10) 
  canvas.drawRectFill(x + 25,y + 15,10,20)
  canvas.drawRectFill(x + 65,y + 15,10,60)
  canvas.drawRectFill(x + 25,y + 35,50,10)

def ten(canvas,x,y): 
  canvas.drawRectFill(x + 20,y + 5,10,70)
  canvas.drawRectFill(x + 45,y + 5,10,70)
  canvas.drawRectFill(x + 70,y + 5,10,70)
  canvas.drawRectFill(x + 45,y + 5,35,10)
  canvas.drawRectFill(x + 45,y + 65,35,10)

def jack(canvas,x,y): 
  #draw the letter J 
  canvas.drawRectFill(x + 25,y + 5,50,10) 
  canvas.drawRectFill(x + 45,y + 5,10,70) 
  canvas.drawRectFill(x + 30,y + 65,20,10)

def queen(canvas,x,y): 
  #draw the letter Q 
  canvas.drawRectFill(x + 25,y + 5,50,10) 
  canvas.drawRectFill(x + 25,y + 15,10,50)
  canvas.drawRectFill(x + 65,y + 15,10,50)
  canvas.drawRectFill(x + 25,y + 55,50,10)
  canvas.drawPolygonFill([(x + 55,y + 45),(x + 62,y + 45),(x + 75,y + 67),(x + 82,y + 67)])

def king(canvas,x,y): 
  #draw the letter K 
  canvas.drawRectFill(x + 25,y + 5,10,70)
  canvas.drawPolygonFill([(x + 65,y + 5),(x + 75,y + 5),(x + 35,y + 45),(x + 35,y + 35)])
  canvas.drawPolygonFill([(x + 75,y + 75),(x + 65,y + 75),(x + 35,y + 45),(x + 35,y + 35)])
 
def ace(canvas,x,y): 
  #draw the letter A 
  canvas.drawRectFill(x + 25,y + 5,10,70)
  canvas.drawRectFill(x + 65,y + 5,10,70)
  canvas.drawRectFill(x + 25,y + 5,50,10) 
  canvas.drawRectFill(x + 25,y + 30,50,10) 

def hearts(canvas,x,y): 
 canvas.drawPolygonFill([(x + 50,y + 75),(x + 20,y + 35),(x + 80,y + 35)])
 canvas.drawCircleFill(x+ 68,y + 25,16)
 canvas.drawCircleFill(x + 32,y + 25,16)
 canvas.drawPolygonFill([(x + 50,y + 25),(x + 40,y + 40),(x + 60,y + 40)])

def spades(canvas,x,y): 
 canvas.drawPolygonFill([(x + 50,y + 60),(x + 65,y + 75),(x + 35,y + 75)])
 canvas.drawPolygonFill([(x + 50,y + 5),(x + 20,y + 45),(x + 80,y + 45)])
 canvas.drawCircleFill(x+ 65,y + 50,15)
 canvas.drawCircleFill(x + 35,y + 50,15)

def diamonds(canvas,x,y): 
  canvas.drawPolygonFill([(x + 50,y + 5),(x + 75,y + 40),(x + 50,y + 75),(x + 25,y + 40)])

def clubs(canvas,x,y): 
  canvas.drawPolygonFill([(x + 50,y + 60),(x + 65,y + 75),(x + 35,y + 75)])
  canvas.drawCircleFill(x+ 50,y + 20,15)
  canvas.drawCircleFill(x + 65,y + 45,15)
  canvas.drawCircleFill(x + 35,y + 45,15)
  canvas.drawRectFill(x+40,y+30,15,15)
  canvas.drawRectFill(x+45,y+40,10,30)

def winner(canvas,x,y): 
  #set color to white 
  canvas.setFillColor(255,255,255)
  #make the whole background white
  canvas.drawRectFill(0,0,525,500)
  #set color to yellow
  canvas.setFillColor(255,255,0)
  #set outline color to black 
  canvas.setOutlineColor(0,0,0)

  #Y
  canvas.drawPolygonFill([(175,50),(125,50),(100,100),(75,50),(25,50),(75,130),(75,225),(125,225),(125,130)])
  #O
  canvas.drawPolygonFill([(200,50),(200,225),(325,225),(325,50)])
  canvas.setFillColor(255,255,255)
  canvas.drawPolygonFill([(250,100),(250,175),(275,175),(275,100)])
  #U
  canvas.setFillColor(255,255,0)
  canvas.drawPolygonFill([(350,50),(400,50),(400,175),(450,175),(450,50),(500,50),(500,225),(350,225)])

  #W
  canvas.drawPolygonFill([(25,275),(75,275),(75,375),(100,325),(125,375),(125,275),(175,275),(175,450),(125,450),(100,400),(75,450),(25,450)])
  #I
  canvas.drawPolygonFill([(200,275),(325,275),(325,325),(285,325),(285,400),(325,400),(325,450),(200,450),(200,400),(240,400),(240,325),(200,325)])
  #N
  canvas.drawPolygonFill([(350,275),(400,275),(450,375),(450,275),(500,275),(500,450),(450,450),(400,350),(400,450),(350,450)])

def loser(canvas,x,y): 
  #set color to black 
  canvas.setFillColor(0,0,0)
  #make the whole background black
  canvas.drawRectFill(0,0,525,500)
  #set color to red
  canvas.setFillColor(255,0,0)

  #Y
  canvas.drawPolygonFill([(175,50),(125,50),(100,100),(75,50),(25,50),(75,130),(75,225),(125,225),(125,130)])
  #O
  canvas.drawPolygonFill([(200,50),(200,225),(325,225),(325,50)])
  canvas.setFillColor(0,0,0)
  canvas.drawPolygonFill([(250,100),(250,175),(275,175),(275,100)])
  #U
  canvas.setFillColor(255,0,0)
  canvas.drawPolygonFill([(350,50),(400,50),(400,175),(450,175),(450,50),(500,50),(500,225),(350,225)])

  #L
  canvas.drawPolygonFill([(25,275),(75,275),(75,400),(130,400),(130,450),(25,450)])
  #O
  canvas.drawRectFill(140,275,110,175)
  canvas.setFillColor(0,0,0)
  canvas.drawRectFill(180,315,30,95)
  #S
  canvas.setFillColor(255,0,0)
  canvas.drawPolygonFill([(270,275),(380,275),(380,325),(300,325),(300,350),(380,350),(380,450),(270,450),(270,400),(350,400),(350,375),(270,375)])
  #E
  canvas.drawPolygonFill([(400,275),(515,275),(515,325),(450,325),(450,350),(475,350),(475,375),(450,375),(450,400),(515,400),(515,450),(400,450)])