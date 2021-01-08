import pygame, random, time, sys
from pygame.locals import *
from random import choice
import Head
import dulieu
import minigame

clicked = False
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
vedich=0
WINDOWWIDTH = 1000
WINDOWHEIGHT = 600
happy = pygame.image.load('Spell/happy.png')
# dùng để xác định thắng thua
#hàm chỉnh đường đua
canh = pygame.image.load('Spell/canh.png')
# COLOR
#tiền trong game

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GREY = (113, 142, 150)

pygame.init()
pygame.mixer.init()
Head.init()

FPS = 60
fpsClock = pygame.time.Clock()

# BACKGROUND
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Racing')

font = pygame.font.SysFont('Consolas', 30)
text_Surface = font.render('START RACING', True, RED, BLACK)

Surface2=pygame.Surface((500,300))
#win11 = pygame.image.load('Set/1.1/win/1.png')
#win12 = 
# HÀM
check = [0]
flag = [False,False,False,False,False]
result = [0,0,0,0,0]

def checkwin(i):
	if (check[0] == 0) and (flag[i] == False):
		check[0] = 1
		result[i] = 1
		flag[i] = True
	if (check[0] == 1) and (flag[i] == False):
		check[0] = 2
		result[i] = 2
		flag[i] = True
	if (check[0] == 2) and (flag[i] == False):
		check[0] = 3
		result[i] = 3
		flag[i] = True
	if (check[0] == 3) and (flag[i] == False):
		check[0] = 4
		result[i] = 4
		flag[i] = True
	if (check[0] == 4) and (flag[i] == False):
		result[i] = 5
		flag[i] = True


def DISPLAY(set):
	global car_x1, car_x1w, car_x2, car_x2w, car_x3, car_x3w, car_x4, car_x4w, car_x5, car_x5w
	screen.blit(set[0], (car_x1, car_x1w))
	screen.blit(set[1], (car_x2, car_x2w))
	screen.blit(set[2], (car_x3, car_x3w))
	screen.blit(set[3], (car_x4, car_x4w))
	screen.blit(set[4], (car_x5, car_x5w))

def RESULT(result,i):
	if result==1:
		screen.blit(i, (20, 110))
	if result==2:
		screen.blit(i, (140, 170))
	if result == 3:
		screen.blit(i, (250, 250))
	if result==4:
		screen.blit(i, (370, 320))
	if result==5:
		screen.blit(i, (490, 400))
	

def RATING(YourChoose, Your_betting): # Hàm xếp hạng kêt qua cuộc đua
	global score_bet
	RESULT(result[0],car1)
	RESULT(result[1],car2)
	RESULT(result[2],car3)
	RESULT(result[3],car4)
	RESULT(result[4],car5)
	if result[YourChoose - 1] == 1:
		screen.blit(pygame.image.load('Reward/win.png'), (300, 0))
		Head.update(Your_betting)
		score_bet=1
	else:
		screen.blit(pygame.image.load('Reward/lose.png'), (300, 0))
		Your_betting = -Your_betting
		Head.update(Your_betting)
		score_bet=2

bua1 = pygame.image.load('Spell/TangToc.png')
bua2 = pygame.image.load('Spell/LamCham.png')
bua3 = pygame.image.load('Spell/DungYen.png')
bua4 = pygame.image.load('Spell/LuiVeSau.png')
bua5 = pygame.image.load('Spell/VeNha.png')
bua6 = pygame.image.load('Spell/VeDich.png')
bua7 = pygame.image.load('Spell/Tocbien.png')
# day là hàm vẽ ra 4 bùa lợi
def Randomi():
	return random.choice([-2,-1,0,1,2,3])
vitri1=Randomi()
vitri2=Randomi()
vitri3=Randomi()
vitri4=Randomi()
vitri5=Randomi()
def Spell(k, i,vitri):
	y=360+70*i
	x=500+vitri*50-100*vedich
	#DISPLAYSURF.blit(pygame.image.load(k), (x,y))
	return x
def Random():
	return random.choice(['Spell/TangToc.png','Spell/LamCham.png','Spell/DungYen.png','Spell/LuiVeSau.png','Spell/VeNha.png','Spell/VeDich.png'])

Set1 = Head.button(800, 100, 'Play')
Set2 = Head.button(800, 200, 'Play')
Set3 = Head.button(800, 300, 'Play')
Set4 = Head.button(800, 400, 'Play')
Set5 = Head.button(800, 500, 'Play')
BG_choose = pygame.image.load('Option/BG.jpg')
Money_option1 = Head.button(120, 250, '100 $')
Money_option2 = Head.button(420, 250, '200 $')
Money_option3 = Head.button(720, 250, '400 $')

def ChooseYour(car1, car2, car3, car4, car5):# Hàm chọn nhân vật mà mình cá cược
	YourSet = 0
	comment = font.render('CHOOSE YOUR CHARACTER', 1, (0, 0, 0))
	while YourSet == 0:
		screen.blit(BG_choose, (0,0))
		screen.blit(comment, (100, 300))
		screen.blit(car1, (680, 100))
		screen.blit(car2, (680, 200))
		screen.blit(car3, (680, 300))
		screen.blit(car4, (680, 400))
		screen.blit(car5, (680, 500))

		if Set1.draw_button():
			pygame.mixer.music.load('sound/button.mp3')
			pygame.mixer.music.play(1)
			YourSet = 1
		elif Set2.draw_button():
			pygame.mixer.music.load('sound/button.mp3')
			pygame.mixer.music.play(1)
			YourSet = 2
		elif Set3.draw_button():
			pygame.mixer.music.load('sound/button.mp3')
			pygame.mixer.music.play(1)
			YourSet = 3
		elif Set4.draw_button():
			pygame.mixer.music.load('sound/button.mp3')
			pygame.mixer.music.play(1)
			YourSet = 4
		elif Set5.draw_button():
			pygame.mixer.music.load('sound/button.mp3')
			pygame.mixer.music.play(1)
			YourSet = 5
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
		pygame.display.update()
	return YourSet

def ChooseMoney(): # Hàm chọn số tiền cá cược
	betting = 0
	comment = font.render('CHOOSE AMOUNT OF YOUR BET', 1, (3, 252, 244))
	back = Head.button(1,1, 'BACK')
	while betting == 0:
		screen.blit(BG_choose, (0,0))
		screen.blit(comment, (290, 400))
		if Money_option1.draw_button():
			if Head.money >=100:
				pygame.mixer.music.load('sound/button.mp3')
				pygame.mixer.music.play(1)
				betting = 100
		elif Money_option2.draw_button():
			if Head.money >=200:		
				pygame.mixer.music.load('sound/button.mp3')
				pygame.mixer.music.play(1)
				betting = 200
		elif Money_option3.draw_button():
			if Head.money >= 400:
				pygame.mixer.music.load('sound/button.mp3')
				pygame.mixer.music.play(1)
				betting = 400
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()


		pygame.display.update()
	return betting

choose_effect = pygame.image.load('set/choose.png')

def BeginGame(YourChoose, length, car1, car2, car3, car4, car5, background_surf):# Hàm bắt đầu cuộc đua
	begin = True
	comment = font.render('Press "space" to play', True, (255, 255, 255))
	while begin:
		screen.blit(background_surf, (0, 0))
		screen.blit(car1, (10, 130))
		screen.blit(car2, (10, 200))
		screen.blit(car3, (10, 270))
		screen.blit(car4, (10, 340))
		screen.blit(car5, (10, 410))

		if YourChoose == 1:
			screen.blit(choose_effect, (80, 140))
		elif YourChoose == 2:
			screen.blit(choose_effect, (80, 210))
		elif YourChoose == 3:
			screen.blit(choose_effect, (80, 280))
		elif YourChoose == 4:
			screen.blit(choose_effect, (80, 350))
		elif YourChoose == 5:
			screen.blit(choose_effect, (80, 420))
		screen.blit(comment, (300, 300))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYUP:
				if event.key == K_SPACE:
					begin = False
		pygame.display.update()

def Run(character, length): #Hàm chạy cuộc đua
	
	car_x6=10
	global car_x1, car_x1w, car_x2, car_x2w, car_x3, car_x3w, car_x4, car_x4w, car_x5, car_x5w, car1, car2, car3, car4, car5
	if character == 1:
		car1 = pygame.image.load('set/1.1/move/1.png')
		car_x1 = 10
		car_x1w = 130
		car2 = pygame.image.load('set/1.2/move/1.png')
		car_x2 = 10
		car_x2w = 200
		car3 = pygame.image.load('set/1.3/move/1.png')
		car_x3 = 10
		car_x3w = 270
		car4 = pygame.image.load('set/1.4/move/1.png')
		car_x4 = 10
		car_x4w = 340
		car5 = pygame.image.load('set/1.5/move/1.png')
		car_x5 = 10
		car_x5w = 410
	elif character == 2:
		car1 = pygame.image.load('set/2.1/move/1.png')
		car_x1 = 10
		car_x1w = 140
		car2 = pygame.image.load('set/2.2/move/1.png')
		car_x2 = 10
		car_x2w = 210
		car3 = pygame.image.load('set/2.3/move/1.png')
		car_x3 = 10
		car_x3w = 280
		car4 = pygame.image.load('set/2.4/move/1.png')
		car_x4 = 10
		car_x4w = 350
		car5 = pygame.image.load('set/2.5/move/1.png')
		car_x5 = 10
		car_x5w = 420
	elif character == 3:
		car1 = pygame.image.load('set/3.1/move/1.png')
		car_x1 = 10
		car_x1w = 140
		car2 = pygame.image.load('set/3.2/move/1.png')
		car_x2 = 10
		car_x2w = 210
		car3 = pygame.image.load('set/3.3/move/1.png')
		car_x3 = 10
		car_x3w = 280
		car4 = pygame.image.load('set/3.4/move/1.png')
		car_x4 = 10
		car_x4w = 350
		car5 = pygame.image.load('set/3.5/move/1.png')
		car_x5 = 10
		car_x5w = 420
	elif character == 4:
		car1 = pygame.image.load('set/4.1/move/1.png')
		car_x1 = 10
		car_x1w = 140
		car2 = pygame.image.load('set/4.2/move/1.png')
		car_x2 = 10
		car_x2w = 210
		car3 = pygame.image.load('set/4.3/move/1.png')
		car_x3 = 10
		car_x3w = 280
		car4 = pygame.image.load('set/4.4/move/1.png')
		car_x4 = 10
		car_x4w = 350
		car5 = pygame.image.load('set/4.5/move/1.png')
		car_x5 = 10
		car_x5w = 420
	elif character == 5:
		car1 = pygame.image.load('set/5.1/move/1.png')
		car_x1 = 10
		car_x1w = 150
		car2 = pygame.image.load('set/5.2/move/1.png')
		car_x2 = 10
		car_x2w = 220
		car3 = pygame.image.load('set/5.3/move/1.png')
		car_x3 = 10
		car_x3w = 290
		car4 = pygame.image.load('set/5.4/move/1.png')
		car_x4 = 10
		car_x4w = 360
		car5 = pygame.image.load('set/5.5/move/1.png')
		car_x5 = 10
		car_x5w = 430

	if length == 1:
		background_surf = pygame.image.load('background/short.png')
		WIN=1000-(length)*100
	elif length == 2:
		background_surf = pygame.image.load('background/medium.png')
		WIN=1000
	elif length == 3:
		background_surf = pygame.image.load('background/long.png')
		WIN=1010
	
	speed = 2

	k1=Random()
	k2=Random()
	k3=Random()
	k4=Random()
	k5=Random()
	Spell(k1,0,vitri1)
	y1=Spell(k1,0,vitri1)
	Spell(k2,1,vitri2)
	y2=Spell(k2,1,vitri2)
	Spell(k3,2,vitri3)
	y3=Spell(k3,2,vitri3)
	Spell(k4,3,vitri4)
	y4=Spell(k4,3,vitri4)
	Spell(k5,4,vitri5)
	y5=Spell(k5,4,vitri5)
	venha1=venha2=venha3=venha4=venha5=0  
	Your_betting = ChooseMoney()
	Your_character = ChooseYour(car1, car2, car3, car4, car5)
	BeginGame(Your_character, length, car1, car2, car3, car4, car5, background_surf)
	setcar = [car1, car2, car3, car4, car5]
	pygame.mixer.music.load('sound/run.mp3')
	pygame.mixer.music.play(-1,0,0)
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			
		screen.blit(text_Surface, (400, 20))

		screen.blit(background_surf, (0, 0))

		DISPLAY(setcar)
		car_x6+=1

		car_x1 += random.choice([1,2])
		#đây là dòng lệnh để vẽ và hiệu ứng xe 1
		if car_x1>=Spell(k1,0,vitri1) and k1=='Spell/TangToc.png':
			car_x1+=0.2
			screen.blit(bua1, (car_x1+30,car_x1w))
		elif car_x1>=Spell(k1,0,vitri1) and k1=='Spell/LamCham.png':
			car_x1+=-0.2
			screen.blit(bua2, (car_x1+30,car_x1w))
		elif car_x1>=Spell(k1,0,vitri1) and car_x6<=Spell(k1,0,vitri1)+20 and k1=='Spell/DungYen.png':
			car_x1=Spell(k1,0,vitri1)  
			screen.blit(bua3, (car_x1+30,car_x1w))        
		elif car_x1>=Spell(k1,0,vitri1) and y1==Spell(k1,0,vitri1) and k1=='Spell/LuiVeSau.png':
			screen.blit(bua4, (car_x1+30,car_x1w))  
			if car_x1 > Spell(k1,0,vitri1) + 20:
				car_x1=Spell(k1,0,vitri1)-50
				y1=Spell(k1,0,vitri1)+1		
		elif car_x1>=Spell(k1,0,vitri1) and k1=='Spell/VeNha.png' and venha1==0 :
			screen.blit(bua5, (car_x1+30,car_x1w))
			if car_x1 > Spell(k1,0,vitri1) + 20:
				car_x1=10
				venha1=1
		elif car_x1>=Spell(k1,0,vitri1) and k1=='Spell/VeDich.png':
			screen.blit(bua6, (car_x1+30,car_x1w))
			if car_x1 > Spell(k1,0,vitri1) + 20:
				car_x1=WINDOWHEIGHT+1000
		if car_x1 + 100 > WIN:
			car_x1 = WIN - 100
			checkwin(0)
		if result[0] == 1:
			screen.blit(canh, (car_x1- 55, car_x1w - 20))
			car_x1w -= speed
			if car_x1w < 80:
				speed *= -1
			if car_x1w > 150:
				speed *= -1
			if car_x1w < 130:
				screen.blit(happy, (car_x1+20, car_x1w +20))
			
				#speed *= -1
			#if car_x1w > 130:
				#car_x1w = 130
				#
				
				#if car_x1w > 150:
					#car_x1w = 150
					#car_x1w -= 2
					#if car_x1w < 80:
						#car_x1w = 80
						#car_x1w += 2
						#if car_x1w > 130:
							#car_x1w = 130


			
			
			


		car_x2 += random.choice([1,2])
		#đây là dòng lệnh để vẽ và hiệu ứng xe 2
		if car_x2>=Spell(k2,1,vitri2) and k2=='Spell/TangToc.png':
			car_x2+=0.2
			screen.blit(bua1, (car_x2+30,car_x2w))
		elif car_x2>=Spell(k2,1,vitri2) and k2=='Spell/LamCham.png':
			car_x2+=-0.2
			screen.blit(bua2, (car_x2+30,car_x2w))
		elif car_x2>=Spell(k2,1,vitri2) and car_x6<=Spell(k2,1,vitri2)+20 and k2=='Spell/DungYen.png':
			car_x2=Spell(k2,1,vitri2)   
			screen.blit(bua3, (car_x2+30,car_x2w))       
		elif car_x2>=Spell(k2,1,vitri2) and y2==Spell(k2,1,vitri2) and k2=='Spell/LuiVeSau.png':
			screen.blit(bua4, (car_x2+30,car_x2w))
			if car_x2 > Spell(k2,1,vitri2) + 20:
				car_x2=Spell(k2,1,vitri2)-50
				y2=Spell(k2,1,vitri2)+1
			
		elif car_x2>=Spell(k2,1,vitri2) and k2=='Spell/VeNha.png' and venha2==0:
			screen.blit(bua5, (car_x2+30,car_x2w))
			if car_x2> Spell(k2,1,vitri2) + 20:
				car_x2 = 10
				venha2=1
			
		elif car_x2>=Spell(k2,1,vitri2) and k2=='Spell/VeDich.png':
			screen.blit(bua6, (car_x2+30,car_x2w))
			if car_x2 > Spell(k2,1,vitri2) +20:
				car_x2=WINDOWHEIGHT+1000
			
		if car_x2 + 100 > WIN:
			car_x2 = WIN - 100
			checkwin(1)
		if result[1] == 1:
			screen.blit(canh, (car_x2- 55, car_x2w - 20))
			car_x2w -= speed
			if car_x2w < 150:
				speed *= -1
			if car_x2w > 220:
				speed *= -1
			if car_x2w < 200:
				screen.blit(happy, (car_x2+20, car_x2w +20))
			

		car_x3 += random.choice([1,2])
		#đây là dòng lệnh để vẽ và hiệu ứng xe 3
		if car_x3>=Spell(k3,2,vitri3) and k3=='Spell/TangToc.png':
			car_x3+=0.2
			screen.blit(bua1, (car_x3+30,car_x3w))
		elif car_x3>=Spell(k3,2,vitri3) and k3=='Spell/LamCham.png':
			car_x3+=-0.2
			screen.blit(bua2, (car_x3+30,car_x3w))
		elif car_x3>=Spell(k3,2,vitri3) and car_x6<=Spell(k3,2,vitri3)+20 and k3=='Spell/DungYen.png':
			car_x3=Spell(k3,2,vitri3)  
			screen.blit(bua3, (car_x3+30,car_x3w))          
		elif car_x3>=Spell(k3,2,vitri3) and y3==Spell(k3,2,vitri3) and k3=='Spell/LuiVeSau.png':
			screen.blit(bua4, (car_x3+30,car_x3w))
			if car_x3 > Spell(k3,2,vitri3) + 20:
				car_x3=Spell(k3,2,vitri3)-50
				y3=Spell(k3,2,vitri3)+1
			
		elif car_x3>=Spell(k3,2,vitri3) and k3=='Spell/VeNha.png' and venha3==0:
			screen.blit(bua5, (car_x3+30,car_x3w))
			if car_x3 > Spell(k3,2,vitri3) + 20:
				car_x3=10
				venha3=1
			
		elif car_x3>=Spell(k3,2,vitri3) and k3=='Spell/VeDich.png':
			screen.blit(bua6, (car_x3+30,car_x3w))
			if car_x3 > Spell(k3,2,vitri3) +20:
				car_x3=WINDOWHEIGHT+1000
			
		if car_x3 + 100 > WIN:
			car_x3 = WIN - 100
			checkwin(2)
		if result[2] == 1:
			screen.blit(canh, (car_x3- 55, car_x3w - 20))
			car_x3w -= speed
			if car_x3w < 220:
				speed *= -1
			if car_x3w > 290:
				speed *= -1
			if car_x3w < 270:
				screen.blit(happy, (car_x3+20, car_x3w +20))
			
		car_x4 += random.choice([1,2])
		#đây là dòng lệnh để vẽ và hiệu ứng xe 4
		if car_x4>=Spell(k4,3,vitri4) and k4=='Spell/TangToc.png':
			car_x4+=0.2
			screen.blit(bua1, (car_x4+30,car_x4w))
		elif car_x4>=Spell(k4,3,vitri4) and k4=='Spell/LamCham.png':
			car_x4+=-0.2
			screen.blit(bua2, (car_x4+30,car_x4w))
		elif car_x4>=Spell(k4,3,vitri4) and car_x6<=Spell(k4,3,vitri4)+20 and k4=='Spell/DungYen.png':
			car_x4=Spell(k4,3,vitri4) 
			screen.blit(bua3, (car_x4+30,car_x4w))           
		elif car_x4>=Spell(k4,3,vitri4) and y4==Spell(k4,3,vitri4) and k4=='Spell/LuiVeSau.png':
			screen.blit(bua4, (car_x4+30,car_x4w))
			if car_x4 > Spell(k4,3,vitri4) + 20:
				car_x4=Spell(k4,3,vitri4)-50
				y4=Spell(k4,3,vitri4)+1
			
		elif car_x4>=Spell(k4,3,vitri4) and k4=='Spell/VeNha.png' and venha4==0:
			screen.blit(bua5, (car_x4+30,car_x4w))
			if car_x4 > Spell(k4,3,vitri4) + 20:
				car_x4=10
				venha4=1
		
		elif car_x4>=Spell(k4,3,vitri4) and k4=='Spell/VeDich.png':
			screen.blit(bua6, (car_x4+30,car_x4w))
			if car_x4 > Spell(k4,3,vitri4) + 20:
				car_x4=WINDOWHEIGHT+1000
			
		if car_x4 + 100 > WIN:
			car_x4 = WIN - 100
			checkwin(3)
		if result[3] == 1:
			screen.blit(canh, (car_x4- 55, car_x4w - 20))
			car_x4w -= speed
			if car_x4w < 290:
				speed *= -1
			if car_x4w > 360:
				speed *= -1
			if car_x4w < 340:
				screen.blit(happy, (car_x4+20, car_x4w +20))
			
		car_x5 += random.choice([1,2])
		#đây là dòng lệnh để vẽ và hiệu ứng xe 5
		if car_x5>=Spell(k5,4,vitri5) and k5=='Spell/TangToc.png':
			car_x5+=0.2
			screen.blit(bua1, (car_x5+30,car_x5w))
		elif car_x5>=Spell(k5,4,vitri5) and k5=='Spell/LamCham.png':
			car_x5+=-0.2
			screen.blit(bua2, (car_x5+30,car_x5w))
		elif car_x5>=Spell(k5,4,vitri5) and car_x6<=Spell(k5,4,vitri5)+20 and k5=='Spell/DungYen.png':
			car_x5=Spell(k5,4,vitri5) 
			screen.blit(bua3, (car_x5+30,car_x5w))          
		elif car_x5>=Spell(k5,4,vitri5) and y5==Spell(k5,4,vitri5) and k5=='Spell/LuiVeSau.png':
			screen.blit(bua4, (car_x5+30,car_x5w))
			if car_x5 > Spell(k5,4,vitri5) + 20:
				car_x5=Spell(k5,4,vitri5)-50
				y5=Spell(k5,4,vitri5)+1
			
		elif car_x5>=Spell(k5,4,vitri5) and k5=='Spell/VeNha.png' and venha5==0:
			screen.blit(bua5, (car_x5+30,car_x5w))
			if car_x5 > Spell(k5,4,vitri5) + 20:
				car_x5=10
				venha5=1
			
		elif car_x5>=Spell(k5,4,vitri5) and k5=='Spell/VeDich.png':
			screen.blit(bua6, (car_x5+30,car_x5w))
			if car_x5 > Spell(k5,4,vitri5) + 20 and k5=='Spell/VeDich.png':
				car_x5=WINDOWHEIGHT+1000
				
			
		if car_x5 + 100 > WIN:
			car_x5 = WIN - 100
			checkwin(4)
		if result[4] == 1:
			screen.blit(canh, (car_x5- 55, car_x5w - 20))
			car_x5w -= speed
			if car_x5w < 360:
				speed *= -1
			if car_x5w > 430:
				speed *= -1
			if car_x5w < 410:
				screen.blit(happy, (car_x5+20, car_x5w +20))
			
		pygame.display.update()
		fpsClock.tick(FPS)
		if flag==[True,True,True,True,True]:
			break
	flag[0] = False
	flag[1] = False
	flag[2] = False
	flag[3] = False
	flag[4] = False

	pygame.mixer.music.stop()
	pygame.mixer.music.load('sound/clear.mp3')
	pygame.mixer.music.play(-1,0,0)
	
	
	screen.blit(pygame.image.load('Reward/BG_reward.jpg'), (0,0))
	screen.blit(pygame.image.load('Reward/1.png'), (40, 20))
	screen.blit(pygame.image.load('Reward/2.png'), (160, 70))
	screen.blit(pygame.image.load('Reward/3.png'), (270, 140))
	screen.blit(pygame.image.load('Reward/4.png'), (390, 230))
	screen.blit(pygame.image.load('Reward/5.png'), (510, 320))
	RATING(Your_character, Your_betting)
	pygame.display.update()
	
	fpsClock.tick(FPS)
	dulieu.history(score_bet, Your_betting)
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_BACKSPACE:
					pygame.mixer.music.stop()
					return

if __name__ == '__main__':
	Run(RunOption1(), RunOption2())