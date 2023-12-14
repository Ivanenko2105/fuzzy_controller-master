import model
import inference_mamdani

class FuzzyController:
	def __init__(self, relevance_level_max: float, inst_tech_level_max: float, student_satis_max: int, pp_max: float) -> None:

		self.model = model
		self.inference_mamdani = inference_mamdani
		self.real_min = 0.07516129032258065
		self.real_max = 0.9328205128205128
		self.coef = 1


		self.max_values = [relevance_level_max, inst_tech_level_max, student_satis_max, pp_max]
		self.min_values = [1, 1, 1, 1]

		self.inference_mamdani.preprocessing(self.model.input_lvs, self.model.output_lv)
	
	def __normalization(self, x, min, max) -> float:
		"""
			Normalization of the quantity x in the interval [0,1]
		"""
		return round((x - min) / (max - min), 2) * self.coef
	
	def __denormalization(self, y, min, max) -> int:
		"""
			Denormalization: from [0,1] to [Ymin, Ymax]
		"""
		coef = (max - min) / (self.real_max - self.real_min)
		return round((y - self.real_min) * coef + min, 1)
	
	def get_result(self, crisp):
		normalization_crisp = []
		for i in range(len(crisp)):
			normalization_crisp.append(self.__normalization(crisp[i], self.min_values[i], self.max_values[i]))

		result = self.inference_mamdani.process(self.model.input_lvs, self.model.output_lv, self.model.rule_base, normalization_crisp)
		denormalization_result = self.__denormalization(result[0], 1, 10)
		return (result[1], denormalization_result)

	def change_model_parameters(self, relevance_level_max, inst_tech_level_max, student_satis_max, pp_max):
		self.model = model
		self.inference_mamdani = inference_mamdani
		self.real_min = 0.07516129032258065
		self.real_max = 0.9328205128205128
		self.coef = 1

		self.max_values = [relevance_level_max, inst_tech_level_max, student_satis_max, pp_max]
		self.min_values = [1, 1, 1, 1]

		self.inference_mamdani.preprocessing(self.model.input_lvs, self.model.output_lv)