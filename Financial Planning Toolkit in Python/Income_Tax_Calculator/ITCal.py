def Income_Tax_Calculator(annual_income, deductions, filing_status, tax_credits):
    taxable_income = annual_income - deductions
    tax_liability = 0

    # Define tax brackets for Single and Married
    tax_brackets = {
        "Single": [(11000, 0.10), (44725, 0.12), (95375, 0.22), (182100, 0.24), (231250, 0.32), (578125, 0.35), (float('inf'), 0.37)],
        "Married": [(22000, 0.10), (89450, 0.12), (190750, 0.22), (364200, 0.24), (462500, 0.32), (693750, 0.35), (float('inf'), 0.37)]
    }

    brackets = tax_brackets.get(filing_status, tax_brackets["Single"])

    #Calculate tax based on progressive brackets
    prev_limit = 0
    for limit, rate in brackets:
        if taxable_income > prev_limit:
            taxable_amount = min(taxable_income, limit) - prev_limit
            tax_liability += taxable_amount * rate
            prev_limit = limit


    net_tax = tax_liability - tax_credits
    if net_tax < 0:
        net_tax = 0         #no tax due
    
    return net_tax
