import pygame,setting,random
class Zx(pygame.sprite.Sprite):#准心
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image=pygame.image.load('准心.png')
		self.rect=self.image.get_rect()
		self.rect.x,self.rect.y=self.x,self.y=x,y
	def update(self,screen,map):
		screen.blit(self.image,(self.rect.x,self.rect.y))
		result=pygame.sprite.spritecollideany(self,map.npc_group)
		if result!=None:
			map.npc_obj=result
		else:
			map.npc_obj=None
def control(event,map):
	if event.type == pygame.KEYDOWN:
		if event.key == pygame.K_z and not(map.change or map.change_p):
			map.z_s=True
		if event.key==pygame.K_a and not map.s_npc and not(map.change or map.change_p):#选中NPC
			map.s_npc=True
		elif event.key==pygame.K_a:
			map.s_npc=False
		if event.key==pygame.K_UP:
			if map.change and map.npc_p>0 and not map.change_p:
				map.npc_p-=1
			elif map.change and not map.change_p:
				map.npc_p=len(setting.npc_info_list)-1
			elif not map.change_p:
				map.m_u=True
		if event.key==pygame.K_DOWN:
			if map.change and map.npc_p<len(setting.npc_info_list)-1 and not map.change_p:
				map.npc_p+=1
			elif map.change and not map.change_p:
				map.npc_p=0
			elif not map.change_p:
				map.m_d=True
		if event.key==pygame.K_LEFT:
			if map.change and not map.change_p:
				pass
			elif not map.change_p:
				map.m_l=True
		if event.key==pygame.K_RIGHT:
			if not map.change_p and map.change:
				map.change_p=True
				map.change=False
			elif map.change_p:#改变属性
				map.change_p=False
				map.change=False
				if type(map.npc_p_num)==str and map.npc_p_type!=str:#修正
					if map.npc_p_type==int:map.npc_p_num=int(map.npc_p_num)
					else:map.npc_p_num=eval(map.npc_p_num)
				setattr(map.npc_obj,setting.npc_info_list[map.npc_p],map.npc_p_num)
				map.npc_p_num=None
				map.npc_p_type=None
			if not map.change and not map.change_p:
				map.m_r=True
		if event.key==pygame.K_c and map.npc_obj!=None and not map.change_p:
			if map.change:
				map.change=False
			else:
				map.change=True
				map.s_npc=False
				map.m_l,map.m_r,map.m_d,map.m_u=False,False,False,False
#------debug---------
		if event.key==pygame.K_b and map.npc_obj:
			map.npc_obj.target_x,map.npc_obj.target_y=random.uniform(0.1,0.9)*map.width,random.uniform(0.1,0.9)*map.height
#-------------------------
		#输入框
		if map.change_p and event.key==pygame.K_BACKSPACE:#删除
			if map.npc_p_num:
				if map.npc_p_type==str:#字符串
					map.npc_p_num=str(map.npc_p_num)[:-1]
				else:#非字符串
					if map.npc_p_type==int:#整数 可以删完
							map.npc_p_num=str(map.npc_p_num)[:-1]
							if len(map.npc_p_num)>0:map.npc_p_num=int(map.npc_p_num)
					#数组等 不能删完 留个开头
					elif len(map.npc_p_num)>1:
						map.npc_p_num=str(map.npc_p_num)[:-1]
						if map.npc_p_num:map.npc_p_num=eval(map.npc_p_num)
		elif map.change_p and map.npc_p_type:#输入
			c_input=str(event.unicode)
			if map.npc_p_type==str:map.npc_p_num+=c_input#字符串
			else:#非字符串
				if map.npc_p_type==int:#整数
						map.npc_p_num=int(str(map.npc_p_num)+c_input)
				else:#数组之类
					map.npc_p_num=eval(str(map.npc_p_num)+c_input)
	#松开按键
	if event.type == pygame.KEYUP:
		if event.key==pygame.K_z:
			map.z_s=False
		if event.key==pygame.K_UP:
			map.m_u=False
		if event.key==pygame.K_DOWN:
			map.m_d=False
		if event.key==pygame.K_LEFT:
			map.m_l=False
		if event.key==pygame.K_RIGHT:
				map.m_r=False
def act(map,screen,zx):
	if map.m_u and map.vy<0 and not map.s_npc:
		map.vy+=10
	elif map.m_u and map.s_npc:#改变准心位置
		zx.rect.y-=5
	elif map.m_d and -map.vy+setting.height<map.height and not map.s_npc:
		map.vy-=10
	elif map.s_npc and map.m_d:#改变准心位置
		zx.rect.y+=5
	if map.m_l and map.vx<0 and not map.s_npc:
		map.vx+=10
	elif map.s_npc and map.m_l:#改变准心位置
		zx.rect.x-=5
	if map.m_r and -map.vx+setting.width<map.width and not map.s_npc:
		map.vx-=10
	elif map.s_npc and map.m_r:#改变准心位置
		zx.rect.x+=5
def render_text(map,screen):#渲染输入框
	if map.change_p:
		font=pygame.font.Font('NotoSerifCJK-Regular.ttc',40)
		if map.npc_p_num==None:
			map.npc_p_num=getattr(map.npc_obj,setting.npc_info_list[map.npc_p])
			map.npc_p_type=type(map.npc_p_num)
		text=font.render('修改'+setting.npc_info_list[map.npc_p]+'为: '+str(map.npc_p_num),True,(255,255,255))
		screen.blit(text,(setting.width//2-120,setting.height//2))
def draw_npc_info(screen,map,font):
	if map.npc_obj!=None:
		y=5
		list_index=0
		while list_index!=len(setting.npc_info_list):
			for info in dir(map.npc_obj):
				if info in setting.npc_info_list and setting.npc_info_list.index(info)==list_index:
					y+=30
					list_index+=1
					color=(255,255,255)
					if setting.npc_info_list.index(info)==map.npc_p:
						color=(230,250,222)
					info_text=font.render(str(info)+' :'+str(getattr(map.npc_obj,info)),True,(0,0,0),color)
					screen.blit(info_text,(0,y))