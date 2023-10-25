#NPC行为
import math,random
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
    return angle_q
def move(npc):#移动
	if npc.target_x!=0 and npc.target_y!=0 and abs(npc.target_angle-npc.angle)<1:
		new_xy=move_q(npc.x,npc.y,npc.target_x,npc.target_y,npc.speed)
		npc.state='move'
		npc.x,npc.y=new_xy
		angle_num=angle(npc.x,npc.y,npc.target_x,npc.target_y,npc.angle)
		if npc.target_x!=npc.x and npc.target_y!=npc.y and npc.target_angle==npc.angle:
			npc.target_angle=int(angle_num)
		else:
			npc.state=None
			npc.frame=2
			npc.target_x,npc.target_y=0,0
def shoot(npc):#开火
	fire=False
	if npc.gun['ammo']==0 and npc.rifle_ammo==0:
		npc.action=None
		npc.state=None
		fire=0
	if fire==False and npc.state!='reload':
		if npc.state=='shoot':
			if npc.frame==2 and npc.anim>0.15:
				npc.state=None
				npc.aim=0
				npc.action=None
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
 				map.sound_list.append('单发装填.wav')
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
 				map.sound_list.append('步枪装填.wav')
 				clip=True
 			else:npc.state,npc.reload_time=None,0
	npc.jd,npc.max_jd=npc.reload_time*20,1*20
	if npc.gun['ammo']==npc.gun['max_ammo'] or npc.rifle_ammo==0:
 		map.sound_list.append('上膛.wav')
 		npc.state=None
 		npc.reload_time=0
 		npc.jd,npc.max_jd=0,0
	return clip