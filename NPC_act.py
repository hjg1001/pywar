#NPC行为
import math,random,astar
def move_q(x, y, target_x, target_y, speed):
    dx = target_x - x
    dy = target_y - y
    distance = math.sqrt(dx**2 + dy**2)
    
    if distance <= speed:
        new_x = target_x
        new_y = target_y
    else:
        ratio = speed / distance
        new_x = x + dx * ratio
        new_y = y + dy * ratio
    
    return new_x, new_y
def angle(x,y,target_x,target_y,angle):
    dx=target_x-x
    dy=target_y-y
    angle_q = math.atan2(dx,dy)
    a=-180
    if angle_q>180:a=0
    if angle_q==180:angle_q=-(angle_q-180)
    angle_q = a+math.degrees(angle_q)
    if x==target_x and y==target_y:angle_q=angle
    return angle_q


def move(npc,map):#移动
	road_list=0
	if npc.target_x!=0 and npc.target_y!=0 and npc.angle==npc.target_angle:
		new_xy=move_q(npc.x,npc.y,npc.target_x,npc.target_y,npc.speed)
		npc.state='move'
		npc.x,npc.y=new_xy
		angle_num=angle(npc.x,npc.y,npc.target_x,npc.target_y,npc.angle)
		npc.target_angle=int(angle_num)
		if abs(npc.x-npc.target_x )<2 and abs(npc.y-npc.target_y)<2:
			npc.target_x,npc.target_y=0,0
			npc.state=None
def shoot(npc):#开火
	fire=False
	if npc.gun['ammo']==0 and npc.rifle_ammo==0:
		npc.action=None
		npc.state=None
		fire=0
	if fire==False and npc.state!='reload':
		if npc.state=='shoot':
			if npc.frame==3 and npc.anim>0.01:
				npc.state='aim'
				npc.frame=2
				npc.aim-=random.random()*0.8-0.007
				npc.action='shoot'
				npc.p=False
		if npc.aim<1 and npc.action=='shoot':
			npc.aim+=0.007
			npc.state='aim'
		elif npc.state=='aim':
			npc.state='shoot'
			if npc.gun['ammo']<=1:
				npc.state='reload'
				npc.aim=0
			npc.gun['ammo']-=1
			fire=True
	return fire
def reload(npc,map):#装弹
	clip=False
	if npc.rifle_clip<1:
 		npc.reload_time+=0.028
 		if npc.reload_time>1:
 			npc.reload_time=0
 			if npc.rifle_ammo>=1:
 				npc.rifle_ammo-=1
 				npc.gun['ammo']+=1
 				map.sound_list.append('单发装填'+str(random.randint(1,4))+'.mp3')
 			else:npc.state,npc.reload_time=None,0
	else:
 		time=0.012-npc.gun['max_ammo']*0.0008
 		if time<0.005:time=0.005
 		npc.reload_time+=time
 		if npc.reload_time>1:
 			npc.reload_time=0
 			if npc.rifle_clip>=1:
 				npc.rifle_clip-=1
 				npc.gun['ammo']=npc.gun['max_ammo']
			 	if npc.gun['type']==0:map.sound_list.append('步枪装填'+str(random.randint(1,4))+'.mp3')
			 	if npc.gun['type']==1:map.sound_list.append('手枪装填'+str(random.randint(1,4))+'.mp3')
 				clip=True
 			else:npc.state,npc.reload_time=None,0
	npc.jd,npc.max_jd=npc.reload_time*20,1*20
	if npc.gun['ammo']==npc.gun['max_ammo'] or npc.rifle_ammo==0:
 		npc.state=None
 		npc.reload_time=0
 		npc.jd,npc.max_jd=0,0
	return clip