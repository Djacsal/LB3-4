from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def mortgage_calculator():
    if request.method == 'POST':

        loan_amount = int(request.form['loan_amount'])
        interest_rate = float(request.form['interest_rate']) / 100
        loan_term = int(request.form['loan_term'])

        monthly_interest_rate = interest_rate / 12
        num_payments = loan_term * 12
        monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)

        monthly_payment = round(monthly_payment, 2)

        return render_template('mortgage_calculator.html', monthly_payment=monthly_payment)
    else:
        return render_template('mortgage_calculator.html')


if __name__ == '__main__':
    app.run(debug=True)