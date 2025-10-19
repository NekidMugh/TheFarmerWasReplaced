
def upgradeSkill():
	hayCount = num_items(Items.Hay)
	woodCount = num_items(Items.Wood)
	carrotsCount = num_items(Items.Carrot)
	pumpkinCount = num_items(Items.Pumpkin)
	cactusCount = num_items(Items.Cactus)
	
	if(upgradeCost(Unlocks.Expand)) < pumpkinCount and upgradeCost(Unlocks.Expand) != {}:
		unlock(Unlocks.Expand)
	elif(upgradeCost(Unlocks.Pumpkins)) < carrotsCount and upgradeCost(Unlocks.Pumpkins) != {}:
		unlock(Unlocks.Pumpkins)
	elif(upgradeCost(Unlocks.Cactus)) < pumpkinCount and upgradeCost(Unlocks.Cactus) != {}:
		unlock(Unlocks.Cactus)
	elif(upgradeCost(Unlocks.Mazes)) < cactusCount and upgradeCost(Unlocks.Mazes) != {}:
		unlock(Unlocks.Cactus)
	elif(upgradeCost(Unlocks.Dinosaurs)) < cactusCount and upgradeCost(Unlocks.Dinosaurs) != {}:
		unlock(Unlocks.Cactus)
	
def upgradeCost(cost):
	cost = get_cost(cost)
	amountNeeded = 0
	for item in cost:
		amountNeeded = cost[item]
		
	return amountNeeded
