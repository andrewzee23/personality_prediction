import flask
from flask import Flask, render_template, jsonify, request
# from flask_wtf import FlaskForm
# from wtforms import SubmitField, TextAreaField, IntegerField, FloatField
# from wtforms.validators import DataRequired

# class PredictorForm(FlaskForm):
#     input1 = IntegerField('Input 1', validators=[DataRequired()])
#     input2 = IntegerField('Input 2', validators=[DataRequired()])
#     input3 = FloatField('Input 3', validators=[DataRequired()])
#     input4 = FloatField('Input 4', validators=[DataRequired()])
#     input5 = IntegerField('Input 5', validators=[DataRequired()])
#     submit = SubmitField('Submit')

app = Flask(__name__)

# app.config['SECRET_KEY'] = 'mbti'

@app.route('/homepage', methods=['GET','POST'])
def home():
    # form = PredictorForm()

    return render_template('index.html')
    #return render_template('index.html', form=form)

@app.route('/visuals')
def visuals():

    return render_template('visuals.html')

@app.route('/contact')
def contacts():

    return render_template('contact.html')

@app.route('/data1')
def data1():
    # use these for json data
    return None

@app.route('/data2')
def data2():
    # use these for json data
    return None

@app.route('/data3')
def data3():
    # use these for json data
    return None

if __name__ == "__main__":
    app.run(debug=True)