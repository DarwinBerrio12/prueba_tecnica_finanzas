from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)

model = joblib.load('models/model_rf.pkl')
encoder = joblib.load('models/encoder.pkl')

@app.route('/predicion', methods=['GET'])
def predicion():
    path_base = os.getcwd()
    path_data = os.path.join(path_base,'data','input','to_predict.csv')    
    data = pd.read_csv(path_data)
    data_obj = data.drop(columns=['autoID','Demand','Charges','SeniorCity','Class'])    
    feature_encode = encoder.transform(data_obj)
    feature_encode = pd.DataFrame(feature_encode, columns=data_obj.columns)

    data_model = pd.concat([data['Charges'],data['Demand'], feature_encode],axis=1)

    data_model = data_model.drop(columns=['Service1','Service2'])

    print(data_model)

    predicion = model.predict(data_model)

    return jsonify({'Predicion1': predicion[0],
                    'Predicion2': predicion[1],
                    'Predicion3': predicion[2]})

if __name__ == '__main__':
    app.run(debug=True)