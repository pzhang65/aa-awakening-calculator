from flask import Flask, render_template, redirect, jsonify, session
from flask_wtf import FlaskForm
from wtforms import IntegerField
from flask_wtf.csrf import CsrfProtect
from wtforms.validators import InputRequired, NumberRange


class Config:
    SECRET_KEY = '11122233344'


app = Flask(__name__)
app.config.from_object(Config)
CsrfProtect(app)


class MyForm(FlaskForm):
    awk = IntegerField(label=('Initial awakening chance? [0-100]'),
                        validators=[InputRequired(),
                        NumberRange(min=0, max=100, message='awakening must be an integer between %(min)s and %(max)s!')])
    fail = IntegerField(label=('Fail stack bonus percent? [0-25]'),
                        validators=[InputRequired(), NumberRange(min=0, max=25, message='fail stacks must be an integer between %(min)s and %(max)s!')])
    suc = IntegerField(label=('Desired success chance? [0-100]'),
                        validators=[InputRequired(), NumberRange(min=0, max=100, message='success chance must be an integer between %(min)s and %(max)s!')])


@app.route('/', endpoint='home', methods=['GET', 'POST'])
def home():
    form = MyForm()
    return render_template('home.html', form=form)

@app.route('/calculate', methods=['POST'])
def calculate():
    form = MyForm()
    #initialize error list to store errors
    err_list = []

    if form.validate_on_submit():
        #assign form data from POST
        awk = form.awk.data/100
        fail = form.fail.data/100
        suc = form.suc.data/100

        #user desired success cannot be lower than one single attempt
        if suc < awk:
            return jsonify({'success': False,
                            'message': 'Error - Desired success chance cannot be lower than initial awakening chance!'})
        #calculate attempts
        attempts=1
        cur_awk = awk
        awk_list = []
        while cur_awk <= suc:
            cur_awk=1-((1-cur_awk)*(1-(awk+attempts*fail)))
            attempts += 1
            awk_list.append((attempts,cur_awk*100))

        #unzips tuples into two list, first being # of attempts, second being awakening percent
        atmpt_lst, per_lst = zip(*awk_list)

        atmpt1=atmpt_lst[-1]
        per1=round(per_lst[-1],2)

        #atmpt_lst will only have attempts past the first attempt, therefore first attempt is not added to list
        try:
            #try to give two attempts to users near their desired success rate, if only two attempts required then first attempt won't be in list
            atmpt2=atmpt_lst[-2]
        except IndexError:
            return jsonify({ 'success': True,
                            'message': (f"You will need: {atmpt1} attempts --> To awaken with: {per1} % chance"),
                            'message2':(f"You will need: 1 attempts --> To awaken with: {awk*100} % chance") })

        per2=round(per_lst[-2],2)

        return jsonify({ 'success': True,
                        'message': (f"You will need: {atmpt1} attempts --> To awaken with: {per1} % chance"),
                        'message2':(f"You will need: {atmpt2} attempts --> To awaken with: {per2} % chance") })

    for fieldName, errorMessages in form.errors.items():
        for err in errorMessages:
            err_list.append(err)

    return jsonify({'success': False,
                    'message': (f"Error! {' '.join(err_list)}")})


if __name__ == '__main__':
    app.run()
