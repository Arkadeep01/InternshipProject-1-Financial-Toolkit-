import tkinter as tk
from tkinter import ttk, messagebox
from invcal import investment_return_calculator  

def compute_return():
    try:
        initial = float(entry_initial.get())
        rate = float(entry_rate.get())
        period = int(entry_period.get())
        additional = float(entry_contribution.get())

        contribution_freq = contribution_var.get()
        compound_freq = compound_var.get()

        if period <= 0:
            messagebox.showerror("Input Error", "Investment period must be greater than 0.")
            return

        future_value, total_contributions, total_interest = investment_return_calculator(
            initial, rate, period, additional, contribution_freq, compound_freq
        )

        result_label.config(
            text=f"Future Value: ${future_value:.2f}\n"
                 f"Total Contributions: ${total_contributions:.2f}\n"
                 f"Total Interest: ${total_interest:.2f}"
        )

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# GUI Setup
root = tk.Tk()
root.title("Investment Return Calculator")
root.geometry("550x450")
root.minsize(450, 400)

# Responsive Layout
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(7, weight=1)

# Fonts
title_font = ("Timmana", 16, "bold")
label_font = ("EB Garamond", 12)
entry_font = ("EB Garamond", 12)
button_font = ("Aleo", 12, "bold")

# Title
title_label = tk.Label(root, text="Investment Return Calculator", font=title_font)
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Labels and Entries
tk.Label(root, text="Initial Investment:", font=label_font).grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_initial = tk.Entry(root, font=entry_font)
entry_initial.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

tk.Label(root, text="Annual Rate of Return (%):", font=label_font).grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_rate = tk.Entry(root, font=entry_font)
entry_rate.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

tk.Label(root, text="Investment Period (Years):", font=label_font).grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_period = tk.Entry(root, font=entry_font)
entry_period.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

tk.Label(root, text="Additional Contribution:", font=label_font).grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry_contribution = tk.Entry(root, font=entry_font)
entry_contribution.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

# Contribution Frequency Dropdown
tk.Label(root, text="Contribution Frequency:", font=label_font).grid(row=5, column=0, padx=10, pady=5, sticky="w")

contribution_var = tk.StringVar()
contribution_dropdown = ttk.Combobox(root, textvariable=contribution_var, values=["monthly", "yearly"], font=entry_font)
contribution_dropdown.grid(row=5, column=1, padx=10, pady=5, sticky="ew")
contribution_dropdown.current(1)  # Default to yearly

# Compounding Frequency Dropdown
tk.Label(root, text="Compounding Frequency:", font=label_font).grid(row=6, column=0, padx=10, pady=5, sticky="w")

compound_var = tk.StringVar()
compound_dropdown = ttk.Combobox(root, textvariable=compound_var, values=["monthly", "quarterly", "semi-annually", "annually"], font=entry_font)
compound_dropdown.grid(row=6, column=1, padx=10, pady=5, sticky="ew")
compound_dropdown.current(3)  # Default to annually

# Calculate Button
calculate_button = tk.Button(root, text="Calculate Return", font=button_font, command=compute_return)
calculate_button.grid(row=7, column=0, columnspan=2, pady=15)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="blue")
result_label.grid(row=8, column=0, columnspan=2, pady=10)

# Make it responsive
for i in range(2):
    root.grid_columnconfigure(i, weight=1)

if __name__ == "__main__":
    root.mainloop()
