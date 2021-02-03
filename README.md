# AA awakening calculator

This is an Flask app that calculates awakening chances for the game Archeage/ArcheageUnchained.

Sends user input to the Flask backend route using Ajax which allows the app to calculate without refreshing page.

Stack includes:
* HTML (bootstrap forms/components)
* jQuery (AJAX form submissions)
* HTML5/wtforms form-validation
* Flask-WTF CSRF protection
* Flask post request catch/return routes


Instructions:

Online: https://aa-awakening-calculator.herokuapp.com/

Locally:

1. Create a new virtualenv, activate it and run `pip install -r requirements.txt`.

2. Run the app: `python awkcalc.py`

3. Open your browser to http://127.0.0.1:5000 to view the app.

The `awkcalc.py` file contains all python code, and the frontend code for the jQuery version is contained in the `templates/base.html` file.
