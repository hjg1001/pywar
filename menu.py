#主文件
import pygame,button,setting
pygame.init()
width,height=setting.width,setting.height#窗口大小
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption='PYWAR'
font=pygame.font.Font('NotoSerifCJK-Regular.ttc',100)
class menu_class:
	def __init__(self):
		self.state=0#0主界面,1开始游戏
	def update(self):
		title=font.render('PYWAR',True,(255,255,255))
		title_rect = title.get_rect()
		title_rect.center=(width//2,height//2-height*0.35)
		screen.blit(title,title_rect)
menu=menu_class()
button1=button.button_claas(1,width//2-110,height//2-height*0.3,'开始模拟',(255,255,255),(0,0,0))
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
	elif menu.state==1:
		print('开始')
	#重新渲染
	pygame.display.flip()