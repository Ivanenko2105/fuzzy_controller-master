from fuzzy_controller import FuzzyController

if __name__=="__main__":
	S_max = 100	# max area
	S_min = 20	# min area
	D_max = 10	# max distance
	F_max = 20	# max floors

	my_controller = FuzzyController(S_max, S_min, F_max, D_max)

	my_area = 50
	my_floor = 20
	my_rank = 7
	my_distance = 5

	crisp = [my_area, my_floor, my_rank, my_distance]

	result = my_controller.get_result(crisp)

	print(result)
