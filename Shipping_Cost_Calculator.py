def calculate_shipping():
    print("--- Logistics Shipping Cost Calculator ---")
    
    try:
        # Input package weight
        weight = float(input("Enter the package weight in kilograms: "))
        if weight < 0:
            print("Weight cannot be negative.")
            return

        # Input shipping rate
        rate = float(input("Enter the shipping rate per kilogram: "))
        if rate < 0:
            print("Rate cannot be negative.")
            return

        # Calculate shipping cost
        shipping_cost = weight * rate

        # Display the result formatted to 2 decimal places
        print(f"\nResult:")
        print(f"Shipping Cost: ${shipping_cost:,.2f} USD")
        
    except ValueError:
        print("Error: Invalid input. Please enter numeric values for weight and rate.")

if __name__ == "__main__":
    calculate_shipping()
