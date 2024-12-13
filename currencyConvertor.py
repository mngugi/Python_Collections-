import tkinter as tk
from tkinter import messagebox
import requests

# Function to fetch exchange rate from API
def get_exchange_rate(base, target):
    try:
        # Replace with your API key if using a paid service like CurrencyLayer or Open Exchange Rates
        url = f"https://api.exchangerate-api.com/v4/latest/{base}"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code != 200:
            raise Exception("Error fetching exchange rates")

        rate = data['rates'].get(target)
        if rate is None:
            raise ValueError("Invalid target currency")
        return rate
    except Exception as e:
        messagebox.showerror("Error", str(e))
        return None

# Function to convert the currency
def convert_currency():
    try:
        amount = float(entry_amount.get())
        base_currency = base_currency_var.get()
        target_currency = target_currency_var.get()

        if amount <= 0:
            raise ValueError("Please enter a positive amount")

        # Get exchange rate
        rate = get_exchange_rate(base_currency, target_currency)
        if rate is not None:
            result = amount * rate
            result_label.config(text=f"Converted Amount: {result:.2f} {target_currency}")
    except ValueError as ve:
        messagebox.showerror("Invalid Input", str(ve))
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Currency Converter")

# Create labels and input fields
tk.Label(root, text="Amount:").grid(row=0, column=0, padx=10, pady=10)
entry_amount = tk.Entry(root)
entry_amount.grid(row=0, column=1, padx=10, pady=10)

# Dropdown for base currency
tk.Label(root, text="From Currency:").grid(row=1, column=0, padx=10, pady=10)
base_currency_var = tk.StringVar()
base_currency_dropdown = tk.OptionMenu(root, base_currency_var, "USD", "EUR", "GBP", "INR", "JPY", "AUD", "CAD")
base_currency_dropdown.grid(row=1, column=1, padx=10, pady=10)

# Dropdown for target currency
tk.Label(root, text="To Currency:").grid(row=2, column=0, padx=10, pady=10)
target_currency_var = tk.StringVar()
target_currency_dropdown = tk.OptionMenu(root, target_currency_var, "USD", "EUR", "GBP", "INR", "JPY", "AUD", "CAD")
target_currency_dropdown.grid(row=2, column=1, padx=10, pady=10)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Label to display result
result_label = tk.Label(root, text="Converted Amount: ")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Set default currencies
base_currency_var.set("USD")
target_currency_var.set("EUR")

# Run the app
root.mainloop()
