import pgzrun
from random import randint

WIDTH=600
HEIGHT=500

score=0

game_over=False

bee=Actor("bee")
flr=Actor("flower")

bee.pos=100,100
flr.pos=200,200

def draw():
    screen.blit("bg",(0,0))
    flr.draw()
    bee.draw()
    screen.draw.text("score "+str(score),color="black",topleft=(10,10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("TIMES UP!!! your final score is: "+str(score),color="red",midtop=(400,10))
        
def place_flower():
    flr.x=randint(70,(WIDTH,-70))
    flr.y=randint(70,(HEIGHT,-70))

def time_up():
    global game_over
    game_over=True



def update():
    global score
    if keyboard.left:
        bee.x=bee.x-2

    if keyboard.right:
        bee.x=bee.x+2

    if keyboard.up:
        bee.y=bee.y-2

    if keyboard.down:
        bee.y=bee.y+2    

    fc=bee.colliderect(flr)
    if fc:
        score=score+10
        place_flower()


clock.schedule(time_up,10.0)
pgzrun.go()
