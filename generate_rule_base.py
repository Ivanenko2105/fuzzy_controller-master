from model import input_lvs
from itertools import product

area = {"minimal": 0,
		"modest": 0.33,
		"comfortable": 0.66,
		"spacious": 1}

floor = {"lower": 0,
		 "middle": 0.5,
		 "upper": 1}

сondition = {"new": 1,
		     "in good condition": 0.5,
		     "needs repair": 0}

distance = {"in the center": 1,
			"near the center": 0.66,
			"far from the center": 0.33,
			"on the outskirts": 0}

coef = {"Area": 0.4,
		"Floor": 0.1,
		"Condition": 0.35,
		"Distance to the city center": 0.15}

Class = {"luxurious": 0.85,
		"expensive": 0.65,
		"moderately expensive": 0.4,
		"average price": 0.25,
		"economical": 0.15,
		"budget": 0}


# Извлекаем имена терминов принадлежности для каждой переменной
term_names_lists = [list(var['terms'].keys()) for var in input_lvs]

# Создаем список кортежей всех возможных комбинаций
combinations = list(product(*term_names_lists))
rule_base = []
values = set()
for comb in combinations:
	area_coef = area[comb[0]] * coef["Area"]
	floor_coef = floor[comb[1]] * coef["Floor"]
	age_coef = сondition[comb[2]] * coef["Condition"]
	distance_coef = distance[comb[3]] * coef["Distance to the city center"]
	res = area_coef + floor_coef + age_coef + distance_coef
	values.add(res)

	for key, value in Class.items():
		if res >= value:
			rule_base.append((comb, key))
			break

# for value in sorted(values):
# 	print(value)

# print(len(values))

for rule in rule_base:
	print(str(rule) + ",")

