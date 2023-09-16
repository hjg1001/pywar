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
#npc走路(慢)
red_walk_1=red.subsurface(pygame.Rect(66,1,31,39))
blue_walk_1=blue.subsurface(pygame.Rect(66,1,31,39))

red_walk_2=red.subsurface(pygame.Rect(99,1,31,40))
blue_walk_2=blue.subsurface(pygame.Rect(99,1,31,40))

red_walk_3=red.subsurface(pygame.Rect(132,1,31,39))
blue_walk_3=blue.subsurface(pygame.Rect(132,1,31,39))

red_walk_4=red.subsurface(pygame.Rect(165,1,31,40))
blue_walk_4=blue.subsurface(pygame.Rect(165,1,31,39))


def update(npc):
	frame_old=npc.frame
	update_image=False
	if npc.state==None and (random.random()+random.random()<setting.npc_none or npc.none_anim):#闲置
		npc.none_anim=True
		if npc.side=='blue' and random.random()+random.random()<setting.npc_none_speed:
			if npc.frame<3 and npc.none_x==0:#正序
				npc.image=eval('blue_none_'+str(npc.frame))
				npc.frame+=1
			elif npc.none_x==0:
				npc.none_x=1
			if npc.none_x==1:#反序
				npc.frame-=1
				npc.image=eval('blue_none_'+str(npc.frame))
				if npc.frame==1:
					npc.none_x=0
					npc.none_anim=False
		elif npc.side=='red' and random.random()+random.random()<setting.npc_none_speed:
			if npc.frame<3 and npc.none_x==0:#正序
				npc.image=eval('red_none_'+str(npc.frame))
				npc.frame+=1
			elif npc.none_x==0:
				npc.none_x=1
			if npc.none_x==1:#反序
				npc.frame-=1
				npc.image=eval('red_none_'+str(npc.frame))
				if npc.frame==1:
					npc.none_x=0
					npc.none_anim=False
	elif npc.state=='move':
		npc.none_anim=True
		if npc.side=='blue' and random.random()+random.random()<setting.walk_p:
			if npc.frame<5 and npc.none_x==0:#正序
				npc.image=eval('blue_walk_'+str(npc.frame))
				npc.frame+=1
			elif npc.none_x==0:
				npc.none_x=1
			if npc.none_x==1:#反序
				npc.frame-=1
				npc.image=eval('blue_walk_'+str(npc.frame))
				if npc.frame==1:
					npc.none_x=0
					npc.none_anim=False
		elif npc.side=='red' and random.random()+random.random()<setting.walk_p+0.1*npc.speed:
			if npc.frame<5 and npc.none_x==0:#正序
				npc.image=eval('red_walk_'+str(npc.frame))
				npc.frame+=1
			elif npc.none_x==0:
				npc.none_x=1
			if npc.none_x==1:#反序
				npc.frame-=1
				npc.image=eval('red_walk_'+str(npc.frame))
				if npc.frame==1:
					npc.none_x=0
					npc.none_anim=False
	if npc.frame!=frame_old:
		update_image=True
	return  update_image