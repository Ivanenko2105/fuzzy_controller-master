import model
import inference_mamdani
import fuzzy_operators

my_area = 50
my_floor = 20
my_rank = 7
my_distance = 5

crisp = [my_area, my_floor, my_rank, my_distance]
inference_mamdani.preprocessing(model.input_lvs, model.output_lv)
result = inference_mamdani.process(model.input_lvs, model.output_lv, model.rule_base, crisp)

print(result)

for lv in model.input_lvs:
    fuzzy_operators.draw_lv(lv)
fuzzy_operators.draw_lv(model.output_lv)









