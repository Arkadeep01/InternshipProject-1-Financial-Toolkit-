import tkinter as tk
from tkinter import messagebox
from ITCal import Income_Tax_Calculator  # Corrected function import

def compute_tax():
    try:
        income = float(entry_income.get())
        deductions = float(entry_deductions.get())
        tax_credits = float(entry_tax_credits.get())
        filing_status = filing_status_var.get()

        if not filing_status:
            messagebox.showerror("Input Error", "Please select a filing status.")
            return

        tax = Income_Tax_Calculator(income, deductions, filing_status, tax_credits)
        result_label.config(text=f"Estimated Tax: ${tax:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# GUI Setup
root = tk.Tk()
root.title("Income Tax Calculator")
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
title_label = tk.Label(root, text="Income Tax Calculator", font=title_font)
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Labels and Entries
tk.Label(root, text="Annual Income:", font=label_font).grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_income = tk.Entry(root, font=entry_font)
entry_income.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

tk.Label(root, text="Deductions:", font=label_font).grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_deductions = tk.Entry(root, font=entry_font)
entry_deductions.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

tk.Label(root, text="Tax Credits:", font=label_font).grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_tax_credits = tk.Entry(root, font=entry_font)
entry_tax_credits.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

# Filing Status Dropdown
tk.Label(root, text="Filing Status:", font=label_font).grid(row=4, column=0, padx=10, pady=5, sticky="w")

filing_status_var = tk.StringVar()
filing_status_dropdown = tk.OptionMenu(root, filing_status_var, "Single", "Married")
filing_status_dropdown.config(font=entry_font)
filing_status_dropdown.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

# Calculate Button
calculate_button = tk.Button(root, text="Calculate Tax", font=button_font, command=compute_tax)
calculate_button.grid(row=5, column=0, columnspan=2, pady=15)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue")
result_label.grid(row=6, column=0, columnspan=2, pady=10)

# Make it responsive
for i in range(2):
    root.grid_columnconfigure(i, weight=1)

if __name__ == "__main__":
    root.mainloop()
