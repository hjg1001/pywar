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
def angle(x,y,target_x,target_y):
    dx = target_x - x
    dy = target_y - y
    angle_q = math.atan2(dx,dy)
    angle_q = math.degrees(angle_q)+180
    return angle_q
def move(npc):#移动
	if npc.target_x!=0 and npc.target_y!=0 and npc.target_angle-npc.angle<1:
		new_xy=move_q(npc.x,npc.y,npc.target_x,npc.target_y,npc.speed)
		npc.state='move'
		npc.x,npc.y=new_xy
		angle_num=angle(npc.x,npc.y,npc.target_x,npc.target_y)
		if npc.target_x!=npc.x and npc.target_y!=npc.y:npc.target_angle=int(angle_num)
		else:
			npc.state=None
			npc.frame=2
			npc.target_x,npc.target_y=0,0