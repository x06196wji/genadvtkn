from flask import Flask, render_template, request
import advtkn  
import os


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    _result = None
    if request.method == 'POST':
        input_data = request.form['input_data']
        # 在這裡呼叫 advtkn.py 中的函數，並傳入 input_data
        _result = advtkn.genAdvTkn(input_data)
    return render_template('index.html', result=_result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 443)))
