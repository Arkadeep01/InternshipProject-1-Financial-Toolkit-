from Bulk_Calculator import Bulkcal as bulk
from Investment_Calculator import invcal as invest
from Mortgage_Calculator import mcal as mortgage
from Savings_Goal_Calculator import sgcal as savings
from Income_Tax_Calculator import ITCal as tax

def main():
    while True:
        print("\nFinancial Calculator Menu")
        print("1. Bulk Tax Calculator")
        print("2. Income Tax Calculator")
        print("3. Investment Calculator")
        print("4. Mortgage Calculator")
        print("5. Savings Goal Calculator")
        print("6. Exit")

        choice = input("Select an option (1-6): ")

        if choice == "1":
            bulk.bulk_income_tax_calculator()
        elif choice == "2":
            annual_income = float(input("Enter annual income: "))
            deductions = float(input("Enter deductions: "))
            filing_status = input("Enter filing status (Single/Married): ").capitalize()
            tax_credits = float(input("Enter tax credits: "))
            tax_due = tax.Income_Tax_Calculator(annual_income, deductions, filing_status, tax_credits)
            print(f"Income Tax Due: ${tax_due:.2f}")
        elif choice == "3":
            initial_investment = float(input("Enter initial investment: "))
            annual_rate_of_return = float(input("Enter annual rate of return (%): "))
            investment_period = int(input("Enter investment period (years): "))
            additional_contribution = float(input("Enter additional contribution per period (default 0): ") or 0)
            contribution_frequency = input("Contribution frequency (monthly/yearly, default yearly): ") or "yearly"
            compound_frequency = input("Compounding frequency (monthly/quarterly/semi-annually/annually, default annually): ") or "annually"

            future_value, total_contributions, total_interest = invest.investment_return_calculator(
                initial_investment, annual_rate_of_return, investment_period, additional_contribution,
                contribution_frequency, compound_frequency
            )
            print(f"Future Value: ${future_value:.2f}, Total Contributions: ${total_contributions:.2f}, Total Interest Earned: ${total_interest:.2f}")
        elif choice == "4":
            loan_amount = float(input("Enter loan amount: "))
            interest_rate = float(input("Enter annual interest rate (%): "))
            loan_terms = int(input("Enter loan term (years): "))

            monthly_payment, total_paid, total_interest = mortgage.mortgage_calculator(loan_amount, interest_rate, loan_terms)
            print(f"Monthly Payment: ${monthly_payment:.2f}, Total Paid: ${total_paid:.2f}, Total Interest: ${total_interest:.2f}")
        elif choice == "5":
            saving_goal = float(input("Enter savings goal: "))
            time_period = int(input("Enter time period (years): "))
            rate_of_return = float(input("Enter annual rate of return (%): "))

            monthly_saving = savings.savings_goal_calculator(saving_goal, time_period, rate_of_return)
            print(f"Required Monthly Saving: ${monthly_saving:.2f}")
        elif choice == "6":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
