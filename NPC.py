import pygame,NPC_act,setting,random,tile
class NPC(pygame.sprite.Sprite):
	def __init__(self,x,y,side):
		self.type='npc'
		pygame.sprite.Sprite.__init__(self)
		if side=='red':self.image=tile.red_none_1
		else:self.image=tile.blue_none_1
		self.rect=self.image.get_rect()
		self.x,self.y=self.rect.x,self.rect.y=x,y
		self.target_x,self.target_y=0,0
		self.shoot_x,self.shoot_y=0,0
		self.angle=0
		self.target_angle=0
		self.none_anim,self.none_x=False,0
		#NPC属性
		self.side=side#阵营(red/bule)
		self.speed=1#当前的速度
		self.state=None#当前状态
		self.action=None#当前行为
		self.frame=1
	def draw_update(self,surface):#把NPC渲染出来
		surface.blit(self.image,(self.x,self.y))
		
	
	def npc_tile(self):#更新贴图(动画)
		if tile.update(self):
			self.image=pygame.transform.rotate(self.image,self.target_angle)


	def update(self,surface,map):#更新行为
		self.rect.x,self.rect.y=map.scale*self.x+map.vx,map.scale*self.y+map.vy
		#---行为---
		NPC_act.move(self)#移动
		#---动画----#
		self.npc_tile()
		#--渲染到屏幕---#
		self.draw_update(surface)
		
		
def create_npc(map):#开局NPC生成
	red,blue=0,0#红蓝数量
	while red<setting.npc_red_num or blue<setting.npc_blue_num:
		x,y=random.randint(35,map.width*0.95),random.randint(45,map.height*0.95)
		if red==0:#红 空的
			place=True
			for obj in map.sprite_group:
				if obj.type=='tree' and abs(obj.x-x)<60 and abs(obj.y-y)<60:
					place=False #和树干重合
			if place:
				red+=1#放置第一个红队NPC
				map.npc_group.add(NPC(x,y,'red'))
		elif red<setting.npc_red_num:#红队人不齐
			for obj in map.npc_group:
				if obj.side=='red':
					pd=True
					while pd:#在队友附近找落脚点
						x,y=obj.x+random.randint(setting.min,setting.max),obj.y+random.randint(setting.min,setting.max)
						if map.width>x>0 and map.height>y>0:
							pd=False
				else:
					continue
			place=True
			for obj in map.sprite_group:
				if obj.type=='tree' and abs(obj.x-x)<60 and abs(obj.y-y)<60:
					place=False #和树干重合
			for obj in map.npc_group:
				if abs(obj.x-x)<60 and abs(obj.y-y)<80:
					place=False #和npc重合
			if place:
				red+=1
				map.npc_group.add(NPC(x,y,'red'))
#--蓝队--
		if blue==0:
			place=True
			for obj in map.sprite_group:
				if obj.type=='tree' and abs(obj.x-x)<60 and abs(obj.y-y)<60:
					place=False #和树干重合
			for obj in map.npc_group:
				if abs(obj.x-x)<60 and abs(obj.y-y)<80:
					place=False#npc重合
			if place:
				blue+=1#放置第一个蓝队NPC
				map.npc_group.add(NPC(x,y,'blue'))
		elif blue<setting.npc_blue_num:#红队人不齐
			for obj in map.npc_group:
				if obj.side=='blue':
					pd=True
					while pd:#在队友附近找落脚点
						x,y=obj.x+random.randint(setting.min,setting.max),obj.y+random.randint(setting.min,setting.max)
						if map.width-30>x>0 and map.height-30>y>0:
							pd=False
				else:
					continue
			place=True
			for obj in map.sprite_group:
				if obj.type=='tree' and abs(obj.x-x)<60 and abs(obj.y-y)<60:
					place=False #和树干重合
			for obj in map.npc_group:
				if abs(obj.x-x)<60 and abs(obj.y-y)<80:
					place=False #和npc重合
			if place:
				blue+=1
				map.npc_group.add(NPC(x,y,'blue'))