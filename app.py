from flask import Flask, render_template, request
from function import calculatorNecesity, calculatorDesires, calculatorSavings

app = Flask(__name__)

@app.route("/")
def home():
    """Return index page with render template"""
    return render_template('index.html')

@app.route('/total', methods=['POST'])
def cal():
    if request.method == 'POST':
        total = float(request.form['total_amount'])
        result_necesity = calculatorNecesity(total)
        result_desires = calculatorDesires(total)
        result_savings = calculatorSavings(total)

        return render_template("index.html", totalsNecesity = result_necesity, totalsDesires = result_desires, totalsSavings = result_savings, total = total)
    return render_template('index.html')

if __name__ == 'main':
    app.run(debug=True, port=5000)


