import joblib
from flask import Flask, render_template, request
import preprocess
import numpy as np
import pandas as pd

app = Flask(__name__)

scaler = joblib.load('Models/scaler.h5')
model = joblib.load('Models/model.h5')

cols_xg = model.get_booster().feature_names


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST', 'GET'])
def get_prediction():

    if request.method == 'POST':
        age = np.int64(request.form['age'])
        campaign = np.int64(request.form['campaign'])
        pdays = np.int64(request.form['pdays'])
        previous = np.int64(request.form['previous'])
        cons_price_idx = np.float64(request.form['cons.price.idx'])
        cons_conf_idx = np.float64(request.form['cons.conf.idx'])
        euribor3m = np.float64(request.form['euribor3m'])
        job = request.form['job']
        marital = request.form['marital']
        education = request.form['education']
        credit = request.form['credit']
        housing = request.form['housing']
        loan = request.form['loan']
        contact = request.form['contact']
        season = request.form['season']
        outcome = request.form['outcome']

    data = {'age': age, 'campaign': campaign, 'pdays': pdays,
            'previous': previous, 'cons_price_idx': cons_price_idx,
            'cons_conf_idx': cons_conf_idx, 'euribor3m': euribor3m,
            'job': job, 'marital': marital, 'education': education, 'credit': credit,
            'housing': housing, 'loan': loan, 'contact': contact,
            'season': season, 'outcome': outcome}
    print(data)

    final_data = preprocess.preprocess_data(data)
    print(final_data)
    scaled = scaler.transform([final_data])


    scaled_df = pd.DataFrame(scaled, columns=cols_xg)
    prediction = model.predict(scaled_df)[0]
   
    # return str(round(prediction))
    return render_template('prediction.html', td_predict=str(round(prediction)))


if __name__ == '__main__':
    app.run(debug=True)
