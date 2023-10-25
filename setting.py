#--窗口设定--
width,height=720,1600#窗口大小
map_w,map_h=180,230#小地图大小
m_p=(30,1210)#小地图坐标
alpha=90#不透明度
npc_info_list=['speed','side','state','action','anim','debug_cmd','target_angle','angle','gun','rifle_ammo','rifle_clip']#左上角显示/可修改的NPC数据


#--对局设定--
tree_num=[5,6]#多少树 树太多会一直找不到落脚点
npc_blue_num=5#蓝队npc数量
npc_red_num=5#红队npc数量



#--生成模式设定--
min,max=-540,500#NPC生成在队友周围的范围
tree_x,tree_y=30,30#树之间的横纵距离


#--图形--
fps=80#帧率
anim_speed=0.016#动画速度
jd=True#NPC旁边的进度条