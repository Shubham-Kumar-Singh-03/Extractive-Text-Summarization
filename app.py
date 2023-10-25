from flask import Flask, render_template, request
from main import summarize

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['GET','POST'])
def analyze():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        summ, doc, len_original, len_summary = summarize(rawtext)

    return render_template('summary.html', summary = summ, doc = doc, olen = len_original, slen = len_summary)

if __name__=='__main__':
    app.run(debug=True)
