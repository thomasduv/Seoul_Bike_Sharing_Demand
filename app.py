from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json
import pandas as pd


app = Flask(__name__)


@app.route('/api/', methods=['POST'])
def makecalc():
    data = request.get_json()
    df = pd.DataFrame(data, columns=['Hour','Temperature(C)','Humidity(%)','Wind speed (m/s)','Visibility (10m)','Dew point temperature(C)','Solar Radiation (MJ/m2)','Rainfall(mm)','Snowfall (cm)','Year','Month','Day','Seasons_id','Holiday_id','FunctioningDay_id','Day_of_Week_id'])
    prediction = np.array2string(model.predict(df))

    return jsonify(prediction)

if __name__ == '__main__':
    modelfile = 'xgbmodel.pickle'
    model = p.load(open(modelfile, 'rb'))
    app.run(debug=True, host='0.0.0.0')