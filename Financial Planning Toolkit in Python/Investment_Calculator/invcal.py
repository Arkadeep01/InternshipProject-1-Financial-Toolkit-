def investment_return_calculator(initial_investment, annual_rate_of_return, investment_period, additional_contribution=0, contribution_frequency='yearly', compound_frequency='annually'):
    compound_map = {'monthly': 12, 'quarterly': 4, 'semi-annually': 2, 'annually': 1}
    compounding_periods = compound_map.get(compound_frequency, 1)
    contribution_periods = 12 if contribution_frequency == 'monthly' else 1

    future_value = initial_investment
    total_contributions = 0

    for year in range(1, investment_period + 1):
        for _ in range(contribution_periods):
            future_value += additional_contribution
            total_contributions += additional_contribution

        for _ in range(compounding_periods):
            future_value *= (1 + (annual_rate_of_return / 100) / compounding_periods)

    total_interest = future_value - initial_investment - total_contributions

    return future_value, total_contributions, total_interest
