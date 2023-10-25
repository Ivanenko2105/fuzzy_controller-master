from tkinter import NO
from flask import Flask, render_template, redirect, url_for, request, session, abort
from fuzzy_controller import FuzzyController

app = Flask(__name__)

app.config['SECRET_KEY'] = 'info-pass-secret-key'

flags = {'ranges_block_flag': True,
		 'user_values_block_flag': True, 
		 'result_block_flag': True}

range_values = {}
my_controller = FuzzyController(10,10,10,10)

@app.route('/', methods=['POST','GET'])
def index():
	global range_values, my_controller, flags
	
	if "change-rp_form" in request.form:
		for i in flags:
			flags[i] = True

		return render_template('index.html', flags=flags, result=None)
	
	elif "submit-rp_form" in request.form and flags['ranges_block_flag']:
		
		range_values['s_max'] = request.form.get('s_max',0, type=int)
		range_values['s_min'] = request.form.get('s_min',0, type=int)
		range_values['d_max'] = request.form.get('d_max',0, type=int)
		range_values['f_max'] = request.form.get('f_max',0, type=int) 
	
		flags['ranges_block_flag'] = False
		try:
			my_controller.change_model_parameters(range_values['s_max'], range_values['s_min'], range_values['d_max'], range_values['f_max'])
		except BaseException as err:			
			print(f'++++++++++++\n{err}')


		return render_template('index.html', flags=flags, range_values=range_values, result=None)

	elif "submit-uv_form" in request.form:
		area = int(request.form.get('area',0))
		floor = int(request.form.get('floor',0))
		rank = int(request.form.get('rank',0))
		distance = int(request.form.get('distance',0))
		
		flags['user_values_block_flag'] = False
		flags['result_block_flag'] = False

		crisp = [area, floor, rank, distance]
		result = my_controller.get_result(crisp)
		
		return render_template('index.html', flags=flags, range_values=range_values, result=result)
	
	return render_template('index.html', flags=flags, range_values=range_values, result=None)


if __name__=="__main__":
	app.run(debug=True)
