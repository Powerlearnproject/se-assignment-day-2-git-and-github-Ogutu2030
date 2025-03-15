def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if it is 20% or higher.
    
    Parameters:
    - price (float): The original price of the item.
    - discount_percent (float): The discount percentage.
    
    Returns:
    - float: The final price after applying the discount, or the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user to input the original price and discount percentage
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate the final price using the function
    final_price = calculate_discount(price, discount_percent)

    # Print the result
    if final_price == price:
        print(f"No discount applied. The original price remains: ${price:.2f}")
    else:
        print(f"Discount applied! The final price is: ${final_price:.2f}")
except ValueError:
    print("Please enter valid numbers for the price and discount percentage.")
