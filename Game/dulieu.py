from pygame.locals import*
import datetime
import user
# cái này viết sau khi các xe chạm đích và hàm flag nó break rồi thì thêm cái history() dô là được
def history(score,bet):
	time_game=datetime.datetime.now()
	luu=str(time_game)
	f=open('lichsu.txt','a+')
	f.write(luu+' ')
	if score==1:
		f.write('V ')
		BET=str(bet)
	else:
		f.write('X ')
		BET='-'+str(bet)
	f.write(BET+'\n')
	f.close()
def doc():
	f=open('lichsu.txt','r')
	i=f.readline()	
	return i
# tạo ra 1 cửa sổ lịch sử rồi in cái này ra là sẽ đọc ra được cái lịch sử đó





