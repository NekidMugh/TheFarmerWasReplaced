import customDef
import upgrade

clear()

while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			#do a flip on every tile
			#harvest()
			customDef.greatPumpkin()

			if(get_pos_y() == get_world_size() - 1):
				upgrade.upgradeSkill()
				move(East)
			
			if(get_water() <= 1):
				use_item(Items.Water)
			#use_item(Items.Fertilizer)
			#use_item(Items.Weird_Substance)
			move(North)
