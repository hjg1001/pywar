import pygame,control,random,terrain,setting,NPC
pygame.init()
screen=pygame.display.set_mode((720,1600))
font=pygame.font.Font('NotoSerifCJK-Regular.ttc',15)
ck=pygame.time.Clock()




class map_class:
	def __init__(self,width,height):
		self.width,self.height=width,height
		self.scale=1#缩放
		self.vx,self.vy=0,0#x,y视角位置
		self.m_l,self.m_r,self.m_d,self.m_u=False,False,False,False#移动视角
		self.a_s,self.z_s=False,False#缩放地图
		self.grass1=pygame.image.load('grass.png').convert()
		self.grass_back=pygame.Surface((width,height),pygame.SRCALPHA).convert()#非精灵图层
		self.display_surface=pygame.Surface((width,height),pygame.OPENGL)#显示图层
		self.sprite_group=pygame.sprite.Group()
		self.npc_group=pygame.sprite.Group()
		self.npc_obj=None#被选中的NPC对象
		self.change=False#正在修改NPC
		self.change_p=False#正在修改NPC属性
		self.npc_p=0#修改的NPC的属性
		self.npc_p_num=None#修改NPC属性的值
		self.npc_p_type=None#npc属性类型
		self.debug=None
	def init(self):
		for x in range(0,self.width,50):
			for y in range(0,self.height,50):
				self.grass_back.blit(self.grass1,(x,y),(random.randint(50,255-50),0,50,50))
		#初始化地形(草地除外)
		terrain.place_tree(map,map.sprite_group)#树
	def render(self,screen):
		#渲染图层
		new_dis=pygame.transform.scale(self.display_surface,(int(self.width*self.scale),int(self.height*self.scale)))
		screen.blit(new_dis,(self.vx,self.vy))


map=map_class(1000,1600)
map.init()
map.sprite_group.update(screen,map,map.grass_back,'init')
NPC.create_npc(map)
zx=control.Zx(setting.width//2,setting.height//2)
while True:
	#操作检测
	for event in pygame.event.get():
		control.control(event,map)
	screen.fill((0,0,0,0))
	control.act(map,screen)
	#渲染非精灵
	map.display_surface.blit(map.grass_back,(0,0))
	#渲染精灵 图层顺序低-高
	map.sprite_group.update(screen,map,map.display_surface,'else')
	map.npc_group.update(map.display_surface,map)
	#渲染图层
	map.render(screen)
	#渲染左上角信息
	ck.tick(setting.fps)
	fps=font.render(str(int(ck.get_fps()))+'-----------'+str(map.npc_obj)+'-------debug: '+str(map.debug),True,(0,0,0),(255,255,255))
	screen.blit(fps,(0,5))
	control.draw_npc_info(screen,map,font)
	map.debug=map.change,map.change_p,map.npc_obj,map.npc_p,map.npc_p_num
	control.render_text(map,screen)
	#渲染准心
	zx.update(screen,map)
	#刷新屏幕
	pygame.display.update()