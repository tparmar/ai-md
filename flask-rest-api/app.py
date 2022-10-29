# from dataclasses import field
from flask import Flask, render_template, request
from flask_restx import Resource, Api
from flask_restx import reqparse
from load_models import *
from flask_restx import fields
from flask_cors import CORS

import json
app = Flask(__name__)
api= Api(app, title='AI Medical Diagnosis', description="Api to predict diseases using user symptoms")
cors = CORS(app, resources={r"/*": {"origins": "*"}})

ns = api.namespace('get-symptoms', 
                   description='Get request for symptoms')

ns2 = api.namespace('predict-diseases', 
                   description='Predict disease using user input')

# class DictItem(fields.Raw):
#     def output(self, key, obj, *args, **kwargs):
#         try:
#             dct = getattr(obj, self.attribute)
#         except AttributeError:
#             return {}
#         return dct or {}


predict_model = api.model('Predict_model', {
    'symptoms': fields.String(required=True, description='Symptoms for prediction'),
    'diseases': fields.Raw()
})


#'diseases': fields.List(fields.List(fields.String()), required=False, description='Disease Diagnosis from symptoms')
@ns2.route('/')
class Predict(Resource):
    @ns2.expect(predict_model)
    @ns.marshal_with(predict_model, code=201)
    def post(self):
        symptoms = request.json
        final_syms = symptoms["symptoms"]
        symptoms["diseases"] = predictDisease(final_syms)
        print(symptoms)
        return symptoms


@ns.route('/')
class GetSymptoms(Resource):
    def get(self):
        return symptoms_index() 


@app.route("/hello-world", methods=["GET"])
def HelloWorld():
    return render_template("HelloWorld.html")