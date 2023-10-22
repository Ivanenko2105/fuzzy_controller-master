from flask import Flask, render_template, redirect, url_for, request, session, abort
from fuzzy_controller import FuzzyController


app = Flask(__name__)
app.config['SECRET_KEY'] = 'info-pass-secret-key'

@app.route('/', methods=['GET', 'POST'])
def index():
	my_controller = FuzzyController(10,10,10,10)
	if "submit-rp_form" in request.form:
		s_max = request.form.get('s_max',0)
		s_min = request.form.get('s_min',0)
		d_max = request.form.get('d_max',0)
		f_max = request.form.get('f_max',0)
		my_controller = FuzzyController(s_max, s_min, f_max, d_max)

	elif "submit-uv_form" in request.form:
		area = request.form.get('area',0)
		floor = request.form.get('floor',0)
		rank = request.form.get('rank',0)
		distance = request.form.get('distance',0)
		
		crisp = [area, floor, rank, distance]
		result = my_controller.get_result(crisp)
	
	return render_template('index.html', result=result)


if __name__=="__main__":
	app.run(debug=True)
	
	# S_max = 100	# max area
	# S_min = 20	# min area
	# D_max = 10	# max distance
	# F_max = 20	# max floors

	# 

	# my_area = 50
	# my_floor = 20
	# my_rank = 7
	# my_distance = 5

	# 

	# 
