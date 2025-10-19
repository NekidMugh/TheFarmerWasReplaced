def is_even(n):
	return n % 2 == 0

def tree_pumpkin():
	harvest()
	if is_even(get_pos_y()) and is_even(get_pos_x()):
		plant(Entities.Tree)
	elif is_even(get_pos_x()) and is_even(get_pos_y() == False):
		till()
		plant(Entities.Carrot)
	elif is_even(get_pos_x() == False) and is_even(get_pos_y()):
		till()
		plant(Entities.Sunflower)
	else:
		till()
		plant(Entities.Pumpkin)

def greatPumpkin():
	if(get_pos_x() < 6) and (get_pos_y() < 6):
		harvest()
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Pumpkin)
	elif(get_pos_x() >= 6) and (get_pos_x() < 12) and (get_pos_y() < 6):
		harvest()
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Cactus)
	else:
		tree_pumpkin()
