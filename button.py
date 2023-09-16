import  pygame
pygame.init()
class button_claas:
	def __init__(self,size,x,y,text,button_color,text_color):
		self.size=int(size)
		self.button_color=button_color
		self.text_color=text_color
		self.text=text
		self.x,self.y=x,y
		self.button_img,self.text_img=0,0
	def init(self):
		font=pygame.font.Font('NotoSerifCJK-Regular.ttc',50*self.size)
		text_img=font.render(self.text,True,self.text_color)
		button_img=pygame.Surface((230*self.size,80*self.size))
		button_img.fill(self.button_color)
		self.button_img,self.text_img=button_img,text_img
	def render(self,screen,text_img,button_img):
		screen.blit(button_img,(self.x,self.y))
		screen.blit(text_img,(self.x+16,self.y))
		text_rect=text_img.get_rect()
		text_rect.center=((200*self.size)//2,(100*self.size)//2)