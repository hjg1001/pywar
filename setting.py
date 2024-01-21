#--窗口设定--
import random,text,math
width,height=720,1600#窗口大小
map_w,map_h=180,230#小地图大小
m_p=(30,1210)#小地图坐标
alpha=90#不透明度
npc_info_list=['x','y','road','state','action','move_q','debug_cmd','target_angle','angle','gun','rifle_ammo','rifle_clip','team','job_text']#左上角显示/可修改的NPC数据


#--对局设定--
tree_num=[2,2]#多少树 树太多会一直找不到落脚点
flag_num=4#旗帜数量(未占点)
 #蓝队
npc_blue_num=10#蓝队npc数量
blue_team=2#编队数量
blue_team_num=5#一个编队最少人数
if blue_team*blue_team_num>npc_blue_num:npc_blue_num=blue_team*blue_team_num
blue_team_s0=[1,6]#步枪手人数
blue_team_s1=[1,2]#军官人数
blue_team_lv=0.5#士兵作战水平差距
blue_K=['2','1','0','0','0']#总指挥的编队 独立于其他编队
npc_blue_num+=len(blue_K)
blue_team_pistol={'type':1,'name':str(random.choice(text.pistol2))+'\''+str(random.choice(text.pistol))+'\''+'  手枪','ammo':10,'max_ammo':10}#手枪
blue_team_rifle={'type':0,'name':str(random.choice(text.rifle))+'步枪','ammo':10,'max_ammo':10}#步枪
if blue_team*blue_team_num<npc_blue_num-len(blue_K):
	t=math.ceil((npc_blue_num-len(blue_K)-blue_team*blue_team_num)/blue_team_num)
	blue_team+=t
blueK=0#开局的点数
blue_command=[]#队伍命令
 #红队
npc_red_num=10#npc数量
red_team=2#编队数量
red_team_num=5#一个编队最少人数
if red_team*red_team_num>npc_red_num:npc_red_num=red_team*red_team_num
red_team_s0=[1,6]#步枪手人数
red_team_s1=[1,2]#军官人数
red_team_lv=0.5#士兵作战水平差距
red_K=['2','1','0','0','0']#总指挥的编队 独立于其他编队
npc_red_num+=len(red_K)
red_team_pistol={'type':1,'name':str(random.choice(text.pistol2))+'\''+str(random.choice(text.pistol))+'\''+'  手枪','ammo':10,'max_ammo':10}#手枪
red_team_rifle={'type':0,'name':str(random.choice(text.rifle))+'步枪','ammo':10,'max_ammo':10}#步枪
if red_team*red_team_num<npc_red_num-len(red_K):
	t=math.ceil((npc_red_num-len(red_K)-red_team*red_team_num)/red_team_num)
	red_team+=t
redK=0#开局的点数

#--生成模式设定--
mapw,maph=3000,3000#大地图大小
min,max=-100,100#NPC生成在队友周围的范围
tree_x,tree_y=30,30#树之间的横纵距离


#--图形--
fps=60#帧率
anim_speed=0.016#动画速度
jd=True#NPC旁边的进度条
smoke=0.4#枪口烟雾概率
#--文本--
job=['步枪手','军官','总指挥']#职位