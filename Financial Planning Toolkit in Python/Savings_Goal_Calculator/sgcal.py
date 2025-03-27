def savings_goal_calculator(saving_goal, time_period, rate_of_return):
    
    #Convert annual rate of monthly rate
    monthly_rate = (rate_of_return / 100) / 12
    total_months = time_period * 12

    #if interest rate is 0, simpley divide
    if monthly_rate == 0:
        monthly_saving = saving_goal / total_months
    else:
        monthly_saving = (saving_goal * monthly_rate) / ((1 + monthly_rate)** total_months - 1)

    return monthly_saving

