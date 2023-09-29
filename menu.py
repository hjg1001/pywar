#废弃的主界面文件
import pygame,button,time
pygame.init()
width,height=720,1600#窗口大小
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption='卡兹'
font=pygame.font.Font('NotoSerifCJK-Regular.ttc',100)
wxg=pygame.image.load('微笑哥.png').convert()
scale=0
pygame.mixer.music.load('rm.mp3')
pygame.mixer.music.set_volume(1)
start=False
class menu_class:
	def __init__(self):
		self.state=0#0主界面,1开始游戏
	def update(self):
		title=font.render('-',True,(255,255,255))
		title_rect = title.get_rect()
		title_rect.center=(width//2,height//2-height*0.35)
		screen.blit(title,title_rect)
menu=menu_class()
button1=button.button_claas(1,width//2-110,height//2-height*0.3,'+',(255,255,255),(0,0,0))
button1.init()
running=True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running=False
		elif event.type == pygame.MOUSEBUTTONUP:
			pos=pygame.mouse.get_pos()
			if (pos[0]>button1.x and pos[0]<button1.x+button1.size*230) and (pos[1]>button1.y and pos[1]<button1.y+button1.size*80):
				menu.state=1
	#清空
	screen.fill((0,0,0))
	#主界面
	if menu.state==0:
		menu.update()
		button1.render(screen,button1.text_img,button1.button_img)
	#开始游戏 设置界面
	elif menu.state==1 and scale <2.4:
		scale+=0.15
	if menu.state==1:
		wxg_1=pygame.transform.scale(wxg,((int(width*scale)),(int(height*scale))))
		wxg_2=wxg_1.get_rect(center=(width/2,height/2))
		screen.blit(wxg_1,wxg_2)
		if not start:
			pygame.mixer.music.play()
			start=True
			time.sleep(2.1)
	#重新渲染
	pygame.display.flip()