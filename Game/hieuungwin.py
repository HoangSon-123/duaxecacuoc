#thêm 2 ảnh
canh = pygame.image.load('Spell/canh.png')
happy = pygame.image.load('Spell/happy.png')
#trong hàm Run thêm biến speech
speech = 2
#sau lời gọi hàm checkwin(0) thì thêm 
		if result[0] == 1:
			screen.blit(canh, (car_x1- 55, car_x1w - 20))
			car_x1w -= speed
			if car_x1w < 80:
				speed *= -1
			if car_x1w > 150:
				speed *= -1
			if car_x1w < 130:
				screen.blit(happy, (car_x1+20, car_x1w +20))
#sau checkwin(1) thì thêm
		if result[1] == 1:
			screen.blit(canh, (car_x2- 55, car_x2w - 20))
			car_x2w -= speed
			if car_x2w < 150:
				speed *= -1
			if car_x2w > 220:
				speed *= -1
			if car_x2w < 200:
				screen.blit(happy, (car_x2+20, car_x2w +20))
#sau checkwin(2)
		if result[2] == 1:
			screen.blit(canh, (car_x3- 55, car_x3w - 20))
			car_x3w -= speed
			if car_x3w < 220:
				speed *= -1
			if car_x3w > 290:
				speed *= -1
			if car_x3w < 270:
				screen.blit(happy, (car_x3+20, car_x3w +20))
#sau checkwin (3)
		if result[3] == 1:
			screen.blit(canh, (car_x4- 55, car_x4w - 20))
			car_x4w -= speed
			if car_x4w < 290:
				speed *= -1
			if car_x4w > 360:
				speed *= -1
			if car_x4w < 340:
				screen.blit(happy, (car_x4+20, car_x4w +20))
#sau checkwin(4)
		if result[4] == 1:
			screen.blit(canh, (car_x5- 55, car_x5w - 20))
			car_x5w -= speed
			if car_x5w < 360:
				speed *= -1
			if car_x5w > 430:
				speed *= -1
			if car_x5w < 410:
				screen.blit(happy, (car_x5+20, car_x5w +20))

