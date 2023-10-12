import model
import inference_mamdani
import fuzzy_operators

crisp = [90, 3, 2, 7]
inference_mamdani.preprocessing(model.input_lvs, model.output_lv)
result = inference_mamdani.process(model.input_lvs, model.output_lv, model.rule_base, crisp)

print(result)

for lv in model.input_lvs:
    fuzzy_operators.draw_lv(lv)
fuzzy_operators.draw_lv(model.output_lv)









