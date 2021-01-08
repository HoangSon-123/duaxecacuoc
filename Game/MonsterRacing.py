import pygame
from pygame.locals import *
import sys, random
import Eracing, minigame, Head, user, dulieu
from winsound import *

Head.init()
pygame.init()


screen_width = 1000
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('MONSTER RACING')
BG_menu = pygame.transform.scale(pygame.image.load('Menu/BG.jpg'),(screen_width, screen_height))
BG_option = pygame.transform.scale(pygame.image.load('Option/BG.jpg'),(screen_width, screen_height))
font = pygame.font.SysFont('Consolas', 30)

#define global variable
character = 0
length = 0 
#bua img

#define button game
start = Head.button(430, 500, 'START')
play = Head.button(100, 300, 'PLAY')
store = Head.button(420, 300, 'STORE')
setting = Head.button(720, 300, 'SETTING')
exit = Head.button(720, 450, 'EXIT')
mini = Head.button(100, 450,'mini game')
history = Head.button(420, 450, 'HISTORY')
back = Head.button(1,1, 'BACK')
set1 = Head.button(20, 500, 'Set 1')
set2 = Head.button(210, 500, 'Set 2')
set3 = Head.button(410, 500, 'Set 3')
set4 = Head.button(610, 500, 'Set 4')
set5 = Head.button(820, 500, 'Set 5')
short_length = Head.button(120, 250, 'Short')
medium_length = Head.button(420, 250, 'Medium')
long_length = Head.button(720, 250, 'Long')
purchase = Head.button(450, 250, '50 $') 

def RunOption2(): #Hàm chọn độ dài đường đua 
    length = 0
    option2 = True
    comment = font.render('SELECT THE RACETRACK LENGTH', 1, (3, 252, 244))
    while option2:      
        screen.blit(BG_option, (0,0))
        screen.blit(comment, (290, 400))
        if back.draw_button():
            pygame.mixer.music.load('sound/button.mp3')
            pygame.mixer.music.play(1)
            option2 = False
            RunMenu()
        if short_length.draw_button():
            pygame.mixer.music.load('sound/button.mp3')
            pygame.mixer.music.play(1)
            length = 1
            option2 = False
        if medium_length.draw_button():
            pygame.mixer.music.load('sound/button.mp3')
            pygame.mixer.music.play(1)
            length = 2
            option2 = False
        if long_length.draw_button():
            pygame.mixer.music.load('sound/button.mp3')
            pygame.mixer.music.play(1)
            length = 3
            option2 = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
    return length

def RunOption1(): #Hàm chọn set nhân vật
    character = 0
    option1 = True
    while option1:
        screen.blit(pygame.image.load('Option/BG1.jpg'),(0,0))
        if back.draw_button():
            pygame.mixer.music.load('sound/button.mp3')
            pygame.mixer.music.play(1)
            option1 = False
            RunMenu()        
        if set1.draw_button():
            pygame.mixer.music.load('sound/button.mp3')
            pygame.mixer.music.play(1)
            character = 1
            option1 = False
        elif set2.draw_button():
            pygame.mixer.music.load('sound/button.mp3')
            pygame.mixer.music.play(1)
            character = 2
            option1 = False
        elif set3.draw_button():
            pygame.mixer.music.load('sound/button.mp3')
            pygame.mixer.music.play(1)
            character = 3
            option1 = False
        elif set4.draw_button():
            pygame.mixer.music.load('sound/button.mp3')
            pygame.mixer.music.play(1)
            character = 4
            option1 = False
        elif set5.draw_button():
            pygame.mixer.music.load('sound/button.mp3')
            pygame.mixer.music.play(1)
            character = 5
            option1 = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()
    return character

def Store(): # Hàm vẽ store lên màn hình
    anh=['Spell/TangToc.png','Spell/LamCham.png','Spell/DungYen.png','Spell/LuiVeSau.png','Spell/VeNha.png','Spell/VeDich.png','Spell/TocBien.png']
    tangtoc =0
    lamcham=0
    dungyen=0
    luivesau=0
    venha=0
    vedich=0
    tocbien=0
    Run = True
    while Run:
        screen.blit(pygame.image.load('Store/BG.png'),(0,0))
        screen.blit(pygame.image.load('Store/purchase.png'), (400, 80))
        if back.draw_button():
            pygame.mixer.music.load('sound/button.mp3')
            pygame.mixer.music.play(1)
            Run = False
        if purchase.draw_button():
            pygame.mixer.music.load('sound/button.mp3')
            pygame.mixer.music.play(1)
            k=random.choice(anh)
            if Head.money > 0:
                Head.update(-50)
                if k=='Spell/TangToc.png':
                    tangtoc += 1
                if k=='Spell/LamCham.png':
                    lamcham += 1
                if k=='Spell/DungYen.png':
                    dungyen += 1
                if k=='Spell/LuiVeSau.png':
                    luivesau += 1
                if k=='Spell/VeNha.png':
                    venha += 1
                if k=='Spell/VeDich.png':
                    vedich += 1
                if k == 'Spell/TocBien.png':
                    tocbien += 1

        MoneySuface = font.render(str(int(Head.money)), True, (0, 0, 0))
        screen.blit(MoneySuface, (810, 20))
        tangtoc_label = font.render(f"{tangtoc}",1,(211,49,21))
        screen.blit(tangtoc_label,(60,530))
        lamcham_label = font.render(f"{lamcham}",1,(211,49,21))
        screen.blit(lamcham_label,(200,530))
        dungyen_label = font.render(f"{dungyen}",1,(211,49,21))
        screen.blit(dungyen_label,(340,530))
        luivesau_label = font.render(f"{luivesau}",1,(211,49,21))
        screen.blit(luivesau_label,(490,530))
        venha_label = font.render(f"{venha}", 1, (211,49,21))
        screen.blit(venha_label, (630, 530))
        vedich_label = font.render(f"{vedich}", 1, (211,49,21))
        screen.blit(vedich_label, (780, 530))
        tocbien_label = font.render(f"{tocbien}", 1, (211,49,21))
        screen.blit(tocbien_label, (920, 530))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()	
        pygame.display.update()

def Run_History():
    press = True
    his = dulieu.doc()
    comment = font.render(his, 1, (0, 0, 0))
    while press:
        screen.blit(pygame.image.load('Menu/mini.jpg'),(0,0))
        screen.blit(comment, (100,100))
        if back.draw_button():
            pygame.mixer.music.load('sound/button.mp3')
            pygame.mixer.music.play(1)
            press = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()	
        pygame.display.update()
def Run_setting():
    press = True
    
    while press:
        screen.blit(pygame.image.load('Option/ảnh 5.png'),(0,0))
        
        if back.draw_button():
            pygame.mixer.music.load('sound/button.mp3')
            pygame.mixer.music.play(1)
            press = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  
        pygame.display.update()

def StartGame():#Hàm hiện lên màn hình đầu trò chơi
    unbegin = True
    while unbegin:
        screen.blit(pygame.image.load('Login/BG.jpg'), (0,0))
        if start.draw_button():
            pygame.mixer.music.load('sound/button.mp3')
            pygame.mixer.music.play(1)
            unbegin = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()	

money_win = 0
def RunMenu(): #hàm chạy menu game
    pygame.mixer.music.load('sound/background.mp3')
    pygame.mixer.music.play(-1,0,0)
    global money_win
    run = True
    while run:    
        screen.blit(BG_menu,(0,0))
        if play.draw_button():
            pygame.mixer.music.load('sound/button.mp3')
            pygame.mixer.music.play(1)
            a = RunOption1()
            b = RunOption2()
            Eracing.Run(a, b)	
        
        if store.draw_button():
            pygame.mixer.music.load('sound/button.mp3')
            pygame.mixer.music.play(1)
            Store()
            
        if history.draw_button():
            pygame.mixer.music.load('sound/button.mp3')
            pygame.mixer.music.play(1)
            Run_History()

        if setting.draw_button():
            pygame.mixer.music.load('sound/button.mp3')
            pygame.mixer.music.play(1)
            
            Run_setting()

        
        if mini.draw_button():
            pygame.mixer.music.load('sound/button.mp3')
            pygame.mixer.music.play(1)
            screen.blit(pygame.image.load('Menu/mini.jpg'),(0,0))
            score = minigame.run()
            if score >= 0 and score <= 10:
                RunMenu()
            else:
                money_win = score * 10 - 10
                Head.update(money_win)
                RunMenu()
        MoneySuface = font.render(str(int(Head.money)), True, (0,0,0))
        screen.blit(MoneySuface, (820, 20))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                file_obj = open(username + '.txt', mode = 'w')
                file_obj.write(password + '\n')
                file_obj.write(str(int(Head.money)))
                file_obj.close()
                sys.exit()	
        if exit.draw_button():
            file_obj = open(username + '.txt', mode = 'w')
            file_obj.write(password + '\n')
            file_obj.write(str(int(Head.money)))
            file_obj.close()
            sys.exit()

        pygame.display.update()
        #pygame.quit()

def Run(): #Hàm chạy game
    global username, password
    StartGame()
    username = user.Input_Username()
    USER=str(username)
    f=open('lichsu.txt','a+')
    f.write(USER +' ')
    f.close()
    password = user.Input_Password(username)
    RunMenu()

Run()

if __name__ == "__main__":
    Run()