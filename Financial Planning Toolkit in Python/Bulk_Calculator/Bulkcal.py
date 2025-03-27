def calculate_tax(annual_income, deductions, filing_status, tax_credits):
    """
    Calculate tax liability for a given income, deductions, and filing status.
    :param annual_income: Total annual income
    :param deductions: Applicable deductions
    :param filing_status: Filing status ('Single' or 'Married')
    :param tax_credits: Applicable tax credits
    :return: Tax liability amount
    """
    tax_brackets = {
        "Single": [(11000, 0.10), (44725, 0.12), (95375, 0.22), (182100, 0.24), (231250, 0.32), (578125, 0.35), (float('inf'), 0.37)],
        "Married": [(22000, 0.10), (89450, 0.12), (190750, 0.22), (364200, 0.24), (462500, 0.32), (693750, 0.35), (float('inf'), 0.37)]
    }

    taxable_income = annual_income - deductions
    tax_liability = 0
    prev_limit = 0

    for limit, rate in tax_brackets.get(filing_status, tax_brackets["Single"]):
        if taxable_income > prev_limit:
            taxable_amount = min(taxable_income, limit) - prev_limit
            tax_liability += taxable_amount * rate
            prev_limit = limit

    net_tax = max(0, tax_liability - tax_credits)
    return round(net_tax, 2)


def bulk_income_tax_calculator():
    """
    Take user input for multiple users and calculate their tax liabilities.
    """
    num_users = int(input("Enter the number of users: "))
    users_data = []

    for i in range(num_users):
        print(f"\nEnter details for User {i + 1}:")
        name = input("Name: ")
        annual_income = float(input("Annual Income: "))
        deductions = float(input("Deductions: "))
        filing_status = input("Filing Status (Single/Married): ").capitalize()
        tax_credits = float(input("Tax Credits: "))

        tax_liability = calculate_tax(annual_income, deductions, filing_status, tax_credits)
        users_data.append({"Name": name, "Tax Liability": tax_liability})

    print("\nCalculated Tax Liabilities:")
    for user in users_data:
        print(f"{user['Name']} - Tax Liability: ${user['Tax Liability']:.2f}")

