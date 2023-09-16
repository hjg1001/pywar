import pygame,random,setting
class leaf_class(pygame.sprite.Sprite):
	def __init__(self,x,y):
		self.type='leaf'
		pygame.sprite.Sprite.__init__(self)
		img_big=pygame.image.load('tree.png').convert_alpha()
		self.img=img_big.subsurface(pygame.Rect(0,0,31,32)).convert_alpha()
		self.rect=self.img.get_rect()
		self.rect.x,self.rect.y=x,y
class trunk_class(pygame.sprite.Sprite):
	def __init__(self,x,y):
		pygame.sprite.Sprite.__init__(self)
		self.type='tree'
		image_big=pygame.image.load('tree.png').convert_alpha()
		self.image=image_big.subsurface(pygame.Rect(33,0,32,32)).convert_alpha()
		self.rect=self.image.get_rect()
		self.rect.x,self.rect.y=self.x,self.y=x,y
		self.leaf=0#与之绑定的树叶对象
	def draw_init(self,screen,terrain_back):#初始化图像
		terrain_back.blit(self.image,(self.rect.x,self.rect.y))
		self.leaf.img=pygame.transform.scale(self.leaf.img,(40,40))
		terrain_back.blit(self.leaf.img,(self.leaf.rect.x,self.leaf.rect.y))
	def update(self,screen,map,terrain_back,state):
		if state=='init':self.draw_init(screen,terrain_back)
def place_tree(map,sprite):#放树
	first=True
	for u in range(1,random.randint(setting.tree_num[0],setting.tree_num[1])):
		place=False
		while not place:#找不到安放树的点就一直找
			cant=False
			tree_x,tree_y=random.randint(5,map.width*0.95),random.randint(5,map.height*0.95)
			for i in sprite:
				first=False
				if abs(i.rect.x-tree_x)<setting.tree_x and abs(i.rect.y-tree_y)<setting.tree_y:cant=True
			if first:#第一棵树
				pos=[random.randint(map.width*0.9,map.height*0.9),random.randint(map.width*0.9,map.height*0.9)]
				obj=trunk_class(pos[0],pos[1])
				obj1=leaf_class(pos[0]-5,pos[1]-25)
				sprite.add(obj)
				sprite.add(obj1)
				obj.leaf=obj1
			elif not cant:place=True#当前坐标能放树
		if not first:#放树
			obj=trunk_class(tree_x,tree_y)
			obj1=leaf_class(tree_x-5,tree_y-25)
			sprite.add(obj)
			sprite.add(obj1)
			obj.leaf=obj1