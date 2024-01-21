import pygame,random,setting
#旗帜
flag=pygame.image.load('flag.png')
flag_blue=pygame.image.load('flag_blue.png')
flag_red=pygame.image.load('flag_red.png')
#NPC贴图
#步枪
	#闲置
red=pygame.image.load('none.png')
blue=red.copy()
for x in range(red.get_width()):
	for y in range(red.get_height()):
		if blue.get_at((x,y))==(114,23,23):
			blue.set_at((x,y),(97,96,177))
red_none,blue_none=[],[]
for tile in range(4):
	red_none.append(red.subsurface(pygame.Rect(0+tile*30,0,30,39)))
	blue_none.append(blue.subsurface(pygame.Rect(0+tile*30,0,30,39)))
	#走路
red=pygame.image.load('walk.png')
blue=red.copy()
for x in range(red.get_width()):
	for y in range(red.get_height()):
		if blue.get_at((x,y))==(114,23,23):
			blue.set_at((x,y),(97,96,177))
red_walk,blue_walk=[],[]
for tile in range(4):
	red_walk.append(red.subsurface(pygame.Rect(0+tile*30,0,30,39)))
	blue_walk.append(blue.subsurface(pygame.Rect(0+tile*30,0,30,39)))
	#跑步
red=pygame.image.load('run.png')
blue=red.copy()
for x in range(red.get_width()):
	for y in range(red.get_height()):
		if blue.get_at((x,y))==(114,23,23):
			blue.set_at((x,y),(97,96,177))
red_run,blue_run=[],[]
for tile in range(4):
	red_run.append(red.subsurface(pygame.Rect(0+tile*30,0,30,39)))
	blue_run.append(blue.subsurface(pygame.Rect(0+tile*30,0,30,39)))
	#瞄准
red=pygame.image.load('aim.png')
blue=red.copy()
for x in range(red.get_width()):
	for y in range(red.get_height()):
		if blue.get_at((x,y))==(114,23,23):
			blue.set_at((x,y),(97,96,177))
red_aim,blue_aim=[],[]
for tile in range(3):
	red_aim.append(red.subsurface(pygame.Rect(0+tile*30,0,30,39)))
	blue_aim.append(blue.subsurface(pygame.Rect(0+tile*30,0,30,39)))
	#开火
red=pygame.image.load('shoot.png')
blue=red.copy()
for x in range(red.get_width()):
	for y in range(red.get_height()):
		if blue.get_at((x,y))==(114,23,23):
			blue.set_at((x,y),(97,96,177))
red_shoot,blue_shoot=[],[]
for tile in range(3):
	red_shoot.append(red.subsurface(pygame.Rect(0+tile*30,0,30,39)))
	blue_shoot.append(blue.subsurface(pygame.Rect(0+tile*30,0,30,39)))
#手枪
	#闲置
red=pygame.image.load('none1.png')
blue=red.copy()
for x in range(red.get_width()):
	for y in range(red.get_height()):
		if blue.get_at((x,y))==(114,23,23):
			blue.set_at((x,y),(97,96,177))
red_none1,blue_none1=[],[]
for tile in range(4):
	red_none1.append(red.subsurface(pygame.Rect(0+tile*30,0,30,39)))
	blue_none1.append(blue.subsurface(pygame.Rect(0+tile*30,0,30,39)))
	#走路
red=pygame.image.load('walk1.png')
blue=red.copy()
for x in range(red.get_width()):
	for y in range(red.get_height()):
		if blue.get_at((x,y))==(114,23,23):
			blue.set_at((x,y),(97,96,177))
red_walk1,blue_walk1=[],[]
for tile in range(4):
	red_walk1.append(red.subsurface(pygame.Rect(0+tile*30,0,30,39)))
	blue_walk1.append(blue.subsurface(pygame.Rect(0+tile*30,0,30,39)))
	#瞄准
red=pygame.image.load('aim1.png')
blue=red.copy()
for x in range(red.get_width()):
	for y in range(red.get_height()):
		if blue.get_at((x,y))==(114,23,23):
			blue.set_at((x,y),(97,96,177))
red_aim1,blue_aim1=[],[]
for tile in range(2):
	red_aim1.append(red.subsurface(pygame.Rect(0+tile*30,0,30,39)))
	blue_aim1.append(blue.subsurface(pygame.Rect(0+tile*30,0,30,39)))
	#开火
red=pygame.image.load('shoot1.png')
blue=red.copy()
for x in range(red.get_width()):
	for y in range(red.get_height()):
		if blue.get_at((x,y))==(114,23,23):
			blue.set_at((x,y),(97,96,177))
red_shoot1,blue_shoot1=[],[]
for tile in range(3):
	red_shoot1.append(red.subsurface(pygame.Rect(0+tile*30,0,30,39)))
	blue_shoot1.append(blue.subsurface(pygame.Rect(0+tile*30,0,30,39)))
#开枪火焰
fire=pygame.image.load('步枪开火.png')
fire_1=fire.subsurface(pygame.Rect(1,1,20,24))
fire_2=fire.subsurface(pygame.Rect(21,1,20,24))
fire_3=fire.subsurface(pygame.Rect(41,1,20,24))
fire_4=fire.subsurface(pygame.Rect(61,1,20,24))
fire_5=fire.subsurface(pygame.Rect(79,1,20,24))
#枪烟
fire_smoke=pygame.image.load('烟.png')
fire_smoke.set_alpha(50)
def update(npc):
	if npc.old_state!=npc.state:#重置动画帧
		npc.anim=0
		if npc.p==True:npc.frame=1
	#动画参数
	anim_state='none'#动画类型
	anim_start=False#开始下一帧 bool
	anim_farme=1#总帧率
	anim_x=False#反序
	if npc.state==None:
		#闲置状态
		npc.anim_max=0.2+random.random()*0.05
		anim_x=False
		anim_state='none'
		if npc.gun['type']==1:anim_state='none1'
		anim_start=npc.anim>npc.anim_max
		anim_farme=4
	if npc.state=='move' and npc.speed<=1.5:
		#慢速移动状态
		npc.anim_max=0.45/npc.speed
		anim_state='walk'
		if npc.gun['type']==1:anim_state='walk1'
		anim_start=npc.anim>npc.anim_max
		anim_farme=4
		anim_x=False
	if npc.state=='move' and npc.speed>1.5:
		#快速移动状态
		npc.anim_max=0.25
		anim_state='run'
		if npc.gun['type']==1:anim_state='walk1'
		anim_start=npc.anim>npc.anim_max
		anim_farme=4
	if npc.state=='aim':
		#瞄准
		npc.anim_max=0.15+random.random()*0.05
		anim_state='aim'
		anim_start=npc.anim>npc.anim_max
		anim_farme=3
		if npc.frame==3:anim_start=False
		if npc.gun['type']==1:
			anim_state='aim1'
			anim_farme=2
			if npc.frame==2:anim_start=False
	if npc.state=='shoot':
		#开火
		npc.anim_max=0.01
		anim_state='shoot'
		if npc.gun['type']==1:
			npc.anim_max=0.01
			anim_state='shoot1'
		anim_start=npc.anim>npc.anim_max
		anim_farme=3
	if npc.state=='reload':
		#装弹
		npc.anim_max=0.5
		anim_state='run'
		npc.frame=2
		if npc.gun['type']==1:
			anim_state='none1'
			npc.frame=1
		anim_start=True
		anim_farme=2
#循环动画
	if npc.side==npc.side and anim_start:
		if npc.frame<anim_farme+1 and npc.none_x==0:#正序
			npc.image=eval(npc.side+'_'+anim_state)[npc.frame-1]
			npc.frame+=1
		elif npc.none_x==0 and anim_x:
			npc.none_x=1
		if not anim_x and npc.frame>anim_farme:
			npc.frame=1
		if npc.none_x==1 and anim_x:#反序
			if npc.frame!=1:npc.frame-=1
			npc.image=eval(npc.side+'_'+anim_state)[npc.frame-1]
			if npc.frame==1:
				npc.none_x=0
	if npc.side==npc.side:
		a_frame=npc.frame
		if anim_state=='none':anim_farme=4
		if a_frame>anim_farme:a_frame=npc.frame-1
		if a_frame<1:a_frame=1
		npc.image=eval(npc.side+'_'+anim_state)[a_frame-1]

	

	






	#记录旧动画
	npc.old_state=npc.state
	npc.p=True
	return anim_start