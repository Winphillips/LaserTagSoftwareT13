from asyncio.windows_events import NULL
from cgitb import small
from msilib.schema import CheckBox
<<<<<<< HEAD
from select import select
=======
from Database import Database
>>>>>>> origin/RicardosBranch
import sys
from this import d
import pygame
import tkinter
import time # for the sleep function

#=====================================================================
#   Pass in database info from Database.py
#=====================================================================

# Initializes connection to Heroku and retrieves info from the database
database = Database()
database.RetrieveInfo()

#Initializes arrays to store the info from the database
idNumbers = []
firstNames = []
lastNames = []
codeNames = []

# Passes the database info from Database.py into here
database.PassInformation(idNumbers, firstNames, lastNames, codeNames)

# Test to make sure data is passed in correctly
print(idNumbers)
print(firstNames)
print(lastNames)
print(codeNames)

# Close connection to Heroku
database.CloseConnection()

#=====================================================================
#   Splash Screen
#=====================================================================
splashScreen = pygame.image.load("splashScreen2.png")
width, height = pygame.display.get_surface().get_size()
splashScreenPosition = (0,0) # splashscreen is positioned at the top left corner of the screen

# following lines just prevent the splash screen from stretching if the window is rectangular
if(width > height):
    splashScreenPosition = ((width - height) / 2,0) # centers the image horizontally
    width = height
elif(height > width):
    splashScreenPosition = ((height - width) / 2,0) # centers the image vertically
    height = width

splashScreen = pygame.transform.scale(splashScreen, (width,height))#Scales the splash screen to the size of the window

splashScreenTimer = 0 
while (splashScreenTimer < 5 * 1): # splash screen is up for 1 second
    screen.fill((5,225,255)) # screen filled with cyan
    screen.blit(splashScreen, splashScreenPosition) 
    pygame.display.flip()         
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit(), sys.exit()
    splashScreenTimer += 1
    time.sleep(.2) # only sleep for .2 seconds so that the program doesn't freeze from not responding to events

#=====================================================================
#   Player Entry Screen
#=====================================================================
# light shade of the button
checkBoxColor = (115,115,115)
checkBoxColorHover = (75,75,75)
# print(pygame.font.get_fonts())        # gets all fonts on system
# initialize font to (defualt pygame font, fontSize)
font = pygame.font.Font(None, 30)

# other variables
checkMark = pygame.image.load("checkMark.png")
checkMark = pygame.transform.scale(checkMark, (30, 30))

checkBoxes = []
smallTextBoxes = []
largeTextBoxes = []

for x in range(20): # make 20 left check boxes 
    checkBoxes.append([False, pygame.Rect(20, x * 33 + 56 ,15, 15)]) # left: whether the check appears on the box or not ||| right: stored the rect for drawing and mouse detection
for x in range(20): # make 20 right check boxes 
    checkBoxes.append([False, pygame.Rect(420, x * 33 + 56 ,15, 15)]) # left: whether the check appears on the box or not ||| right: stored the rect for drawing and mouse detection

for x in range(20): # make 20 left small text boxes
    smallTextBoxes.append(["", pygame.Rect(40, x * 33 + 50, 115, 30)]) 
for x in range(20): # make 20 right small text boxes 
    smallTextBoxes.append(["", pygame.Rect(440, x * 33 + 50, 115, 30)]) 

for x in range(20): # make 20 left large text boxes 
    largeTextBoxes.append(["", pygame.Rect(160, x * 33 + 50, 235, 30)]) 
for x in range(20): # make 20 right large text boxes 
    largeTextBoxes.append(["", pygame.Rect(560, x * 33 + 50, 235, 30)]) 

selected = [NULL, ""] #stores the currently selected textbox and the type of textbox (large or small) it is

#==================LOAD THE PLAYER LIST HERE==================#

#Change variable names to whatever fits best, all loading is done right here and the variables are not used again later
leftSideSmallText = ["test1"]
rightSideSmallText = ["yes", "mhm"]

leftSidelargeText = ["neat"]
rightSidelargeText = ["another test name", "last one"]


### load data into arrays here ###


##################################


#small text box loading:
for x in range(len(leftSideSmallText)):
     smallTextBoxes[x][0] = leftSideSmallText[x]

for x in range(len(rightSideSmallText)):
     smallTextBoxes[x + 20][0] = rightSideSmallText[x]

# large text box loading:
for x in range(len(leftSidelargeText)):
     largeTextBoxes[x][0] = leftSidelargeText[x]

for x in range(len(rightSidelargeText)):
     largeTextBoxes[x + 20][0] = rightSidelargeText[x]


#=============================================================#

while True:
    screen.fill((0,195,0)) # fill screen with GREEN
    screen.fill((195,0,0), (0, 0, screen.get_width() / 2, screen.get_height())) # fill right side of screen with RED
    screen.fill((115,115,115), (0, 720, screen.get_width(), screen.get_height()/10)) # fill Bottom bar for Functions with GRAY
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit(), sys.exit()

        # check for mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            clickFound = False #stops checking stuff if we've found what the mouse clicked
            for x in checkBoxes:
                if x[1].collidepoint(pygame.mouse.get_pos()):
                    clickFound = True
                    if x[0]:
                        x[0] = False
                        break
                    else:
                        x[0] = True
                        break
            if not clickFound:
                 for x in smallTextBoxes:
                    if x[1].collidepoint(pygame.mouse.get_pos()):
                        clickFound = True
                        selected = [x, "smallTextBox"]
                        break
            if not clickFound:
                 for x in largeTextBoxes:
                    if x[1].collidepoint(pygame.mouse.get_pos()):
                        clickFound = True
                        selected = [x, "largeTextBox"]
                        break
        if event.type == pygame.KEYDOWN and selected[0] != NULL:
            if event.key == pygame.K_RETURN:
                selected[0] = NULL
            elif event.key == pygame.K_BACKSPACE:
                selected[0][0] = selected[0][0][:-1]
            else:
                if selected[1] == "smallTextBox":
                    if len(selected[0][0]) < 9:
                        selected[0][0] += event.unicode
                elif selected[1] == "largeTextBox":
                    if len(selected[0][0]) < 18:
                        selected[0][0] += event.unicode




    # Team texts
    # add EDIT CURRENT GAME text
    text = font.render("Edit Current Game", 1, (5,5,5)) # Black text color
    screen.blit(text, (320, 5)) # position text on screen

    # add RED TEAM text
    text = font.render("Red Team", 1, (5,225,255)) # Cyan text color
    screen.blit(text, (150, 25))

    # add GREEN TEAM text
    text = font.render("Green Team", 1, (5,225,255))
    screen.blit(text, (550, 25))

    # draws boxes
    for x in range(20):
        
        # check boxes
        # left boxes
        if checkBoxes[x][1].collidepoint(pygame.mouse.get_pos()): #checks if mouse hovering over
            pygame.draw.rect(screen, (55,55,55), checkBoxes[x][1], 3)
        else:
            pygame.draw.rect(screen, (5,5,5), checkBoxes[x][1], 3)
        # right boxes
        if checkBoxes[x + 20][1].collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (55,55,55), checkBoxes[x + 20][1], 3)
        else:
            pygame.draw.rect(screen, (5,5,5), checkBoxes[x + 20][1], 3)

        # checks
        # left checks
        if(checkBoxes[x][0] == True):
            screen.blit(checkMark, (16, x * 33 + 45))
        # right checks
        if(checkBoxes[x + 20][0] == True):
            screen.blit(checkMark, (416, x * 33 + 45))
        
        # small text boxes
        screen.fill((255,255,255), smallTextBoxes[x][1])
        text = font.render(smallTextBoxes[x][0], 1, (5,5,5))
        screen.blit(text, text.get_rect(center=(smallTextBoxes[x][1].center)))

        screen.fill((255,255,255), smallTextBoxes[x + 20][1])
        text = font.render(smallTextBoxes[x + 20][0], 1, (5,5,5))
        screen.blit(text, text.get_rect(center=(smallTextBoxes[x + 20][1].center)))

    
        # large text boxes
        screen.fill((255,255,255), largeTextBoxes[x][1])
        text = font.render(largeTextBoxes[x][0], 1, (5,5,5))
        screen.blit(text, text.get_rect(center=(largeTextBoxes[x][1].center)))

        screen.fill((255,255,255), largeTextBoxes[x + 20][1])
        text = font.render(largeTextBoxes[x + 20][0], 1, (5,5,5))
        screen.blit(text, text.get_rect(center=(largeTextBoxes[x + 20][1].center)))

    pygame.display.flip() # keep at end of while loop
