#BIT1228025
def display():
    print("-------------------------------")
    print("Available Currencies:")
    print("1. USD - United States Dollar")
    print("2. EUR - Euro")
    print("3. GBP - British Pound")
    print("4. JPY - Japanese Yen")
    print("-------------------------------")
    choice = input("Enter choice (1/2/3/4): ")
    
def getexchangerate(fromcurrency, tocurrency):
    rates = {
        'USD': {'USD': 1.0, 'EUR': 1.18, 'GBP': 1.33, 'JPY': 0.0091},
        'EUR': {'USD': 0.85, 'EUR': 1.0, 'GBP': 0.88, 'JPY': 129.09},
        'GBP': {'USD': 0.75, 'EUR': 1.13, 'GBP': 1.0, 'JPY': 146.25},
        'JPY': {'USD': 110.0, 'EUR': 0.0078, 'GBP': 0.0068, 'JPY': 1.0}
    }
    return rates[fromcurrency][tocurrency]

def convertcurrency(amount, fromcurrency, tocurrency):
    exchangerate = getexchangerate(fromcurrency, tocurrency)
    convertedamount = amount * exchangerate
    return convertedamount

def main():
    print("-----------------------------------")
    print("Welcome to the Currency Converter!")
    print("-----------------------------------")
    
    while True:
        display()

        amount = float(input("Enter the amount you want to convert: "))
        fromcurrency = input("Enter the currency you want to convert from (Example, USD): ").upper()
        tocurrency = input("Enter the currency you want to convert to (Example, EUR): ").upper()

        converted_amount = convertcurrency(amount, fromcurrency, tocurrency)
        print(f"Converted Amount: {converted_amount:.2f} {tocurrency}")

        choice = input("Do you want to convert another amount? (yes/no): ").lower()
        if choice != 'yes':
            break

if __name__ == "__main__":
    main()