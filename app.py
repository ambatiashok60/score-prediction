# Importing necessary libraries
import numpy as np
from flask import Flask, request, make_response
import json
import pickle
from flask_cors import cross_origin
from flask import jsonify

# @app.route('/')
# def index():
#     return render_template('index.html')


# @app.route('/api/say_name', methods=['POST'])
# def say_name():
#     json = request.get_json()
#     first_name = json['first_name']
#     last_name = json['last_name']
#     return jsonify(first_name=first_name, last_name=last_name)


# if __name__ == '__main__':
#     app.run(debug=True)

# Declaring the flask app
app = Flask(__name__)

# Loading the model from pickle file
model = pickle.load(open('model.pkl', 'rb'))


# geting and sending response to dialogflow
@app.route('/webhook', methods=['POST'])
def score_prediction():
    json = request.get_json()
    print(json)
    return jsonify(json)
# @cross_origin()
# def webhook():

    # req = request.get_json(silent=True, force=True)
    # res = processRequest(req)
    # res = json.dumps(res, indent=4)
    # r = make_response(res)
    # r.headers['Content-Type'] = 'application/json'
    # return r

# processing the request from dialogflow


# def processRequest(req):

#     result = req.get("queryResult")

#     # Fetching the data points
#     parameters = result.get("parameters")
#     score = parameters.get("number")
#     features = [score]

#     # Dumping the data into an array
#     final_features = [np.array(score)]

#     # Getting the intent which has fullfilment enabled
#     intent = result.get("intent").get('displayName')

#     # Fitting out model with the data points
#     if (intent == 'scorePrediction'):
#         prediction = model.predict(final_features)

#         output = round(prediction[0], 2)

#         # Returning back the fullfilment text back to DialogFlow
#         fulfillmentText = "The predicted score is {} !".format(output)
#         #log.write_log(sessionID, "Bot Says: "+fulfillmentText)
#         return {
#             "fulfillmentText": fulfillmentText
#         }


if __name__ == '__main__':
    app.run()
