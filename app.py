from flask import Flask, render_template, request
from function import function

app = Flask(__name__)

@app.route("/")
def home():
    """Return index page with render template"""
    return render_template('index.html')

@app.route('/total', methods=['POST'])
def calculator_one():
    if request.method == 'POST':
        total = float(request.form['total_amount'])
        result_necesity = function(total, 0.40)
        result_desires = function(total, 0.25)
        result_savings = function(total, 0.35)

        return render_template('index.html', totalsNecesity = result_necesity, totalsDesires = result_desires, totalsSavings = result_savings, total = total)
    return render_template('index.html')

if __name__ == 'main':
    app.run(debug=True, port=5000)


