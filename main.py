from flask import Flask, render_template, request,jsonify
from dotenv import load_dotenv
import os

config_file=os.path.abspath('config.env')
load_dotenv(config_file,override=True)

#load the tensorflow model
import nmt_model.model as NMT

app = Flask(__name__)

MODEL_EN_KOK_PATH = os.environ['MODEL_EN_KOK_PATH']
MODEL_KOK_EN_PATH = os.environ['MODEL_KOK_EN_PATH']

#loading the models from tensorflow SavedModel format
model_ek = NMT.load_model(MODEL_EN_KOK_PATH)
model_ke = NMT.load_model(MODEL_KOK_EN_PATH,model_type='KE')

@app.route('/', methods=['GET', 'POST'])
def index():
    output = {
                "Message":"TranslateKar Welcomes you!",
                'Request Type':'POST',
                "Endpoints":{
                            'English to Konkani':'/translate/en-kok/',
                            'Konkani to English':'/translate/kok-en/',
                        },
                "Request params":
                    {'input':'(str) string to be translated'},
                "Response params":
                    {   
                        'source':'(str) input string passed as request',
                        'target':'(str) translated string',
                        'target_lang':'(str) langauge of translated string'
                    },
              }
    return jsonify(output)

@app.route('/translate/en-kok/', methods=['POST'])
def translate_EK():
    input_data = request.json['input']
    translated_sentence = model_ek(input_data).numpy().decode()
    output = {
                'source':input_data,
                'target': translated_sentence,
                'target_lang':'Konkani',
            }
    print("JSON response:\n",output)
    return jsonify(output)

@app.route('/translate/kok-en/', methods=['POST'])
def translate_KE():
    input_data = request.json['input']
    translated_sentence = model_ke(input_data).numpy().decode()
    output = {
                'source':input_data,
                'target': translated_sentence,
                'target_lang':'English',
            }
    print("JSON response:\n",output)
    return jsonify(output)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000,debug=False,use_reloader=False)

