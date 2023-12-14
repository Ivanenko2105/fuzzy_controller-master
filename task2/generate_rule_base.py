from model import input_lvs
from itertools import product

relevance_level = {
		"irrelevant": 0,
		"low relevant": 0.4,
		"possible": 0.7,
		"overwhelming": 1}

institution_technical_level = {
		"miserable": 0,
		"below middle": 0.33,
		"satisfying": 0.66,
		"positive": 1}

student_satisfaction = {
			"low": 0,
			"poor": 0.2,
			"avarage": 0.6,
			"high": 1}

program_propensity = {
			"small": 0,
			"median": 0.66,
			"towering": 1}

coef = {"relevance_level": 0.4,
		"institution_technical_level": 0.1,
		"student_satisfaction": 0.35,
		"program_propensity": 0.15}

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
	a = relevance_level[comb[0]] * coef["relevance_level"]
	b = institution_technical_level[comb[1]] * coef["institution_technical_level"]
	c = student_satisfaction[comb[2]] * coef["student_satisfaction"]
	d = program_propensity[comb[3]] * coef["program_propensity"]
	res = a + b + c + d
	values.add(res)

	for key, value in Class.items():
		if res >= value:
			keys.append(key)
			rule_base.append((comb, key))
			break


for rule in rule_base:
	print(str(rule) + ",")

