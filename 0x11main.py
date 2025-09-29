# CLI Shopping Cart
# Users can add, view, and remove items, then checkout.
# Data is stored using dictionaries and lists.

print("Welcome to MiniMart!")

# Shopping cart stored as dictionary {item: quantity}
cart = {}

# Display menu
print("1. Add item to cart")
print("2. Remove item from cart")
print("3. View cart")
print("4. Checkout")

# Get user choice
choice = input("Choose an option: ")

# Handle choices
if choice == "1":
    item = input("Enter item name: ")
    quantity = int(input("Enter quantity: "))
    # Add or update item in cart
    if item in cart:
        cart[item] += quantity
    else:
        cart[item] = quantity
    print(f"{item} added to cart.")

elif choice == "2":
    item = input("Enter item name to remove: ")
    if item in cart:
        del cart[item]
        print(f"{item} removed from cart.")
    else:
        print(f"{item} not found in cart.")

elif choice == "3":
    if cart:
        print("Your cart contains:")
        print(cart)
    else:
        print("Your cart is empty.")

elif choice == "4":
    print("Thank you for shopping! You bought:")
    if cart:
        print(cart)
    else:
        print("Nothing (your cart was empty).")

else:
    print("Invalid choice. Please select 1, 2, 3, or 4.")