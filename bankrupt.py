import pygame, pyautogui,sys
pygame.init()

name='Bankrupt'

while True:
    
    start=pyautogui.confirm(title=name,text=f'Welcome to {name}, the game where you lose all of your money!',buttons=['START','QUIT'])
    if start=='START':
        break
    elif start=='QUIT':
        sys.exit()

mode=pyautogui.confirm(title=name,text='Pick game mode',buttons=['EASY','MEDIUM','INSANE'])
if mode=='EASY':
    modifier=3.5
elif mode=='MEDIUM':
    modifier=3
else:
    modifier=2.5


width=800
height=600
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption(name)

back=pygame.image.load('money.png')
back=pygame.transform.scale(back,(width,height))
backrect=back.get_rect()

barHeight=60
font=pygame.font.SysFont('comic sans',32)
time=0
money=100
level = 1

text=font.render(f'${money}k',True,(0,0,0))
textrect=text.get_rect()
textrect.center=(0,0)

levtext=font.render(str(level),True,(0,0,0))
levtextrect=levtext.get_rect()
levtextrect.right=width

money_minus = 10
money_plus = 1
money_often=50

while True:
        
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            money-=money_minus
            
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RALT:
                money=0
            

    time+=1
    if time%money_often==0:
        money+=money_plus
        text=font.render(f'${money}k',True,(0,0,0))
        textrect=text.get_rect()

    screen.blit(back,backrect)
    pygame.draw.rect(screen,(100,100,100),(0,0,width,barHeight))
    screen.blit(levtext,levtextrect)
    screen.blit(text,textrect)
    
    pygame.display.update()
    
    if money<=0:
        level += 1
        pygame.display.update()
        pyautogui.alert(text='Good Job',button='Next Level!')
        money=10**level
        money_plus+=5
        money_minus+=int(level**modifier)
        
        levtext=font.render(str(level),True,(0,0,0))
        levtextrect=levtext.get_rect()
        levtextrect.right=width
    
    