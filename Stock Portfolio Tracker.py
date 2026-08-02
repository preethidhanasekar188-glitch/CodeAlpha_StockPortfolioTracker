STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 145,
    "MSFT": 330
}


def show_available_stocks():
    """Display the list of stocks and their prices."""
    print("\nAvailable Stocks:")
    for stock, price in STOCK_PRICES.items():
        print(f"  {stock} - ${price}")


def get_portfolio():
    """Take user input for stock names and quantities, return as a dictionary."""
    portfolio = {}

    print("\nEnter the stocks you own. Type 'done' when finished.")

    while True:
        stock_name = input("\nEnter stock symbol (or 'done' to finish): ").upper().strip()

        if stock_name == "DONE":
            break

        if stock_name not in STOCK_PRICES:
            print("Stock not found in our price list. Please choose from the available stocks.")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock_name}: "))
            if quantity <= 0:
                print("Quantity must be a positive number.")
                continue
        except ValueError:
            print("Please enter a valid whole number for quantity.")
            continue

        if stock_name in portfolio:
            portfolio[stock_name] += quantity
        else:
            portfolio[stock_name] = quantity

    return portfolio


def calculate_investment(portfolio):
    """Calculate total investment value and per-stock breakdown."""
    breakdown = {}
    total_value = 0

    for stock, quantity in portfolio.items():
        price = STOCK_PRICES[stock]
        value = price * quantity
        breakdown[stock] = value
        total_value += value

    return breakdown, total_value


def display_summary(portfolio, breakdown, total_value):
    """Print a formatted summary of the portfolio."""
    print("\n" + "=" * 40)
    print("PORTFOLIO SUMMARY")
    print("=" * 40)
    print(f"{'Stock':<10}{'Qty':<8}{'Price':<10}{'Value':<10}")
    print("-" * 40)

    for stock, quantity in portfolio.items():
        price = STOCK_PRICES[stock]
        value = breakdown[stock]
        print(f"{stock:<10}{quantity:<8}${price:<9}${value:<9}")

    print("-" * 40)
    print(f"Total Investment Value: ${total_value}")
    print("=" * 40)


def save_to_file(portfolio, breakdown, total_value):
    """Save the portfolio summary to a .txt file."""
    filename = "portfolio_summary.txt"

    with open(filename, "w") as file:
        file.write("PORTFOLIO SUMMARY\n")
        file.write("=" * 40 + "\n")
        file.write(f"{'Stock':<10}{'Qty':<8}{'Price':<10}{'Value':<10}\n")
        file.write("-" * 40 + "\n")

        for stock, quantity in portfolio.items():
            price = STOCK_PRICES[stock]
            value = breakdown[stock]
            file.write(f"{stock:<10}{quantity:<8}${price:<9}${value:<9}\n")

        file.write("-" * 40 + "\n")
        file.write(f"Total Investment Value: ${total_value}\n")

    print(f"\nSummary saved to '{filename}'")


def main():
    print("Welcome to the Stock Portfolio Tracker!")
    show_available_stocks()

    portfolio = get_portfolio()

    if not portfolio:
        print("\nNo stocks were added. Exiting program.")
        return

    breakdown, total_value = calculate_investment(portfolio)
    display_summary(portfolio, breakdown, total_value)

    save_choice = input("\nDo you want to save this summary to a file? (yes/no): ").lower().strip()
    if save_choice == "yes":
        save_to_file(portfolio, breakdown, total_value)

    print("\nThank you for using the Stock Portfolio Tracker!")


if __name__ == "__main__":
    main()
