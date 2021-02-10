# /models/form.py

from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import InputRequired, NumberRange

class MyForm(FlaskForm):
    awk = IntegerField(label=('Initial awakening chance?'),
                        validators=[InputRequired(),
                        NumberRange(min=0, max=100, message='Awakening must be an integer between %(min)s and %(max)s!')])
    fail = IntegerField(label=('Fail stack bonus percent?'),
                        validators=[InputRequired(), NumberRange(min=0, max=25, message='Fail stacks must be an integer between %(min)s and %(max)s!')])
    suc = IntegerField(label=('Desired success chance?'),
                        validators=[InputRequired(), NumberRange(min=0, max=100, message='Desired chance must be an integer between %(min)s and %(max)s!')])
