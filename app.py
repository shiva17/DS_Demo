import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
# # takes 3 params

# @app.route('/')
# def home():
#     """
#     Uses GET Method
#     """
#     result_dic = {}
#     input_data = request.args.get('input')
#     ls_data = eval(input_data)

#     prediction = model.predict([np.array(ls_data)])
#     output = prediction[0]
#     result_dic["Input"] = ls_data
#     result_dic["Predictes Salary"] = output
#     return jsonify(result_dic)


@app.route('/hello')
def hello():
    return("hello")

# # =============================================================================

# @app.route('/predict_api',methods=['POST'])
# def predict_api():
#     """
#     Uses POST Method
#     """
#     ls_data = request.get_json(force=True)
#     print(ls_data)
#     prediction = model.predict([np.array(ls_data)])

#     output = prediction[0]
#     return jsonify(output)
# # =============================================================================

if __name__ == "__main__":
    app.run(debug=True)
