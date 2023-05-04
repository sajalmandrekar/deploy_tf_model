from flask import Flask, render_template, request
import nmt_model.model as NMT
import os

app = Flask(__name__)
MODEL_NAME='TRANSFORMER_MINI_KOK_EN'

if 'MODEL_PATH' not in os.environ:
    MODEL_PATH='/media/sajalmandrekar/BlackHole/NMT models/TRANS_MINI_KOK_EN_08_04/exported_translator'
else:
    MODEL_PATH=os.environ['MODEL_PATH']


@app.route('/', methods=['GET', 'POST'])
def index():
    processed_text = None
    if request.method == 'POST':
        text = request.form['text']
        # do something with the text here, for example:
        processed_text = NMT.translate_text(model,text)
        print("Translated_text:",processed_text)

    return render_template('index.html', processed_text=processed_text, input_text=request.form.get('text', ''))

if __name__ == '__main__':
    model = NMT.load_model(MODEL_NAME,MODEL_PATH)
    app.run(debug=True)

