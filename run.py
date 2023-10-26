from tkinter import NO
from flask import Flask, render_template, redirect, url_for, request, session, abort
from fuzzy_controller import FuzzyController

app = Flask(__name__)

app.config['SECRET_KEY'] = 'info-pass-secret-key'

flags = {'ranges_block_flag': True,
		 'user_values_block_flag': True, 
		 'result_block_flag': True}

range_values = {'s_max': 0,
				's_min': 0,
				'd_max': 0,
				'f_max': 0}

my_controller = FuzzyController(10,10,10,10)

@app.route('/', methods=['POST','GET'])
def index():
	global range_values, my_controller, flags
	
	if "change-rp_form" in request.form:
		for i in flags:
			flags[i] = True

		return render_template('index.html', flags=flags, range_values=range_values)
	
	elif "submit-rp_form" in request.form and flags['ranges_block_flag']:
		
		flags['ranges_block_flag'] = False
		
		for v in range_values:
			range_values[v] = request.form.get(v, 1, type=int)
	
		try:
			my_controller.change_model_parameters(
				range_values['s_max'], 
				range_values['s_min'], 
				range_values['d_max'], 
				range_values['f_max'])
		except BaseException as err:			
			print(f'Error: {err}')

		return render_template('index.html', flags=flags, range_values=range_values)

	elif "submit-uv_form" in request.form:
		
		for i in flags:
			flags[i] = False
		
		area = request.form.get('area', 1, type=int)
		floor = request.form.get('floor', 1, type=int)
		rank = request.form.get('rank', 1, type=int)
		distance = request.form.get('distance', 1, type=int)

		crisp = [area, floor, rank, distance]
		result = my_controller.get_result(crisp)
		
		return render_template('index.html', flags=flags, range_values=range_values, result=result)
	
	return render_template('index.html', flags=flags, range_values=range_values)


if __name__=="__main__":
	app.run(debug=True)
