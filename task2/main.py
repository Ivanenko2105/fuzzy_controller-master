from fuzzy_controller import FuzzyController

relevance_level_max = 50
inst_tech_level_max = 12
student_satis_max = 20
pp_max = 15

Controller = FuzzyController(relevance_level_max, inst_tech_level_max, student_satis_max, pp_max)


relevance_level = 40
institution_technical_level = 8
student_satisfaction = 7
program_propensity = 15

crisp = [
    relevance_level, 
    institution_technical_level, 
    student_satisfaction, 
    program_propensity]


result = Controller.get_result(crisp)

print(result)