# AA awakening calculator

This is an Flask app that calculates awakening chances for the game Archeage/ArcheageUnchained.

Sends user input to the Flask backend route using Ajax which allows the app to calculate without refreshing page.

Stack includes:
* HTML (bootstrap forms/components)
* jQuery (AJAX form submissions)
* HTML5/wtforms form-validation
* Flask-WTF CSRF protection
* Flask post request catch/return routes

The `awkcalc.py` file contains all python code, and the frontend code for the jQuery version is contained in the `templates/base.html` file.
Instructions:

Online: https://aa-awakening-calculator.herokuapp.com/

Local development server:

1. Create a new virtualenv, activate it and run `pip install -r requirements.txt`.

2. Run the app: `python awkcalc.py`

3. Open your browser to localhost:5000 to view the app.

Local production server (gunicorn):

1. Make sure Docker is installed

2. 'docker-compose build'

3. 'docker-compose up -d'

4. Open your browser to localhost:5004 to view the app.
