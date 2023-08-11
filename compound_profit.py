from flask import Flask, render_template, request
app = Flask(__name__)

def calculate_compound_profit(balance, days, profit_percent):
    tmp = balance
    for i in range(days):
        tmp += tmp * profit_percent / 100
    return tmp, tmp - balance

@app.route('/', methods=['GET', 'POST'])
def calculate_page():
    if request.method == 'POST':
        try:
            balance = float(request.form['balance'])
            days = int(request.form['days'])
            profit_percent = float(request.form['profit_percent'])

            complex_profit, raw_profit = calculate_compound_profit(balance, days, profit_percent)

            complex_profit_formatted = "{:.0f}".format(complex_profit)
            raw_profit_formatted = "{:.0f}".format(raw_profit)

            return render_template('result.html', complex_profit=complex_profit_formatted, raw_profit=raw_profit_formatted)
        except ValueError:
            error_message = "Invalid input. Please enter valid numeric values."
            return render_template('index.html', error_message=error_message)

    return render_template('index.html', error_message=None)

if __name__ == '__main__':
    app.run(debug=True)
