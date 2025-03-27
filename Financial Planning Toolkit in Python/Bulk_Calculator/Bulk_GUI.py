import tkinter as tk
from tkinter import messagebox
from Bulkcal import calculate_tax  # Import tax calculation function

def compute_tax():
    try:
        income = float(entry_income.get())
        deductions = float(entry_deductions.get())
        credits = float(entry_credits.get())
        tax_credits = float(entry_tax_credits.get())  # Added missing argument

        tax = calculate_tax(income, deductions, credits, tax_credits)  # Fixed function call
        result_label.config(text=f"Estimated Tax: ${tax:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# GUI Setup
root = tk.Tk()
root.title("Bulk Tax Calculator")
root.geometry("500x350")  # Default size
root.minsize(400, 300)  # Prevent too small resizing

# Responsive Layout
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(5, weight=1)

# Fonts
title_font = ("Timmana", 16, "bold")
label_font = ("EB Garamond", 12)
entry_font = ("EB Garamond", 12)
button_font = ("Aleo", 12, "bold")

# Title
title_label = tk.Label(root, text="Bulk Tax Calculator", font=title_font)
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Labels and Entries
tk.Label(root, text="Annual Income:", font=label_font).grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_income = tk.Entry(root, font=entry_font)
entry_income.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

tk.Label(root, text="Deductions:", font=label_font).grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_deductions = tk.Entry(root, font=entry_font)
entry_deductions.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

tk.Label(root, text="Tax Credits:", font=label_font).grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_credits = tk.Entry(root, font=entry_font)
entry_credits.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

tk.Label(root, text="Additional Tax Credits:", font=label_font).grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry_tax_credits = tk.Entry(root, font=entry_font)
entry_tax_credits.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

# Calculate Button
calculate_button = tk.Button(root, text="Calculate Tax", font=button_font, command=compute_tax)
calculate_button.grid(row=5, column=0, columnspan=2, pady=15)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue")
result_label.grid(row=6, column=0, columnspan=2, pady=10)

# Make it responsive
for i in range(2):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
