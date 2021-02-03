import flask
import re
import string
import nltk
import pandas as pd
import joblib
import pickle
from flask import Flask, render_template, jsonify, request
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, IntegerField, FloatField
from wtforms.validators import DataRequired
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

nltk.download('stopwords')

lm = WordNetLemmatizer()


class PredictorForm(FlaskForm):
    input1 = TextAreaField('Input 1', validators=[DataRequired()])
    submit = SubmitField('Submit')

# machine learning
# files = open('mbti_model.pickle', 'rb')
# model = pickle.load(files)

stopwords = nltk.corpus.stopwords.words('english')
ps = nltk.PorterStemmer()

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mbti'

@app.route('/homepage', methods=['GET','POST'])
def home():
    form = PredictorForm()

    if request.method == 'POST':
        input_one_text = form.input1.data


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


    honey_predict_df = pd.DataFrame({
        'Input 1': [input1_df]
    })

    files = open('mbti_model.pickle', 'rb')
    model = pickle.load(files)

    # def clean_posts(post):

    #     post = "".join([word.lower() for word in post if word not in string.punctuation])
    #     tokens = re.split('\W+', post)
    #     post = [ps.stem(word) for word in tokens if word not in stopwords]

    #     return post

    # cleaned_df = clean_posts(honey_predict_df)

    # # print(cleaned_df)


    # count_vectorize = CountVectorizer(analyzer = clean_posts)
    # X_count = count_vectorize.fit_transform(honey_predict_df['Input 1'])
    # X_count_feature = pd.DataFrame(X_count.toarray())

    return None

if __name__ == "__main__":
    app.run(debug=True)