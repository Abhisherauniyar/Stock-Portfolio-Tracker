# Simple Stock Investment Tracker
# Concepts used: Dictionary, Input/Output, Basic Arithmetic, File Handling

# Hardcoded dictionary of stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 145,
    "MSFT": 330
}

def get_stock_investment():
    """Take stock name and quantity from user, return name, qty, and investment value."""
    print("Available stocks:", ", ".join(stock_prices.keys()))
    name = input("Enter stock name: ").strip().upper()

    if name not in stock_prices:
        print(f"'{name}' not found in price list. Skipping.\n")
        return None

    try:
        qty = int(input(f"Enter quantity of {name}: "))
        if qty <= 0:
            print("Quantity must be greater than 0. Skipping.\n")
            return None
    except ValueError:
        print("Invalid quantity entered. Skipping.\n")
        return None

    price = stock_prices[name]
    investment = price * qty
    return (name, qty, price, investment)


def main():
    portfolio = []
    total_investment = 0

    print("=== Stock Investment Tracker ===\n")

    while True:
        result = get_stock_investment()
        if result:
            name, qty, price, investment = result
            portfolio.append(result)
            total_investment += investment
            print(f"Added: {qty} shares of {name} @ ${price} = ${investment}\n")

        again = input("Add another stock? (y/n): ").strip().lower()
        if again != "y":
            break

    # Display summary
    print("\n=== Investment Summary ===")
    for name, qty, price, investment in portfolio:
        print(f"{name}: {qty} shares x ${price} = ${investment}")
    print(f"\nTotal Investment Value: ${total_investment}")

    # Optionally save result to a .txt file
    save = input("\nSave this summary to a .txt file? (y/n): ").strip().lower()
    if save == "y":
        filename = "investment_summary.txt"
        with open(filename, "w") as file:
            file.write("=== Investment Summary ===\n")
            for name, qty, price, investment in portfolio:
                file.write(f"{name}: {qty} shares x ${price} = ${investment}\n")
            file.write(f"\nTotal Investment Value: ${total_investment}\n")
        print(f"Summary saved to '{filename}'.")


if __name__ == "__main__":
    main()
