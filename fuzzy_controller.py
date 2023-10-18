import model
import inference_mamdani


class FuzzyController:
	def __init__(self, S_max: float, S_min: float, F_max: int, D_max: float) -> None:
		"""
			S_max - max area of flat for a city
			S_min - min area of flat for a city
			D_max - max distance from the city center to a flat
			F_max - max floors in buildings for a city 
		"""
		self.max_values = [S_max, F_max, 10, D_max]
		self.min_values = [S_min, 1, 1, 0]

		inference_mamdani.preprocessing(model.input_lvs, model.output_lv)
	
	def __normalization(self, x, min, max) -> float:
		"""
			Normalization of the quantity x in the interval [0,1]
		"""
		return round((x - min) / (max - min), 2)
	
	def __denormalization(self, y, min, max) -> int:
		"""
			Denormalization: from [0,1] to [Ymin, Ymax]
		"""
		coef = (max - min) / (0.9328205128205128 - 0.07516129032258065)
		return round((y - 0.07516129032258065) * coef + min)
	
	def get_result(self, crisp):
		normalization_crisp = []
		for i in range(len(crisp)):
			normalization_crisp.append(self.__normalization(crisp[i], self.min_values[i], self.max_values[i]))

		result = inference_mamdani.process(model.input_lvs, model.output_lv, model.rule_base, normalization_crisp)
		denormalization_result = self.__denormalization(result[0], 1, 10)
		return (result[1], denormalization_result)

	def change_model_parameters(self, S_max: float, S_min: float, F_max: int, D_max: float):
		self.max_values = [S_max, F_max, 10, D_max]
		self.min_values = [S_min, 1, 1, 0]