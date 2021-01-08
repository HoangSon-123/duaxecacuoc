import pygame as pg
import sys, os
import Head

pg.init()
Head.init()
# define
screen = pg.display.set_mode((1000, 600))
FONT = pg.font.SysFont('Consolas', 40)

# Hàm hiện giao diện nhập username cho người chơi
def Input_Username():
    screen = pg.display.set_mode((1000, 600))
    clock = pg.time.Clock()
    username = ''

    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    pg.mixer.music.load('sound/button.mp3')
                    pg.mixer.music.play(1)
                    done = True
                if event.key == pg.K_BACKSPACE:
                    username = username[:-1]
                else:  # Add the character to the password string.
                    username += event.unicode

        screen.blit(pg.image.load('Login/BG1.png'), (0,0))
        # Render the asterisks and blit them.
        username_surface = FONT.render(username, True, (0, 0, 0))
        screen.blit(username_surface, (305, 298))

        pg.display.flip()
        clock.tick(30)
    return username

# Hàm hiện giao diện nhập password
def Input_Password(username):
    screen = pg.display.set_mode((1000, 600))
    clock = pg.time.Clock()
    password = ''

    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    if os.path.isfile(username + '.txt') == 0:
                        file_obj = open(username + ".txt", mode = 'w')
                        file_obj.write(password + '\n')
                        #file_obj.write('200')
                        file_obj.close()
                        Head.money = 200
                    else:
                        file_obj = open(username + ".txt", mode = 'r')
                        data_password = file_obj.readline()
                        if data_password != (password + '\n'):
                            Input_Password(username)
                        Head.money = int(file_obj.readline())
                        file_obj.close()
                    pg.mixer.music.load('sound/button.mp3')
                    pg.mixer.music.play(1)
                    done = True
                if event.key == pg.K_BACKSPACE:
                    password = password[:-1]
                else:  # Add the character to the password string.
                    password += event.unicode

        screen.blit(pg.image.load('Login/BG2.png'), (0,0))
        # Render the asterisks and blit them.
        password_surface = FONT.render('*'*len(password), True, (0, 0, 0))
        screen.blit(password_surface, (305, 304))

        pg.display.flip()
        clock.tick(30)
    return password