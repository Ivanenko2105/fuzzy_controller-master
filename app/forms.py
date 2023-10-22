from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class RangeParameterForm(FlaskForm):
    s_max = StringField('S_max')
    s_min = StringField('S_min')
    d_max = StringField('D_max')
    f_max = StringField('F_max')
    submit = SubmitField('Submit')

class UserValueForm(FlaskForm):
    area = StringField('Area')
    floor = StringField('Floor')
    rank = StringField('Rank')
    distance = StringField('Distance')
    submit = SubmitField('Submit')