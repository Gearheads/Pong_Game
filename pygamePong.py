import sys, pygame
from pygame.locals import *

pygame.init()

def Game_Loop():
    pygame.key.set_repeat(50, 50)               #allows user to hold down movement key
    white = (255, 255, 255)                     #color white
    win = 3                                     #number of points to win
    ballspeed = 200                             #option to increase ball speed
    scoreboard1 = []                            #player 1 score
    score1 = 0                                  #counter for player 1
    sb1Pos = (260, 40)                          #scoreboard1 position
    scoreboard2 = []                            #player 2 score
    score2 = 0                                  #counter for player 2
    sb2Pos = (330, 40)                          #scoreboard2 position
    screen = pygame.display.set_mode((640,480)) #creates the screen
    pygame.display.set_caption('Pong')          #adds the title
    game_over = pygame.image.load('game_over.jpg').convert()    #uploads game_over image
    background = pygame.image.load('background.jpg').convert()  #uploads background image
    screen.blit(background, (0, 0))                             #draws the background
    zero = pygame.image.load('zero.jpg').convert()              #uploads zero image
    one = pygame.image.load('one.jpg').convert()                #uploads one image
    two = pygame.image.load('two.jpg').convert()                #uploads two image
    three = pygame.image.load('three.jpg').convert()            #uploads three image
    scoreboard1.append(zero)                    #adds image to player 1 scoreboard
    scoreboard1.append(one)                     #adds...
    scoreboard1.append(two)                     #adds...
    scoreboard1.append(three)                   #adds...
    scoreboard2 = list(scoreboard1)             #copies scoreboard1
    screen.blit(scoreboard1[0], sb1Pos)         #position of player 1 score
    screen.blit(scoreboard2[0], sb2Pos)         #position of player 2 score
    ball = pygame.Rect(310, 220, 20, 20)        #creates the ball
    screen.fill(white, ball)                    #makes the ball white
    ballDirection = ['right', 'down']           #direction of the ball
    player1 = pygame.Rect(10, 200, 20, 85)      #creates player 1
    screen.fill(white, player1)                 #makes player 1 white
    player2 = pygame.Rect(610, 200, 20, 85)     #creates player 2
    screen.fill(white, player2)                 #makes player 2 white
    pygame.display.update()                     #shows it all
    clock = pygame.time.Clock()
    
    while 1:
        clock.tick(ballspeed)                         #slows down the game
        if score1 == win or score2 == win:
            screen.blit(game_over, (190, 200))
            pygame.display.update()
            break
        elif ball.left > 640 and score1 < win:  #player 1 scores
            ball.left = 310
            ball.top = 220
            score1 += 1
            ballspeed = 200
        elif ball.left < 0 and score2 < win:    #player 2 scores
            ball.left = 310
            ball.top = 220
            score2 += 1
            ballspeed = 200
        elif ball.colliderect(player2) and ballDirection[1] == 'up':
            ballDirection[0] = 'left'
            ball.left -= 1
            ball.top -= 1
            ballspeed += 5
        elif ball.colliderect(player2) and ballDirection[1] == 'down':
            ballDirection[0] = 'left'
            ball.left -= 1
            ball.top += 1
            ballspeed += 5
        elif ball.colliderect(player1) and ballDirection[1] == 'up':
            ballDirection[0] = 'right'
            ball.left += 1
            ball.top -= 1
            ballspeed += 5
        elif ball.colliderect(player1) and ballDirection[1] == 'down':
            ballDirection[0] = 'right'
            ball.left += 1
            ball.top += 1
            ballspeed += 5
        elif ballDirection[0] == 'right' and ballDirection[1] == 'down' and ball.top < 440:
            ball.left += 1
            ball.top += 1
        elif ballDirection[0] == 'right' and ballDirection[1] == 'down' and ball.top >= 440:
            ballDirection[1] = 'up'
        elif ballDirection[0] == 'left' and ballDirection[1] == 'down' and ball.top < 440:
            ball.left -= 1
            ball.top += 1
        elif ballDirection[0] == 'left' and ballDirection[1] == 'down' and ball.top >= 440:
            ballDirection[1] = 'up'
        elif ballDirection[0] == 'right' and ballDirection[1] == 'up' and ball.top > 35:
            ball.left += 1
            ball.top -= 1
        elif ballDirection[0] == 'right' and ballDirection[1] == 'up' and ball.top <= 35:
            ballDirection[1] = 'down'
        elif ballDirection[0] == 'left' and ballDirection[1] == 'up' and ball.top > 35:
            ball.left -= 1
            ball.top -= 1
        elif ballDirection[0] == 'left' and ballDirection[1] == 'up' and ball.top <= 35:
            ballDirection[1] = 'down'
        
        for event in pygame.event.get():  #gets events that happen
            if event.type==QUIT:          #if user clicks close on window
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN:     #if user presses a key
                if event.key==K_DOWN and player2.top < 360: #if key is down arrow
                    player2.top += 20
                elif event.key==K_UP and player2.top > 40:  #if key is up arrow
                    player2.top -= 20
                elif event.key==K_w and player1.top > 40:   #if key is w, move up
                    player1.top -=20
                elif event.key==K_s and player1.top < 360:  #if key is s, move down
                    player1.top += 20
                screen.blit(background, (0,0))              #remake background
                screen.fill(white, player1)                 #remake player 1
                screen.fill(white, player2)                 #remake player 2
                screen.fill(white, ball)                    #remake ball
                screen.blit(scoreboard1[score1], sb1Pos)    #position of player 1 score
                screen.blit(scoreboard2[score2], sb2Pos)    #position of player 2 score
                pygame.display.update()                     #updates screen

        screen.blit(background, (0,0))              #remake background
        screen.fill(white, player1)                 #remake player 1
        screen.fill(white, player2)                 #remake player 2
        screen.fill(white, ball)                    #remake ball
        screen.blit(scoreboard1[score1], sb1Pos)    #position of player 1 score
        screen.blit(scoreboard2[score2], sb2Pos)    #position of player 2 score
        pygame.display.update()                     #updates screen
        
while 1:
    play_again = 0
    Game_Loop()
    while 1:
        for event in pygame.event.get():  #gets events that happen
            if event.type==QUIT:          #if user clicks close on window
                pygame.quit()
                sys.exit()
            elif event.type==KEYDOWN:
                if event.key==K_SPACE:
                    play_again = 1
        if play_again == 1:
            break
