import pygame,random,setting
#NPC贴图
red=pygame.image.load('npc.png')
blue=red.copy()
for x in range(red.get_width()):
	for y in range(red.get_height()):
		if blue.get_at((x,y))==(114,23,23):
			blue.set_at((x,y),(97,96,177))
#NPC 闲置
red_none_1=red.subsurface(pygame.Rect(1,1,30,39))
blue_none_1=blue.subsurface(pygame.Rect(1,1,30,39))
	
red_none_2=red.subsurface(pygame.Rect(33,1,31,39))
blue_none_2=blue.subsurface(pygame.Rect(33,1,31,39))
#npc移动(慢)
red_walk_1=red.subsurface(pygame.Rect(66,1,31,39))
blue_walk_1=blue.subsurface(pygame.Rect(66,1,31,39))

red_walk_2=red.subsurface(pygame.Rect(99,1,31,39))
blue_walk_2=blue.subsurface(pygame.Rect(99,1,31,39))

red_walk_3=red.subsurface(pygame.Rect(132,1,31,39))
blue_walk_3=blue.subsurface(pygame.Rect(132,1,31,39))

red_walk_4=red.subsurface(pygame.Rect(165,1,31,39))
blue_walk_4=blue.subsurface(pygame.Rect(165,1,31,39))
#npc移动(快)
red_run_1=red.subsurface(pygame.Rect(198,1,31,39))
blue_run_1=blue.subsurface(pygame.Rect(198,1,31,39))

red_run_2=red.subsurface(pygame.Rect(231,1,31,40))
blue_run_2=blue.subsurface(pygame.Rect(231,1,31,40))

red_run_3=red.subsurface(pygame.Rect(264,1,31,39))
blue_run_3=blue.subsurface(pygame.Rect(264,1,31,39))

red_run_4=red.subsurface(pygame.Rect(297,1,31,40))
blue_run_4=blue.subsurface(pygame.Rect(297,1,31,39))

def update(npc):
	#动画参数
	anim_state='none'#动画类型
	anim_start=False#开始下一帧 bool
	anim_farme=1#总帧率
	if npc.state==None:
		#闲置状态
		npc.anim_max=1
		anim_state='none'
		anim_start=random.random()<0.6 and npc.anim>npc.anim_max
		anim_farme=2
	if npc.state=='move' and npc.speed<=0.9:
		#慢速移动状态
		npc.anim_max=0.75
		anim_state='walk'
		anim_start=((random.random()<0.8-(0.9-npc.speed)) or npc.speed<0.15) and npc.anim>npc.anim_max
		anim_farme=4
	if npc.state=='move' and npc.speed>0.9:
		#快速移动状态
		npc.anim_max=0.59
		anim_state='run'
		anim_start=((random.random()<0.8-(0.9-npc.speed)) or npc.speed<0.15) and npc.anim>npc.anim_max
		anim_farme=4
#循环动画
	if npc.side=='blue' and anim_start:
		if npc.frame<anim_farme+1 and npc.none_x==0:#正序
			npc.image=eval('blue_'+anim_state+'_'+str(npc.frame))
			npc.frame+=1
		elif npc.none_x==0:
			npc.none_x=1
		if npc.none_x==1:#反序
			npc.frame-=1
			npc.image=eval('blue_'+anim_state+'_'+str(npc.frame))
			if npc.frame==1:
				npc.none_x=0
	elif npc.side=='blue':
		a_frame=npc.frame
		if npc.frame>anim_farme:a_frame-=npc.frame-1
		npc.image=eval('blue_'+anim_state+'_'+str(a_frame))
	if npc.side=='red' and anim_start:
		if npc.frame<anim_farme+1 and npc.none_x==0:#正序
			npc.image=eval('red_'+anim_state+'_'+str(npc.frame))
			npc.frame+=1
		elif npc.none_x==0:
			npc.none_x=1
		if npc.none_x==1:#反序
			npc.frame-=1
			npc.image=eval('red_'+anim_state+'_'+str(npc.frame))
			if npc.frame==1:
				npc.none_x=0
	elif npc.side=='red':
		a_frame=npc.frame
		if npc.frame>anim_farme:a_frame-=npc.frame-1
		npc.image=eval('red_'+anim_state+'_'+str(a_frame))
#非循环动画
	









	return anim_start