import model
import model_2
import inference_mamdani
import t2_mandani_inference
import fuzzy_operators
import random

choose_model = 2

if choose_model == 1:
	my_area = 50
	my_floor = 20
	my_rank = 7
	my_distance = 5

	crisp = [my_area, my_floor, my_rank, my_distance]
	inference_mamdani.preprocessing(model.input_lvs, model.output_lv)
	result = inference_mamdani.process(model.input_lvs, model.output_lv, model.rule_base, crisp)

	print(result)

	# for lv in model.input_lvs:
	# 	fuzzy_operators.draw_lv(lv)
	fuzzy_operators.draw_lv(model.output_lv)

else:
	t2_mandani_inference.preprocessing(model_2.input_lvs, model_2.output_lv)

	for _ in range(100):
		crisp_values = (random.randint(17, 100), random.randint(130, 200), random.randint(15, 50), random.randint(1000, 50000))
		result = t2_mandani_inference.process(model_2.input_lvs, model_2.output_lv, model_2.rule_base, crisp_values)
		print(result)







