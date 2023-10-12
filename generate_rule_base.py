from model import input_lvs
from itertools import product

area = {"minimal": 0.25,
		"modest": 0.5,
		"comfortable": 0.75,
		"spacious": 1}

floor = {"lower": 0.33,
		"middle": 0.66,
		"upper": 1}

age = {"new building": 1,
		"young": 0.75,
		"middle-aged": 0.5,
		"old": 0.25}

distance = {"in the center": 1,
			"near the center": 0.75,
			"far from the center": 0.5,
			"on the outskirts": 0.25}

coef = {"Area": 0.55,
		"Floor": 0.1,
		"Аge of buildinge": 0.2,
		"Distance to the city center": 0.15}

cost = {"extremely expensive": 0.95,
		"luxurious": 0.9,
		"elite": 0.8,
		"high": 0.6,
		"average": 0.5,
		"affordable": 0.4,
		"economical": 0}


# Извлекаем имена терминов принадлежности для каждой переменной
term_names_lists = [list(var['terms'].keys()) for var in input_lvs]

# Создаем список кортежей всех возможных комбинаций
combinations = list(product(*term_names_lists))
rule_base = []
for comb in combinations:
	area_coef = area[comb[0]] * coef["Area"]
	floor_coef = floor[comb[1]] * coef["Floor"]
	age_coef = age[comb[2]] * coef["Аge of buildinge"]
	distance_coef = distance[comb[3]] * coef["Distance to the city center"]
	res = area_coef + floor_coef + age_coef + distance_coef

	for key, value in cost.items():
		if res > value:
			rule_base.append((comb, key))
			break


for rule in rule_base:
	print(str(rule) + ",")

