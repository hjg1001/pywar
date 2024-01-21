import pygame,control,random,terrain,setting,NPC,astar,tile
pygame.init()
screen=pygame.display.set_mode((720,1600))
font=pygame.font.Font('NotoSerifCJK-Regular.ttc',15)
ck=pygame.time.Clock()
pygame.mixer.music.set_volume(1)
pygame.mixer.init()


class map_class:
	def __init__(self,width,height):
		self.width,self.height=width,height
		self.scale=1#缩放
		self.vx,self.vy=0,0#x,y视角位置
		self.m_l,self.m_r,self.m_d,self.m_u=False,False,False,False#移动视角
		self.a_s,self.z_s=False,False#缩放地图
		self.grass1=pygame.image.load('grass.png').convert()
		self.map=pygame.Surface((setting.map_w,setting.map_h),pygame.SRCALPHA,32).convert()#小地图图层
		self.grass_back=pygame.Surface((width,height),32).convert()#草地图层
		self.display_surface=pygame.Surface((setting.width,setting.height),32)#显示图层
		self.sprite_group=pygame.sprite.Group()#地图精灵组
		self.block_group=pygame.sprite.Group()#区块精灵组
		self.o_sprite=pygame.sprite.Group()#其他精灵组
		self.npc_group=pygame.sprite.Group()#NPC精灵组
		self.s_npc=False#选中模式
		self.npc_obj=None#被选中的NPC对象
		self.change=False#正在修改NPC
		self.change_p=False#正在修改NPC属性
		self.npc_p=0#修改的NPC的属性
		self.npc_p_num=None#修改NPC属性的值
		self.npc_p_type=None#npc属性类型
		self.debug=None
		self.sound_list=[]
		self.team_list={}
		self.pause=False#暂停
		self.A_map=[]#二维简化地图
		self.m_surface=[]#切分区块列表
		self.astar_search=0
		self.flag_list=[]
		self.su_num=0
	def init(self):
		for i in range(int(self.height//60)):
			self.A_map.append([])
			for o in range(int(self.width//60)):
				self.A_map[i].append(0)
		self.astar_search=astar.Astar(self.A_map)
		for x in range(0,self.width,50):
			for y in range(0,self.height,50):
				self.grass_back.blit(self.grass1,(x,y),(random.randint(50,255-50),0,50,50))
		#初始化地形(草地除外)
		terrain.place_tree(map,map.sprite_group)#树
		#旗帜
		flag_num=0
		while flag_num<setting.flag_num:
			for y,Y in enumerate(self.A_map):
				if random.randint(0,1200)>1190:
					for x,X in enumerate(Y):
						if flag_num==setting.flag_num:break
						if X==0 and random.randint(0,300)>299:
							self.flag_list.append(terrain.flag(x*60,y*60))
							flag_num+=1
	def render(self,screen):
		#渲染旗帜
		for i in self.flag_list:
			if not i.oc:self.display_surface.blit(tile.flag,(i.x+map.vx,i.y+map.vy))
			if i.oc=='blue':self.display_surface.blit(tile.flag_blue,(i.x+map.vx,i.y+map.vy))
			if i.oc=='red':self.display_surface.blit(tile.flag_red,(i.x+map.vx,i.y+map.vy))
			point=font.render(str(i.point),True,(255,225,0))
			self.display_surface.blit(point,(i.x+9+map.vx,i.y-3+map.vy))
		#渲染显示图层
		screen.blit(self.display_surface,(0,0))
		#渲染小地图
		self.map.fill((255,255,255))
		for i in self.npc_group:
			if i.side=='red':color=(114,23,23)
			else:color=(7,96,177)
			pygame.draw.circle(self.map,color,((setting.map_w/self.width)*i.x,(setting.map_h/self.height)*i.y),2)
			pygame.draw.rect(self.map,(0,0,0),((setting.map_w/self.width)*(-self.vx),(setting.map_h/self.height)*(-self.vy),(setting.map_w/self.width)*setting.width,(setting.map_h/self.height)*setting.height),2)
		for i in self.flag_list:
			if not i.oc:color=(79,79,79)
			elif i.oc=='blue':color=(26,68,141)
			else:color=(102,15,15)
			pygame.draw.circle(self.map,color,((setting.map_w/self.width)*i.x,(setting.map_h/self.height)*i.y),5)
map=map_class(setting.mapw,setting.maph)
map.init()
NPC.create_npc(map)
zx=control.Zx(setting.width//2,setting.height//2)
while True:
	#操作检测
	for event in pygame.event.get():
		control.control(event,map)
	screen.fill((0,0,0,0))
	control.act(map,screen,zx)
	#渲染草地
	map.display_surface.fill((0,0,0))
	map.display_surface.blit(map.grass_back,(map.vx,map.vy))
	#渲染精灵 图层顺序低-高
	map.o_sprite.update(map)
	map.sprite_group.update(map)
	map.npc_group.update(map)
	#总渲染
	map.render(screen)
	#渲染左上角信息
	ck.tick(setting.fps)
	fps=font.render(str(int(ck.get_fps
	()))+'   暂停:'+str(map.pause)+'   debug: '+str(map.debug),True,(0,0,0),(255,255,255))
	screen.blit(fps,(0,5))
	control.draw_npc_info(screen,map,font)
	control.render_text(map,screen)
	#渲染准心
	zx.update(screen,map)
	#渲染小地图
	screen.blit(map.map,setting.m_p)
	map.map.set_alpha(setting.alpha)
	#播放音效
	if map.sound_list:
		for i in map.sound_list:
			sound=pygame.mixer.Sound(i)
			sound.play()
	map.sound_list.clear()
	#刷新屏幕
	pygame.display.update()