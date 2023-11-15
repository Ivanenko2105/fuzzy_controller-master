import model, model_2
import inference_mamdani, t2_mandani_inference

class FuzzyController:
	def __init__(self, chosen_model, S_max: float, S_min: float, F_max: int, D_max: float) -> None:
		"""
			S_max - max area of flat for a city
			S_min - min area of flat for a city
			D_max - max distance from the city center to a flat
			F_max - max floors in buildings for a city 
		"""
		if chosen_model == 1:
			self.model = model
			self.inference_mamdani = inference_mamdani
			self.real_min = 0.07516129032258065
			self.real_max = 0.9328205128205128
			self.coef = 1
		else:
			self.model = model_2
			self.inference_mamdani = t2_mandani_inference
			self.real_min = 0.4387793427230046
			self.real_max = 9.218827404479581
			self.coef = 10

		self.max_values = [S_max, F_max, 10, D_max]
		self.min_values = [S_min, 1, 1, 0]

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

	def change_model_parameters(self, chosen_model, S_max: float, S_min: float, F_max: int, D_max: float):
		if chosen_model == 1:
			self.model = model
			self.inference_mamdani = inference_mamdani
			self.real_min = 0.07516129032258065
			self.real_max = 0.9328205128205128
			self.coef = 1
		else:
			self.model = model_2
			self.inference_mamdani = t2_mandani_inference
			self.real_min = 0.4387793427230046
			self.real_max = 9.218827404479581
			self.coef = 10

		self.max_values = [S_max, F_max, 10, D_max]
		self.min_values = [S_min, 1, 1, 0]

		self.inference_mamdani.preprocessing(self.model.input_lvs, self.model.output_lv)