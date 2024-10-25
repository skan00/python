# currency_converter.py

# Currency data with name, symbol, and exchange rate based on USD
currencies = {
    "USD": {"name": "US Dollar", "symbol": "$", "rate": 1.0},
    "EUR": {"name": "Euro", "symbol": "€", "rate": 0.85},
    "GBP": {"name": "British Pound", "symbol": "£", "rate": 0.75},
    "JPY": {"name": "Japanese Yen", "symbol": "¥", "rate": 110.0}
}

def currency_converter():
    print("\n--- Currency Converter ---")
    
    # Display available currencies
    print("Available currencies:")
    for code, details in currencies.items():
        print(f"{code}: {details['name']} ({details['symbol']})")
    
    # Get source currency
    from_currency = input("Enter the currency you have (USD, EUR, GBP, JPY): ").upper()
    if from_currency not in currencies:
        print("Invalid source currency. Please try again.")
        return
    
    # Get target currency
    to_currency = input("Enter the currency you want (USD, EUR, GBP, JPY): ").upper()
    if to_currency not in currencies:
        print("Invalid target currency. Please try again.")
        return
    
    # Get the amount to convert
    try:
        amount = float(input(f"Enter amount in {from_currency}: "))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return

    # Perform conversion
    from_rate = currencies[from_currency]["rate"]
    to_rate = currencies[to_currency]["rate"]
    converted_amount = amount * (to_rate / from_rate)
    
    # Display result
    print(f"{currencies[from_currency]['symbol']}{amount:.2f} {from_currency} = {currencies[to_currency]['symbol']}{converted_amount:.2f} {to_currency}")
