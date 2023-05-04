from flask import Flask, render_template, request
import nmt_model.model as NMT

app = Flask(__name__)
MODEL_NAME='TRANSFORMER_MINI_KOK_EN'
MODEL_PATH='/media/sajalmandrekar/BlackHole/NMT models/TRANS_MINI_KOK_EN_08_04/exported_translator'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        # do something with the text here, for example:
        processed_text = NMT.translate_text(model,text)

        return render_template('result.html', text=processed_text)
    return render_template('index.html')

if __name__ == '__main__':
    model = NMT.load_model(MODEL_NAME,MODEL_PATH)
    app.run(debug=True)

