from model_2 import input_lvs
from itertools import product

area = {"Very small": 0,
		"Small": 0.2,
		"Average": 0.4,
		"Large": 0.6,
		"Very large": 0.8,
		"Extra large": 1}

floor = {"Lower": 0,
		 "Below middle": 0.33,
		 "Above middle": 0.66,
		 "Upper": 1}

сondition = {"Very poor": 0,
			 "Poor": 0.2,
			 "Average": 0.4,
			 "Good": 0.6,
			 "Very good": 0.8,
			 "Excellent": 1}

distance = {"in the center": 1,
			"near the center": 0.66,
			"far from the center": 0.33,
			"on the outskirts": 0}

coef = {"Area": 0.4,
		"Floor": 0.1,
		"Condition": 0.35,
		"Distance to the city center": 0.15}

Class = {"Extremely high": 0.736,
	     "Very high": 0.623,
		 "High": 0.543,
		 "Average": 0.46,
		 "Favorable": 0.379,
		 "Low": 0.2695,
		 "Very low": 0}


# Извлекаем имена терминов принадлежности для каждой переменной
term_names_lists = [list(var['terms'].keys()) for var in input_lvs]

# Создаем список кортежей всех возможных комбинаций
combinations = list(product(*term_names_lists))
rule_base = []
values = set()
keys = []
for comb in combinations:
	area_coef = area[comb[0]] * coef["Area"]
	floor_coef = floor[comb[1]] * coef["Floor"]
	age_coef = сondition[comb[2]] * coef["Condition"]
	distance_coef = distance[comb[3]] * coef["Distance to the city center"]
	res = area_coef + floor_coef + age_coef + distance_coef
	values.add(res)

	for key, value in Class.items():
		if res >= value:
			keys.append(key)
			rule_base.append((comb, key))
			break

# set_key = set(keys)

# for key in set_key:
# 	print(key, "-", keys.count(key))

# i = 0
# for value in sorted(values):
# 	i = i + 1
# 	if i == 70:
# 		print(value)
# 		i = 0

for value in sorted(values):
	print(value)

# print(len(values))

# for rule in rule_base:
# 	print(str(rule) + ",")

# print(len(rule_base))
