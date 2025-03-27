import tkinter as tk
from tkinter import messagebox
from mcal import mortgage_calculator  # Ensure 'mcal.py' is the correct file

def compute_mortgage():
    try:
        loan_amount = float(entry_loan.get())
        interest_rate = float(entry_interest.get())
        loan_terms = float(entry_terms.get())

        if loan_amount <= 0 or interest_rate < 0 or loan_terms <= 0:
            messagebox.showerror("Input Error", "Please enter positive values for loan amount and loan term.")
            return

        monthly_payment, total_paid, total_interest = mortgage_calculator(loan_amount, interest_rate, loan_terms)

        result_label.config(
            text=f"Monthly Payment: ${monthly_payment:.2f}\n"
                 f"Total Amount Paid: ${total_paid:.2f}\n"
                 f"Total Interest Paid: ${total_interest:.2f}"
        )

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# GUI Setup
root = tk.Tk()
root.title("Mortgage Calculator")
root.geometry("500x400")
root.minsize(400, 350)

# Responsive Layout
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(6, weight=1)

# Fonts
title_font = ("Timmana", 16, "bold")
label_font = ("EB Garamond", 12)
entry_font = ("EB Garamond", 12)
button_font = ("Aleo", 12, "bold")

# Title
title_label = tk.Label(root, text="Mortgage Calculator", font=title_font)
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Labels and Entries
tk.Label(root, text="Loan Amount ($):", font=label_font).grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_loan = tk.Entry(root, font=entry_font)
entry_loan.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

tk.Label(root, text="Interest Rate (%):", font=label_font).grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_interest = tk.Entry(root, font=entry_font)
entry_interest.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

tk.Label(root, text="Loan Term (Years):", font=label_font).grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_terms = tk.Entry(root, font=entry_font)
entry_terms.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

# Calculate Button
calculate_button = tk.Button(root, text="Calculate Mortgage", font=button_font, command=compute_mortgage)
calculate_button.grid(row=4, column=0, columnspan=2, pady=15)

# Result Label
result_label = tk.Label(root, text="", font=("Black Ops One", 14, "bold"), fg="blue")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Make it responsive
for i in range(2):
    root.grid_columnconfigure(i, weight=1)

if __name__ == "__main__":
    root.mainloop()
