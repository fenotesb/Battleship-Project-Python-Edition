from graphics import *
from random import randrange

# creats players
class players:
    def __init__ (self,name,):
        self.name = name
    def wins (self,win):
        Wintext = Rectangle(Point(0,0), Point(25,25))
        Wintext.setFill("light green")
        Wintext.draw(win)
        text =Text(Point(13,13),"You Win")
        text.setSize(20)
        text.draw(win)

    def lose (self,win):
        Ltext = Rectangle(Point(0,0), Point(25,25))
        Ltext.setFill("light green")
        Ltext.draw(win)
        text =Text(Point(13,13),"You Lose")
        text.setSize(20)
        text.draw(win)
 #make window   
def window():
    win=GraphWin("Project",600,600)
    win.setBackground("light blue")
    win.setCoords(0,0,25,25)
    return win
#draws the board
def makeBattleGround(win):

    rec = Rectangle(Point(2,2), Point(16,16))
    rec.setFill("light blue")
    rec.draw(win)
    #draw vertical lines

    for i in range(2,16,2):
        aLine = Line(Point(i,2), Point(i,16))
        aLine.draw(win)
    for i in range(2,16,2):
        aLine = Line(Point(2,i), Point(16,i))
        aLine.draw(win)
    border = Rectangle(Point(8,16), Point(10,2))
    border.setFill("tan")
    border.draw(win)
#Displays the welcome box
def welcome(win):
    welcomerec = Rectangle(Point(2,21.5), Point(24,24.5))
    welcomerec.setFill("light green")
    welcomerec.draw(win)
    welcometext =Text(Point(13,23),"Welcome to BattleShip")
    welcometext.setSize(27)
    welcometext.draw(win)
#Displays the sumbit box
def submitbox(win):
    submitbox = Rectangle(Point(18,18), Point(24,20))
    submitbox.draw(win)
    submitbox.setFill("light green")
    submitboxText = Text(Point(21,19),"Submit")
    submitboxText.setSize(20)
    submitboxText.draw(win)

#Labels the graph     
def labelGrid(win):
    counter = 0
    for col in range (3,17,2):
        labelNum= ["A", "B", "C","D","E","F","G"]
        #Fill in values for the Point coordinates

        label=Text(Point(  1   ,  col  ),str(labelNum[counter]))
        label.setSize(18)
        label.draw(win)
        counter = counter +1
    counter = 0
    for row in [3,5,7]:
        labelNum1=["1","2","3"]
        #Fill in values for the Point coordinates
        label=Text(Point(   row  ,  1   ),str(labelNum1[counter]))
        label.setSize(18)
        label.draw(win)
        counter = counter +1
    counter = 0
    for row in [11,13,15]:
        labelNum2=["1","2","3"]
        #Fill in values for the Point coordinates
        label=Text(Point(   row  ,  1   ),str(labelNum2[counter]))
        label.setSize(18)
        label.draw(win)
        counter = counter +1
#puts the new winner out 
def winor (win,fname,winner):
    #tells program where to put staments
    outfile = open(fname+".txt","w")
    print (winner,"(1-0)",file = outfile )


    outfile.close()
    
def Loseor (win,fname,LOOSER):
    #tells program where to put staments
    outfile = open(fname+".txt","w")
    print (LOOSER,"(0-1)",file = outfile )


    outfile.close()
#draws the record box
    
def recordboxgAME (win,fname ):
    infile = open(fname+".txt","r")
    counter = 0
    Recordbox = Rectangle(Point(17,2), Point(24,8))
    Recordbox.setFill("light green")
    Recordbox.draw(win)
    aLine =Line(Point(17   ,  7 ),Point(   24,  7 ))
    aLine.draw(win)
    for line in infile:
        datasplit = line.split()
        name=datasplit[0]
        record = datasplit[1]
        namelabel=Text(Point(   19  ,7.5- counter  ),str(name))
        namelabel.setSize(12)
        namelabel.draw(win)
        Reclabel=Text(Point(   22  ,7.5- counter  ),str(record))
        Reclabel.setSize(12)
        Reclabel.draw(win)
        counter = counter+1
    infile.close()
    
def recordbox (win,fname ):
    infile = open(fname+".txt","r")
    counter = 0
    Recordbox = Rectangle(Point(17,2), Point(24,8))
    Recordbox.setFill("light green")
    Recordbox.draw(win)
    aLine =Line(Point(17   ,  7 ),Point(   24,  7 ))
    aLine.draw(win)
    for line in infile:
        datasplit = line.split()
        name=datasplit[0]
        record = datasplit[1]
        namelabel=Text(Point(   19  ,7.5- counter  ),str(name))
        namelabel.setSize(12)
        namelabel.draw(win)
        Reclabel=Text(Point(   22  ,7.5- counter  ),str(record))
        Reclabel.setSize(12)
        Reclabel.draw(win)
        counter = counter+1
    infile.close()
#make the text box to ask questions
def maketextbox(win):
    textboxQ = Rectangle(Point(2,18), Point(16,20))
    textboxQ.setFill("white")
    textboxQ.draw(win)
    return textboxQ
#errors 
def validateinput(userinput):
    userinput = userinput.strip()
    result = True
    if len(userinput) != 2:
        result = False
    elif not ('A' <= userinput[0] <= 'G'):
        result = False
    elif not ('1' <= userinput[1] <= '3'):
        result = False
    return result
#draws the error box
def errorbox (win,n,error):
    errorbox = Rectangle(Point(17,9), Point(24,16))
    errorbox.setFill("light green")
    errorbox.draw(win)

    if n == "1" :
        submitboxText = Text(Point(20.5,15),str(error)+" is an invalid entry ")
        submitboxText1 = Text(Point(20.5,14),"please input a 6 letter name")
        submitboxText2 = Text(Point(20.5,13),"to continue ")
        submitboxText.setSize(10)
        submitboxText.draw(win)
        submitboxText1.setSize(10)
        submitboxText1.draw(win)
        S = "-1"
        return S
 
    if n == "2" :
        submitboxText2 = Text(Point(20.5,15),str(error)+" is an invalid entry  ")
        submitboxText3 = Text(Point(20.5,14),"please input H or V")
        submitboxText4 = Text(Point(20.5,13),"to continue ")
        submitboxText2.setSize(12)
        submitboxText2.draw(win)
        submitboxText3.setSize(12)
        submitboxText3.draw(win)
        submitboxText4.setSize(12)
        submitboxText4.draw(win)
        S = "-2"
        
#ask the user for their name
     
def stepOne(win,textboxQ):
    
    Quest1 = Text(Point(8,19),"Please enter username(<=6 letters ): ")
    Quest1.setSize(10)
    Quest1.draw(win)
   
    Ans1 = Entry(Point(14.5,19),6)
    Ans1.draw(win)
    firstmove = win.getMouse()
    xplace=firstmove.getX()
    yplace=firstmove.getY()
    errors = "0"
    while firstmove != (xplace >= 18 and yplace >= 18 and xplace <=24 and yplace <=20):
        firstmove = win.getMouse()
        xplace=firstmove.getX()
        yplace=firstmove.getY()
        if xplace >= 18 and yplace >= 18 and xplace <=24 and yplace <=20:
            name = Ans1.getText()
            lengthName =len(name)
            while lengthName >6:
                errors = errorbox(win,"1",name)
                win.getMouse()
                name = Ans1.getText()
                lengthName =len(name)
            if errors == "-1":
                error = errorbox(win,errors,name)
            Quest1.undraw()
            Ans1.undraw()
            return name
# inputs a vertical or horizontal ship
def stepTwo(win,textboxQ):
    #draws text on screen
    Quest2 = Text(Point(8,19.5),"Would you like a horizontal ")
    Quest2.setSize(10)
    Quest2.draw(win)
    Quest2_1 = Text(Point(8,18.5),"or vertical ship?(H/V):")
    Quest2_1.setSize(10)
    Quest2_1.draw(win)
    #draws entry box
    Ans2 = Entry(Point(12.5,19),1)
    Ans2.draw(win)
    firstmove = win.getMouse()
    #waits for the user to click submit
    xplace=firstmove.getX()
    yplace=firstmove.getY()
    errors = 0
    nextmove = 0
    dirction = 0
    #makes sure the program only moves on if the user hits submit
    while firstmove != (xplace >= 18 and yplace >= 18 and xplace <=24 and yplace <=20):
        firstmove = win.getMouse()
        xplace=firstmove.getX()
        yplace=firstmove.getY()
        #cont. when the user hits submit
        if xplace >= 18 and yplace >= 18 and xplace <=24 and yplace <=20:
        #looks for the users input 
            entry = Ans2.getText()
            dirction = ord(entry)
        #if the user put's the wrong input makes them try again
        if dirction !=( 72):
            if dirction != (86):
#error text appears
                errors = errorbox(win,"2",entry)
        if dirction == 72 :
            letter = chr(dirction)
            error = errorbox(win,"-2",entry)
            
            Quest2.undraw()
            Quest2_1.undraw()
            Ans2.undraw()
            return letter
        if dirction == 86:
            letter = chr(dirction)
            error = errorbox(win,"-2",entry)
            
            Quest2.undraw()
            Quest2_1.undraw()
            Ans2.undraw()
            return letter
        
#does the attaxck
def attack(win,textq):
#Creates text box
    Quest3 = Text(Point(8,19),"Where would you like to Attack? ")
    Quest3.setSize(10)
    Quest3.draw(win)
#make entry box
    Ans3 = Entry(Point(12.5,19),2)
    Ans3.draw(win)
    while not validateinput(Ans3.getText()):
        Ans3.setText('')
        firstmove = win.getMouse()
    xplace=firstmove.getX()
    yplace=firstmove.getY()
    ShipCenter = 0
    ycord =0
#makes sure the only the sumbit click matters
    
    while firstmove != (xplace >= 18 and yplace >= 18 and xplace <=24 and yplace <=20):
        firstmove = win.getMouse()
        xplace=firstmove.getX()
        yplace=firstmove.getY()
        #onces you hit submit it takes the input
        if xplace >= 18 and yplace >= 18 and xplace <=24 and yplace <=20:
            locationb = Ans3.getText()
            location = str(locationb)
            ymakeup = ord(location[0])
            letter = location[0]
            #convers the input to cooridates 
            if location[1] == "1":
                if letter == "A":
                    ycord = ymakeup- (62)
                elif letter == "B":
                    ycord = ymakeup- (61)
                elif letter == "C":
                    ycord = ymakeup- (60)
                elif letter == "D":
                    ycord = ymakeup- (59)
                elif letter == "E":
                    ycord = ymakeup- (58)
                elif letter == "F":
                    ycord = ymakeup- (57)
                elif letter == "G":
                    ycord = ymakeup- (56)
                ShipCenter = [11,ycord]
            elif location[1] == "2":
                if letter == "A":
                    ycord = ymakeup- (62)
                elif letter == "B":
                    ycord = ymakeup- (61)
                elif letter == "C":
                    ycord = ymakeup- (60)
                elif letter == "D":
                    ycord = ymakeup- (59)
                elif letter == "E":
                    ycord = ymakeup- (58)
                elif letter == "F":
                    ycord = ymakeup- (57)
                elif letter == "G":
                    ycord = ymakeup- (56)
                ShipCenter = [13,ycord] 
            elif location[1] == "3":
                if letter == "A":
                    ycord = ymakeup- (62)
                elif letter == "B":
                    ycord = ymakeup- (61)
                elif letter == "C":
                    ycord = ymakeup- (60)
                elif letter == "D":
                    ycord = ymakeup- (59)
                elif letter == "E":
                    ycord = ymakeup- (58)
                elif letter == "F":
                    ycord = ymakeup- (57)
                elif letter == "G":
                    ycord = ymakeup- (56)
                ShipCenter = [15,ycord]
            Quest3.undraw()
            Ans3.undraw()
            ShipCenter.append(location)
            return ShipCenter
    
def stepthree(win,textboxQ):
    Quest3 = Text(Point(8,19),"Where would you like to doc? ")
    Quest3.setSize(10)
    Quest3.draw(win)
    Ans3 = Entry(Point(12.5,19),2)
    Ans3.draw(win)
    while not validateinput(Ans3.getText()):
        Ans3.setText('')
        firstmove = win.getMouse()
    xplace=firstmove.getX()
    yplace=firstmove.getY()
    ShipCenter = 0
    ycord =0
    
    while firstmove != (xplace >= 18 and yplace >= 18 and xplace <=24 and yplace <=20):
        firstmove = win.getMouse()
        xplace=firstmove.getX()
        yplace=firstmove.getY()
        if xplace >= 18 and yplace >= 18 and xplace <=24 and yplace <=20:
            location = Ans3.getText()
            ymakeup = ord(location[0])
            letter = location[0]
            if location[1] == "1":
                if letter == "A":
                    ycord = ymakeup- (62)
                elif letter == "B":
                    ycord = ymakeup- (61)
                elif letter == "C":
                    ycord = ymakeup- (60)
                elif letter == "D":
                    ycord = ymakeup- (59)
                elif letter == "E":
                    ycord = ymakeup- (58)
                elif letter == "F":
                    ycord = ymakeup- (57)
                elif letter == "G":
                    ycord = ymakeup- (56)
                ShipCenter = [3,ycord]
            elif location[1] == "2":
                if letter == "A":
                    ycord = ymakeup- (62)
                elif letter == "B":
                    ycord = ymakeup- (61)
                elif letter == "C":
                    ycord = ymakeup- (60)
                elif letter == "D":
                    ycord = ymakeup- (59)
                elif letter == "E":
                    ycord = ymakeup- (58)
                elif letter == "F":
                    ycord = ymakeup- (57)
                elif letter == "G":
                    ycord = ymakeup- (56)
                ShipCenter = [5,ycord]
            elif location[1] == "3":
                if letter == "A":
                    ycord = ymakeup- (62)
                elif letter == "B":
                    ycord = ymakeup- (61)
                elif letter == "C":
                    ycord = ymakeup- (60)
                elif letter == "D":
                    ycord = ymakeup- (59)
                elif letter == "E":
                    ycord = ymakeup- (58)
                elif letter == "F":
                    ycord = ymakeup- (57)
                elif letter == "G":
                    ycord = ymakeup- (56)
                ShipCenter = [7,ycord]
            Quest3.undraw()
            Ans3.undraw()
            ShipCenter.append(location)
            return ShipCenter
def checkdoc(win, ShipX,ShipY,HorV):
    xup = ShipX+2
    yup = ShipY+2
    xdown= ShipX-2
    ydown = ShipY-2
     
    if HorV == "V":
        if ShipX >= 3 and ydown >= 3 and ShipX <=7 and yup <=15:
            return 1
        else:
            x=errorbox (win,"4",0)
            return 4
    if HorV == "H":
        
        if xdown >= 3 and ShipY >= 3 and ydown <=7 and ShipY <=15:
            return 1

        else:
            x=errorbox (win,"4",0)
            return 4
                
            
def DrawMyShip(win,ShipX,ShipY,HorV):
    xup = ShipX+2
    yup = ShipY+2
    xdown= ShipX-2
    ydown = ShipY-2
    Cir = Circle(Point(ShipX,ShipY), 1)
    Cir.setFill("grey")
    Cir.draw(win)
    
    if HorV == "V":
        
        if ShipX >= 3 and ydown >= 3 and ShipX <=7 and yup <=15:
            aCircle = Circle(Point(ShipX,ydown), 1)
            aCircle.setFill("grey")
            aCircle.draw(win)
            bCircle = Circle(Point(ShipX,yup), 1)
            bCircle.setFill("grey")
            bCircle.draw(win)
        
            
    if HorV == "H":
        if xdown >= 3 and ShipY >= 3 and xup <=7 and ShipY <=15:
            aCircle = Circle(Point(xdown,ShipY), 1)
            aCircle.setFill("grey")
            aCircle.draw(win)
            bCircle = Circle(Point(xup,ShipY), 1)
            bCircle.setFill("grey")
            bCircle.draw(win)

def DrawCpuShip(win):
    chance =randrange(0,5)
    ShipX = 13
    horv = randrange(0,2)
    dic = ["H","V"]
    centerY = [5,7,9,11,13]
    ShipY = centerY[chance]
    xup = ShipX+2
    yup = ShipY+2
    xdown= ShipX-2
    ydown = ShipY-2
    
    HorV = dic[horv]
    
    
    Cir = Circle(Point(ShipX,ShipY), 1)
    Cir.setFill("grey")
    Cir.draw(win)
    
    if HorV == "V":
        aCircle = Circle(Point(ShipX,ydown), 1)
        aCircle.setFill("grey")
        aCircle.draw(win)
        bCircle = Circle(Point(ShipX,yup), 1)
        bCircle.setFill("grey")
        bCircle.draw(win)
    
    
            
    if HorV == "H":
        
        aCircle = Circle(Point(xdown,ShipY), 1)
        aCircle.setFill("grey")
        aCircle.draw(win)
        bCircle = Circle(Point(xup,ShipY), 1)
        bCircle.setFill("grey")
        bCircle.draw(win)
    Cpulet = 0
    if ShipY == 3:
        Cpulet = "A"
    if ShipY == 5:
        Cpulet = "B"
    if ShipY == 7:
        Cpulet = "C"
    if ShipY == 9:
        Cpulet = "D"
    if ShipY == 11:
        Cpulet = "E"
    if ShipY == 13:
        Cpulet = "F"
    if ShipY == 15:
        Cpulet = "G"
    print (ShipX,Cpulet,HorV,"this is that part")
    return ShipX,Cpulet,HorV


    
    
        
def playerlist(ShipX,letterLoc,HorV):
    Hones = ["A","B","C","D","E","F","G"]
    
    Htwos = ["A","B","C","D","E","F","G"]
    
    Hthree = ["A","B","C","D","E","F","G"]
 

    #alters the list so we can see where the ship at via the list

    if ShipX == 3:
        if letterLoc == "B":
            Hones.remove("B")
            Hones.insert(1,"S")
            if HorV == "V":
                Hones.remove("C")
                Hones.insert(2,"S")
                Hones.remove("A")
                Hones.insert(0,"S")
                
        elif letterLoc == "C":
            Hones.remove("C")
            Hones.insert(2,"S")

            if HorV == "V":
                Hones.remove("D")
                Hones.insert(3,"S")
                Hones.remove("B")
                Hones.insert(1,"S")
        elif letterLoc == "D":
            Hones.remove("D")
            Hones.insert(3,"S")

            if HorV == "V":
                Hones.remove("E")
                Hones.insert(4,"S")
                Hones.remove("C")
                Hones.insert(2,"S")
            
        elif letterLoc == "E":
            Hones.remove("E")
            Hones.insert(4,"S")

            if HorV == "V":
                Hones.remove("F")
                Hones.insert(5,"S")
                Hones.remove("D")
                Hones.insert(3,"S")
        elif letterLoc == "F":
            Hones.remove("F")
            Hones.insert(5,"S")


            if HorV == "V":
                Hones.remove("G")
                Hones.insert(6,"S")
                Hones.remove("E")
                Hones.insert(4,"S")
    if ShipX == 5:
        if letterLoc == "A":
            Htwos.remove("A")
            Htwos.insert(0,"S")
            if Htwos == "H":
                Hones.remove("A")
                Hones.insert(0,"S")
                Hthree.remove("A")
                Hthree.insert(0,"S")
            
        elif letterLoc == "B":
            Htwos.remove("B")
            Htwos.insert(1,"S")
            
            if HorV == "H":
                Hones.remove("B")
                Hones.insert(1,"S")
                Hthree.remove("B")
                Hthree.insert(1,"S")

            if HorV == "V":
                Htwos.remove("C")
                Htwos.insert(2,"S")
                Htwos.remove("A")
                Htwos.insert(0,"S")
                
        elif letterLoc == "C":
            Htwos.remove("C")
            Htwos.insert(2,"S")
            if HorV == "H":
                Hones.remove("C")
                Hones.insert(2,"S")
                Hthree.remove("C")
                Hthree.insert(2,"S")

            if HorV == "V":
                Htwos.remove("D")
                Htwos.insert(3,"S")
                Htwos.remove("B")
                Htwos.insert(1,"S")
        elif letterLoc == "D":
            Htwos.remove("D")
            Htwos.insert(3,"S")

            if HorV == "H":
                Hones.remove("D")
                Hones.insert(3,"S")
                Hthree.remove("D")
                Hthree.insert(3,"S")

            if HorV == "V":
                Htwos.remove("E")
                Htwos.insert(4,"S")
                Htwos.remove("C")
                Htwos.insert(2,"S")
            
        elif letterLoc == "E":
            Htwos.remove("E")
            Htwos.insert(4,"S")

            if HorV == "H":
                Hones.remove("E")
                Hones.insert(4,"S")
                Hthree.remove("E")
                Hthree.insert(4,"S")

            if HorV == "V":
                Htwos.remove("F")
                Htwos.insert(5,"S")
                Htwos.remove("D")
                Htwos.insert(3,"S")
        elif letterLoc == "F":
            Htwos.remove("F")
            Htwos.insert(5,"S")

            if HorV == "H":
                Hones.remove("F")
                Hones.insert(5,"S")
                Hthree.remove("F")
                Hthree.insert(5,"S")

            if HorV == "V":
                Htwos.remove("G")
                Htwos.insert(6,"S")
                Htwos.remove("E")
                Htwos.insert(4,"S")
        elif letterLoc == "G":
            Htwos.remove("G")
            Htwos.insert(6,"S")
            if HorV == "H":
                Hones.remove("G")
                Hones.insert(6,"S")
                Hthree.remove("G")
                Hthree.insert(6,"S")
    if ShipX == 7:
        if letterLoc == "B":
            Hthree.remove("B")
            Hthree.insert(1,"S")
            if HorV == "V":
                Hthree.remove("C")
                Hthree.insert(2,"S")
                Hthree.remove("A")
                Hthree.insert(0,"S")
                
        elif letterLoc == "C":
            Hthree.remove("C")
            Hthree.insert(2,"S")

            if HorV == "V":
                Hthree.remove("D")
                Hthree.insert(3,"S")
                Hthree.remove("B")
                Hthree.insert(1,"S")
        elif letterLoc == "D":
            Hthree.remove("D")
            Hthree.insert(3,"S")

            if HorV == "V":
                Hthree.remove("E")
                Hthree.insert(4,"S")
                Hthree.remove("C")
                Hthree.insert(2,"S")
            
        elif letterLoc == "E":
            Hthree.remove("E")
            Hthree.insert(4,"S")

            if HorV == "V":
                Hthree.remove("F")
                Hthree.insert(5,"S")
                Hthree.remove("D")
                Hthree.insert(3,"S")
        elif letterLoc == "F":
            Hthree.remove("F")
            Hthree.insert(5,"S")


            if HorV == "V":
                Hthree.remove("G")
                Hthree.insert(6,"S")
                Hthree.remove("E")
                Hthree.insert(4,"S")

    
    return Hones, Htwos, Hthree

def Cpulist(ShipX,letterLoc,HorV):
    
    Hones = ["A","B","C","D","E","F","G"]
    CPUones = ["A","B","C","D","E","F","G"]
    Htwos = ["A","B","C","D","E","F","G"]
    CPUtwos = ["A","B","C","D","E","F","G"]
    Hthree = ["A","B","C","D","E","F","G"]
    CPUthree=  ["A","B","C","D","E","F","G"]
#alters the list so we can see where the ship at via the list
    if ShipX == 11:
        if letterLoc == "B":
            Hones.remove("B")
            Hones.insert(1,"S")
            if HorV == "V":
                Hones.remove("C")
                Hones.insert(2,"S")
                Hones.remove("A")
                Hones.insert(0,"S")
                
        elif letterLoc == "C":
            Hones.remove("C")
            Hones.insert(2,"S")

            if HorV == "V":
                Hones.remove("D")
                Hones.insert(3,"S")
                Hones.remove("B")
                Hones.insert(1,"S")
        elif letterLoc == "D":
            Hones.remove("D")
            Hones.insert(3,"S")

            if HorV == "V":
                Hones.remove("E")
                Hones.insert(4,"S")
                Hones.remove("C")
                Hones.insert(2,"S")
            
        elif letterLoc == "E":
            Hones.remove("E")
            Hones.insert(4,"S")

            if HorV == "V":
                Hones.remove("F")
                Hones.insert(5,"S")
                Hones.remove("D")
                Hones.insert(3,"S")
        elif letterLoc == "F":
            Hones.remove("F")
            Hones.insert(5,"S")


            if HorV == "V":
                Hones.remove("G")
                Hones.insert(6,"S")
                Hones.remove("E")
                Hones.insert(4,"S")
    if ShipX == 13:
        if letterLoc == "A":
            Htwos.remove("A")
            Htwos.insert(0,"S")
            if Htwos == "H":
                Hones.remove("A")
                Hones.insert(0,"S")
                Hthree.remove("A")
                Hthree.insert(0,"S")
            
        elif letterLoc == "B":
            Htwos.remove("B")
            Htwos.insert(1,"S")
            
            if HorV == "H":
                Hones.remove("B")
                Hones.insert(1,"S")
                Hthree.remove("B")
                Hthree.insert(1,"S")

            if HorV == "V":
                Htwos.remove("C")
                Htwos.insert(2,"S")
                Htwos.remove("A")
                Htwos.insert(0,"S")
                
        elif letterLoc == "C":
            Htwos.remove("C")
            Htwos.insert(2,"S")
            if HorV == "H":
                Hones.remove("C")
                Hones.insert(2,"S")
                Hthree.remove("C")
                Hthree.insert(2,"S")

            if HorV == "V":
                Htwos.remove("D")
                Htwos.insert(3,"S")
                Htwos.remove("B")
                Htwos.insert(1,"S")
        elif letterLoc == "D":
            Htwos.remove("D")
            Htwos.insert(3,"S")

            if HorV == "H":
                Hones.remove("D")
                Hones.insert(3,"S")
                Hthree.remove("D")
                Hthree.insert(3,"S")

            if HorV == "V":
                Htwos.remove("E")
                Htwos.insert(4,"S")
                Htwos.remove("C")
                Htwos.insert(2,"S")
            
        elif letterLoc == "E":
            Htwos.remove("E")
            Htwos.insert(4,"S")

            if HorV == "H":
                Hones.remove("E")
                Hones.insert(4,"S")
                Hthree.remove("E")
                Hthree.insert(4,"S")

            if HorV == "V":
                Htwos.remove("F")
                Htwos.insert(5,"S")
                Htwos.remove("D")
                Htwos.insert(3,"S")
        elif letterLoc == "F":
            Htwos.remove("F")
            Htwos.insert(5,"S")

            if HorV == "H":
                Hones.remove("F")
                Hones.insert(5,"S")
                Hthree.remove("F")
                Hthree.insert(5,"S")

            if HorV == "V":
                Htwos.remove("G")
                Htwos.insert(6,"S")
                Htwos.remove("E")
                Htwos.insert(4,"S")
        elif letterLoc == "G":
            Htwos.remove("G")
            Htwos.insert(6,"S")
            if HorV == "H":
                Hones.remove("G")
                Hones.insert(6,"S")
                Hthree.remove("G")
                Hthree.insert(6,"S")
    if ShipX == 15:
        if letterLoc == "B":
            Hthree.remove("B")
            Hthree.insert(1,"S")
            if HorV == "V":
                Hthree.remove("C")
                Hthree.insert(2,"S")
                Hthree.remove("A")
                Hthree.insert(0,"S")
                
        elif letterLoc == "C":
            Hthree.remove("C")
            Hthree.insert(2,"S")

            if HorV == "V":
                Hthree.remove("D")
                Hthree.insert(3,"S")
                Hthree.remove("B")
                Hthree.insert(1,"S")
        elif letterLoc == "D":
            Hthree.remove("D")
            Hthree.insert(3,"S")

            if HorV == "V":
                Hthree.remove("E")
                Hthree.insert(4,"S")
                Hthree.remove("C")
                Hthree.insert(2,"S")
            
        elif letterLoc == "E":
            Hthree.remove("E")
            Hthree.insert(4,"S")

            if HorV == "V":
                Hthree.remove("F")
                Hthree.insert(5,"S")
                Hthree.remove("D")
                Hthree.insert(3,"S")
        elif letterLoc == "F":
            Hthree.remove("F")
            Hthree.insert(5,"S")


            if HorV == "V":
                Hthree.remove("G")
                Hthree.insert(6,"S")
                Hthree.remove("E")
                Hthree.insert(4,"S")

    
    return Hones, Htwos, Hthree



def DrawMyAttackHit(win,ShipX,ShipY,):
    Cir = Circle(Point(ShipX,ShipY), 1)
    Cir.setFill("red")
    Cir.draw(win)

def DrawMyAttackmiss(win,ShipX,ShipY,):
    Cir = Circle(Point(ShipX,ShipY), 1)
    Cir.setFill("blue")
    Cir.draw(win) 

    
def DrawCpuAttack(win,ShipX,ShipY,):
    Cir = Circle(Point(ShipX,ShipY), 1)
    Cir.setFill("blue")
    Cir.draw(win) 

def cpucheck(Cpuguesslist,Cpuletter,CpuGuessX):
    for i in Cpuguesslist :
        if i == Cpuletter+CpuGuessX:
            return False
    return True
            
    
def main():
    win = window()
    Grid=makeBattleGround(win)
    Gridlabels = labelGrid(win)
    wel =welcome(win)
    textq = maketextbox(win)
    submit = submitbox(win)
    Hit = 0
    miss = 0
    ShipHit= 0

    
    
    Hones = ["A","B","C","D","E","F","G"]
    CPUones = ["A","B","C","D","E","F","G"]
    Htwos = ["A","B","C","D","E","F","G"]
    CPUtwos = ["A","B","C","D","E","F","G"]
    Hthree = ["A","B","C","D","E","F","G"]
    CPUthree=  ["A","B","C","D","E","F","G"]

    fname= "Record"
    Winbox =recordbox(win,fname )

    Name = stepOne(win,textq)
    
    
    HorV = stepTwo(win,textq)
    #returns the x y and string og location 
    ShipX,ShipY,location = stepthree(win,textq)
    
    #draws ship
    ship = DrawMyShip(win,ShipX,ShipY,HorV)
    
    CpuShipX,CpuShipY,CpuHorV = DrawCpuShip(win)
    
    Player1 = players(Name)
    letterLoc = location[0]
    #human the computer side of the board
    Hones, Htwos, Hthree =playerlist(ShipX,letterLoc,HorV)
    #computses the computer side of the board
    CPUones,CPUtwos,CPUthree = Cpulist(CpuShipX,CpuShipY,CpuHorV)
    #returns the attack x y and string
    CpuXlist = ["1","2","3"]
    CpuYlistCpu= ["A","B","C","D","E","F","G"]
    Cpuguesslist= []
    
    CpuShipHit = 0    
    while ShipHit != 3:
        CpuguessYIndex = randrange(0,7)
        
        Cpuletter = CpuYlistCpu[CpuguessYIndex]
    
        CpuguessY = 3+(2*(ord(Cpuletter)-ord("A")))
        
        CpuGuessXIndex = randrange(0,3)
       
        CpuGuessX = CpuXlist[CpuGuessXIndex]
    
        AttackpointX,AttackpointY,AttackLoc= attack(win,textq)
        AttackNum = AttackLoc[1]
        AttackLetter = AttackLoc[0]
        if AttackNum == "1" :
            if CPUones[ord(AttackLetter)-ord("A")] == 'S':
                f = DrawMyAttackHit(win,AttackpointX,AttackpointY)
                ShipHit = ShipHit +1
            if CPUones[ord(AttackLetter)-ord("A")] != 'S':
                f = DrawMyAttackmiss(win,AttackpointX,AttackpointY,)
                    
        if AttackNum == "2" :
            if CPUtwos[ord(AttackLetter)-ord("A")] == 'S':
                f = DrawMyAttackHit(win,AttackpointX,AttackpointY)
                ShipHit = ShipHit +1
            if CPUtwos[ord(AttackLetter)-ord("A")] != 'S':
                f = DrawMyAttackmiss(win,AttackpointX,AttackpointY,)
        if AttackNum == "3" :
            if CPUthree[ord(AttackLetter)-ord("A")] == 'S':
                f = DrawMyAttackHit(win,AttackpointX,AttackpointY)
                ShipHit = ShipHit +1
            if CPUthree[ord(AttackLetter)-ord("A")] != 'S':
                f = DrawMyAttackmiss(win,AttackpointX,AttackpointY)
        check = cpucheck(Cpuguesslist,Cpuletter,CpuGuessX)
        if check == True :
            if CpuGuessX == "1" :
                if Hones[ord(Cpuletter)-ord("A")] == 'S':
                    
                    f = DrawMyAttackHit(win,3,CpuguessY)
                    CpuShipHit = CpuShipHit +1
                if Hones[ord(Cpuletter)-ord("A")] != 'S':
                    f = DrawMyAttackmiss(win,3,CpuguessY,)
            if CpuGuessX == "2" :
                if Htwos[ord(Cpuletter)-ord("A")] == 'S':
                    f = DrawMyAttackHit(win,5,CpuguessY)
                    CpuShipHit = CpuShipHit +1
                if Htwos[ord(Cpuletter)-ord("A")] != 'S':
                    f = DrawMyAttackmiss(win,5,CpuguessY,)
                    
            if CpuGuessX =="3" :
                if Hthree[ord(Cpuletter)-ord("A")] == 'S':
                    
                    f = DrawMyAttackHit(win,7,CpuguessY)
                    CpuShipHit = CpuShipHit +1
                if Hthree[ord(Cpuletter)-ord("A")] != 'S':
                    f = DrawMyAttackmiss(win,7,CpuguessY,)
            
            Cpuguesslist.append(Cpuletter+CpuGuessX)
            if CpuShipHit == 3:
                break

    if CpuShipHit == 3:
        Player1.lose(win)
        looseer = Loseor (win,fname,Name)
    if ShipHit == 3:
        Player1.wins(win)
        wins= winor(win,fname,Name)


    
    GAME = recordboxgAME (win,fname )
    
main()
    
