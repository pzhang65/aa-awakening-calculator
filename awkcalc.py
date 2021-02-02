from flask import Flask, render_template, redirect, jsonify, session
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from flask_wtf.csrf import CsrfProtect
from wtforms.validators import ValidationError, InputRequired, NumberRange


class Config:
    SECRET_KEY = '11122233344'


app = Flask(__name__)
app.config.from_object(Config)
CsrfProtect(app)


class MyForm(FlaskForm):
    awk = IntegerField(label=('What is the initial awakening chance?'),
                        validators=[InputRequired(), NumberRange(min=0, max=100, message='Percent must be an integer between 0 and 100!')])
    fail = IntegerField(label=('Fail stack bonus percent?'),
                        validators=[InputRequired(), NumberRange(min=0, max=100, message='Percent must be an integer between 0 and 100!')])
    suc = IntegerField(label=('Desired success chance?'),
                        validators=[InputRequired(), NumberRange(min=0, max=100, message='Percent must be an integer between 0 and 100!')])


@app.route('/', endpoint='home', methods=['GET', 'POST'])
def home():
    form = MyForm()
    return render_template('home.html', form=form)

@app.route('/calculate', methods=['POST'])
def calculate():
    form = MyForm()

    #assign form data from POST
    awk = form.awk.data/100
    fail = form.fail.data/100
    suc = form.suc.data/100

    #calculate attempts
    attempts=1
    cur_awk = awk
    awk_list = []
    while cur_awk <= suc:
        cur_awk=1-((1-cur_awk)*(1-(awk+attempts*fail)))
        attempts += 1
        #append tuple values to awk_list
        awk_list.append((attempts,cur_awk*100))

    #unzips tuples into two list, first being # of attempts, second being awakening percent
    atmpt_lst, per_lst = zip(*awk_list)
    atmpt1=atmpt_lst[-1]
    atmpt2=atmpt_lst[-2]
    per1=round(per_lst[-1],2)
    per2=round(per_lst[-2],2)
    if form.validate_on_submit():
        return jsonify({ 'success': True,
            'message': (f"You will need: {atmpt1} attempts --> To awaken with: {per1} % chance"),
            'message2':(f"You will need: {atmpt2} attempts --> To awaken with: {per2} % chance") })

    return jsonify({'success': False,
                    'message': 'Error - Invalid submission'})


if __name__ == '__main__':
    app.run(debug=True)
