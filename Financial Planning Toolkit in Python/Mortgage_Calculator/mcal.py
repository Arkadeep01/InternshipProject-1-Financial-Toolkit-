def mortgage_calculator(loan_amount, interest_rate, loan_terms):
    monthly_interest_rate = (interest_rate / 100) / 12
    total_payments = loan_terms * 12

    if monthly_interest_rate == 0:
        return loan_amount / total_payments

    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -total_payments)
    total_paid = monthly_payment * total_payments
    total_interest = total_paid - loan_amount

    return monthly_payment, total_paid, total_interest
