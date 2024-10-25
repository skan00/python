# currency_converter.py

# Exchange rates for the currency converter
exchange_rates = {
    "USD": {"EUR": 0.85, "GBP": 0.75},
    "EUR": {"USD": 1.18, "GBP": 0.88},
    "GBP": {"USD": 1.33, "EUR": 1.14}
}

def currency_converter():
    print("\n--- Currency Converter ---")
    from_currency = input("Enter the currency you have (USD, EUR, GBP): ").upper()
    to_currency = input("Enter the currency you want (USD, EUR, GBP): ").upper()
    if from_currency in exchange_rates and to_currency in exchange_rates[from_currency]:
        amount = float(input(f"Enter amount in {from_currency}: "))
        converted_amount = amount * exchange_rates[from_currency][to_currency]
        print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    else:
        print("Currency conversion not available for selected currencies.")

