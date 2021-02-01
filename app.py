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

model_dict = joblib.load('count_vect_model.sav')

app = Flask(__name__)

# app.config['SECRET_KEY'] = 'mbti'

@app.route('/homepage', methods=['GET','POST'])
def home():
    # form = PredictorForm()

    if request.method == 'POST':
        input_one_text = form.input1.data
        input_two_text = form.input2.data
        input_three_text = form.input3.data
        input_four_text = form.input4.data
        input_five_text = form.input5.data

        predicted_value = Predict(form)

    
        return render_template('index.html', form = form, predicted=predicted_value)
    else:
        return render_template('index.html', form = form)

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

@app.route("/data", methods=['GET', 'POST'])

def Predict(honey):
    input1_df = honey.input1.data
    input2_df = honey.input2.data
    input3_df = honey.input3.data
    input4_df = honey.input4.data
    input5_df = honey.input5.data


    honey_predict_df = pd.DataFrame({
        'Input 1': [input1_df],
        'Input 2': [input2_df],
        'Input 3': [input3_df],
        'Input 4': [input4_df],
        'Input 5': [input5_df]
    })

    # hive = model_dict['model']
    # X_Scaler = model_dict['scaler']
    # predict_df_scaled = X_Scaler.transform(honey_predict_df)
    # predicted = hive.predict(predict_df_scaled)

    return predicted

if __name__ == "__main__":
    app.run(debug=True)