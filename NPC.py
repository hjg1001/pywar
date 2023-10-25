import pygame,NPC_act,setting,random,tile



class shell(pygame.sprite.Sprite):#弹壳
	def __init__(self,x,y,angle):
		self.type='shell'
		pygame.sprite.Sprite.__init__(self)
		self.image_old=pygame.image.load('弹壳.png')
		self.img2=pygame.image.load('弹夹.png')
		self.image=self.image_old
		self.rect=self.image.get_rect()
		self.x,self.y=self.rect.x,self.rect.y=x,y
		self.scale=1.2
		self.angle=angle
		self.time=0
		self.max_scale=0.8
		self.target=[x+15+abs(15*(random.random()-random.random())),y+6+10*(random.random()-random.random())]
	def update(self,screen,map):#弹壳掉落
		self.rect.x,self.rect.y=map.scale*self.x+map.vx,map.scale*self.y+map.vy
		if self.target!=[self.x,self.y]:
			pos=NPC_act.move_q(self.x,self.y,self.target[0],self.target[1],1.2)
			if self.scale>self.max_scale:self.scale-=0.05
			self.x,self.y=pos[0],pos[1]
		self.image=self.image_old
		self.image=pygame.transform.rotate(self.image,self.angle)
		self.image=pygame.transform.scale(self.image,(int(2*self.scale),int(5*self.scale)))
		screen.blit(self.image,(self.x,self.y))
		self.time+=1
		if self.time>500:self.image_old.set_alpha(255-(self.time-500)*4)
		elif self.time>550:del self




class NPC(pygame.sprite.Sprite):
	def __init__(self,x,y,side):
		self.type='npc'
		pygame.sprite.Sprite.__init__(self)
		if side=='red':self.image=tile.red_none_1
		else:self.image=tile.blue_none_1
		self.surface=pygame.Surface((32,50),pygame.SRCALPHA)#个体NPC整体表面
		self.rect=self.image.get_rect()
		self.x,self.y=self.rect.x,self.rect.y=x,y
		self.target_x,self.target_y=0,0
		self.shoot_x,self.shoot_y=0,0
		self.aim=0#瞄准完成度/进度
		self.angle=0
		self.target_angle=0
		self.none_x=0
		self.reload_time=0
		self.frame=1
		self.anim=0#帧计时
		self.anim_max=1#帧计时最大值
		self.old_state=None#旧状态
		self.debug_cmd=0
		self.time,self.time2=0,0
		self.jd,self.max_jd=0,0#进度条的进度,上限
		#NPC属性
		self.gun={'name':'1','ammo':1,'max_ammo':5}
		self.rifle_ammo,self.rifle_clip=10,1
		self.side=side#阵营(red/bule)
		self.team=0#部队编号
		self.job=None#职位
		self.level=0#等级(作战水平)
		self.speed=1.9#当前的速度
		self.state=None#当前状态
		self.action=None#当前行为
	def draw_update(self,surface,fire):#把NPC渲染出来
		self.surface.fill((0,0,0,0))
		self.surface.blit(self.image,(0,15))
		#调试用线段
		if self.state=='move':pygame.draw.line(surface,(0,0,90),(self.x,self.y),(self.target_x,self.target_y))
		#枪口特效
		if fire or (self.time>0 and self.time<6):
			self.time+=1
			self.surface.blit(pygame.transform.scale(eval('tile.fire_'+str(random.randint(1,5))),(35,40)),(-2,-10))
		elif not fire:
			self.time=0
		if fire or (self.time2>0 and self.time2<30):
			self.time2+=1
			fire_smoke=tile.fire_smoke
			self.surface.blit(pygame.transform.scale((fire_smoke),(20,29)),(2,-9-self.time2*0.3))
			fire_smoke.set_alpha(65-self.time2*1.8)
		elif not fire:
			self.time2=0
		#整体渲染
		surface.blit(pygame.transform.rotate(self.surface,self.angle),(self.x,self.y))
	def npc_tile(self):#更新贴图(动画)
		tile.update(self)
		if self.anim<self.anim_max:
			self.anim+=1/60+setting.anim_speed
		else:
			self.anim=0
		#旋转
		if self.angle!=self.target_angle:
			if self.angle<self.target_angle:self.angle+=3
			elif self.angle>self.target_angle:self.angle-=3
		if abs(self.target_angle-self.angle)<3:
			self.angle=self.target_angle
		if abs(self.angle)>360 or abs(self.target_angle)>360:self.angle,self.target_angle=0,0
	def update(self,surface,map):#更新行为
		self.rect.x,self.rect.y=map.scale*self.x+map.vx,map.scale*self.y+map.vy
		#---行为---
		fire=False
		if not map.pause:
				#移动
			NPC_act.move(self)
				#开枪
			if self.action=='shoot':fire=NPC_act.shoot(self)
			if fire:
				map.sound_list.append('步枪开火.wav')
				map.o_sprite.add(shell(self.x+18,self.y+15,self.angle))
				#装弹
			if self.state=='reload':
				if NPC_act.reload(self,map):
					clip=shell(self.x+18,self.y+15,self.angle)
					clip.image_old=clip.img2
					clip.scale,clip.max_scale=2,1.3
					map.o_sprite.add(clip)
			#---动画----#
			self.npc_tile()
			if self.max_jd!=0 and setting.jd:
				jd1=pygame.Surface((self.max_jd,5),pygame.SRCALPHA)#进度条(灰)
				jd1.fill((255,255,255))
				jd2=pygame.Surface((self.jd,5))#进度条(白)
				jd2.fill((255,255,255))
				jd1.set_alpha(40)
				jd2.set_alpha(90)
				map.display_surface.blit(jd1,(self.x-9,self.y+25))
				map.display_surface.blit(jd2,(self.x-9,self.y+25))
		#--调试用--
		if map.npc_obj:
			if self.debug_cmd==1:self.target_x,self.target_y=random.uniform(0.1,0.9)*map.width,random.uniform(0.1,0.9)*map.height
			if self.debug_cmd==2:self.action='shoot'
		else:self.debug_cmd=0
		#--渲染到屏幕---#
		self.draw_update(surface,fire)

		
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